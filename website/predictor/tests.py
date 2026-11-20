import json
from django.test import TestCase, Client
from django.urls import reverse
from predictor.forms import PredictorForm
from predictor.messages_i18n import (
    MESSAGES,
    get_passenger_tier_sentence,
    get_crew_sentence,
    get_musician_sentence,
    format_match_message
)
from predictor.matching import match_passenger
from predictor.ml_service import MLService

class TitanicUnitAndIntegrationTests(TestCase):
    def setUp(self):
        self.client = Client()

    # 1. Form Validation Tests
    def test_form_validation_valid_minimal(self):
        """Minimal input with only the 4 required fields."""
        data = {
            "Sex": "female",
            "Age": 28.0,
            "Pclass": "1",
            "Person_Role": "Normal Passenger"
        }
        form = PredictorForm(data=data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_form_validation_missing_required(self):
        """Missing required fields must fail."""
        data = {
            "Age": 28.0
            # Missing Sex, Pclass, Person_Role
        }
        form = PredictorForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("Sex", form.errors)
        self.assertIn("Pclass", form.errors)
        self.assertIn("Person_Role", form.errors)

    def test_form_validation_invalid_age(self):
        """Negative age or age > 120 must fail."""
        data = {
            "Sex": "female",
            "Age": -5.0,
            "Pclass": "1",
            "Person_Role": "Normal Passenger"
        }
        form = PredictorForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("Age", form.errors)

    def test_form_validation_negative_fare(self):
        """Negative fare must fail."""
        data = {
            "Sex": "male",
            "Age": 30.0,
            "Pclass": "3",
            "Person_Role": "Normal Passenger",
            "Fare": -15.5
        }
        form = PredictorForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("Fare", form.errors)

    # 2. Probability Tier Selection Tests
    def test_passenger_tier_selection_en(self):
        # Tier p < 20
        s_10 = get_passenger_tier_sentence(10, lang="en")
        self.assertIn("only a 10% chance of survival", s_10)
        self.assertIn("history would most likely not have been kind to you", s_10)

        # Tier 20 <= p < 50
        s_35 = get_passenger_tier_sentence(35, lang="en")
        self.assertIn("35% chance of survival", s_35)
        self.assertIn("The odds were against you", s_35)

        # Tier 50 <= p < 80
        s_65 = get_passenger_tier_sentence(65, lang="en")
        self.assertIn("65% chance of survival", s_65)
        self.assertIn("found a seat in a lifeboat", s_65)

        # Tier p >= 80
        s_90 = get_passenger_tier_sentence(90, lang="en")
        self.assertIn("90% chance of survival", s_90)
        self.assertIn("Fortune would have smiled on you", s_90)

    def test_passenger_tier_selection_fr(self):
        s_15 = get_passenger_tier_sentence(15, lang="fr")
        self.assertIn("que 15 % de chances de survie", s_15)
        self.assertIn("l'histoire ne vous aurait probablement pas épargné", s_15)

        s_40 = get_passenger_tier_sentence(40, lang="fr")
        self.assertIn("40 % de chances de survie", s_40)
        self.assertIn("place dans un canot de sauvetage n'était pas hors de portée", s_40)

        s_70 = get_passenger_tier_sentence(70, lang="fr")
        self.assertIn("70 % de chances de survie", s_70)
        self.assertIn("trouvé une place dans un canot de sauvetage", s_70)

        s_85 = get_passenger_tier_sentence(85, lang="fr")
        self.assertIn("85 % de chances de survie", s_85)
        self.assertIn("La chance vous aurait souri cette nuit-là", s_85)

    # 3. Crew Sentence Tests
    def test_crew_sentence(self):
        en_crew = get_crew_sentence(24, lang="en")
        self.assertEqual(en_crew, "Thank you for your service. Aboard the Titanic, you would have had a 24% chance of survival.")

        fr_crew = get_crew_sentence(24, lang="fr")
        self.assertEqual(fr_crew, "Merci pour votre service. À bord du Titanic, vous auriez eu 24 % de chances de survie.")

    # 4. Musician Trigger & Easter Egg Tests
    def test_musician_trigger_logic(self):
        en_musician = get_musician_sentence(lang="en")
        self.assertIn("The band played on", en_musician)
        self.assertIn("Thank you for the music", en_musician)

        fr_musician = get_musician_sentence(lang="fr")
        self.assertIn("L'orchestre a continué de jouer", fr_musician)
        self.assertIn("Merci pour la musique", fr_musician)

    # 5. Matching Logic Tests
    def test_matching_by_name(self):
        # Fuzzy match on Elisabeth Walton Allen
        match = match_passenger({"name": "Elisabeth Allen"}, lang="en")
        self.assertIsNotNone(match)
        self.assertIn("Allen", match["name"])
        self.assertTrue(match["survived"])
        self.assertIn("Historically, this person survived.", match["message"])

    def test_matching_by_key_features(self):
        # Match by Sex + Age + Pclass + Fare
        match = match_passenger({
            "Sex": "female",
            "Age": 29.0,
            "Pclass": "1",
            "Fare": 211.3375
        }, lang="en")
        self.assertIsNotNone(match)
        self.assertIn("Allen", match["name"])

    def test_matching_insufficient_features_returns_none(self):
        # Only Sex + Age + Pclass without SibSp/Parch/Fare -> No match
        match = match_passenger({
            "Sex": "female",
            "Age": 29.0,
            "Pclass": "1"
        }, lang="en")
        self.assertIsNone(match)

    # 6. Language Switch Tests
    def test_language_switch_endpoint(self):
        # Switch to FR
        response = self.client.get(reverse('set_language') + "?lang=fr")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session.get('lang'), 'fr')

        # Load page in FR
        page_resp = self.client.get(reverse('predict'))
        self.assertEqual(page_resp.status_code, 200)
        self.assertContains(page_resp, "Prédicteur de Survie du Titanic")
        self.assertContains(page_resp, "Champs Obligatoires")

        # Switch back to EN
        response = self.client.get(reverse('set_language') + "?lang=en")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session.get('lang'), 'en')

        page_resp_en = self.client.get(reverse('predict'))
        self.assertEqual(page_resp_en.status_code, 200)
        self.assertContains(page_resp_en, "Titanic Survival Predictor")
        self.assertContains(page_resp_en, "Required Details")

    # 7. Django Test Client Scenarios
    def test_client_scenario_normal_passenger(self):
        """Scenario A: 1st class adult female passenger (high survival expected)."""
        data = {
            "Sex": "female",
            "Age": 30.0,
            "Pclass": "1",
            "Person_Role": "Normal Passenger",
            "SibSp": 1,
            "Parch": 0,
            "Fare": 80.0,
            "Embarked": "C"
        }
        response = self.client.post(reverse('predict'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "SURVIVED")
        self.assertContains(response, "Survival Probability")
        self.assertContains(response, "Model Confidence")
        self.assertContains(response, "Data Completeness")

    def test_client_scenario_crew_member(self):
        """Scenario B: Male fireman in engineering crew."""
        data = {
            "Sex": "male",
            "Age": 28.0,
            "Pclass": "Engineering Crew",
            "Person_Role": "Engineering Crew",
            "Occupation": "Fireman"
        }
        response = self.client.post(reverse('predict'), data=data)
        self.assertEqual(response.status_code, 200)
        # Should render crew sentence
        self.assertContains(response, "Thank you for your service.")

    def test_client_scenario_musician_trigger(self):
        """Scenario C: Musician easter egg takes precedence over all else."""
        data = {
            "Sex": "male",
            "Age": 33.0,
            "Pclass": "Band",
            "Person_Role": "Other Crew",
            "Occupation": "Musician"
        }
        response = self.client.post(reverse('predict'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The band played on")
        self.assertContains(response, "Thank you for the music")

    def test_client_scenario_exact_dataset_match(self):
        """Scenario D: Exact dataset match for Master Hudson Trevor Allison."""
        data = {
            "name": "Hudson Trevor Allison",
            "Sex": "male",
            "Age": 0.9,
            "Pclass": "1",
            "Person_Role": "Normal Passenger",
            "SibSp": 1,
            "Parch": 2,
            "Fare": 151.55,
            "Embarked": "S"
        }
        response = self.client.post(reverse('predict'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You might be")
        self.assertContains(response, "Allison")

    def test_client_scenario_minimal_input(self):
        """Scenario E: Minimal input with only the 4 required fields."""
        data = {
            "Sex": "male",
            "Age": 22.0,
            "Pclass": "3",
            "Person_Role": "Normal Passenger"
        }
        response = self.client.post(reverse('predict'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "DID NOT SURVIVE")
        self.assertContains(response, "Survival Probability")
        # Completeness should be 4/13 = 30.8%
        self.assertContains(response, "30.8%")
