"""
Internationalization dictionary for English and French.
Contains exact hard-coded historical sentences, UI labels, and error messages.
"""

MESSAGES = {
    "en": {
        # App branding & navigation
        "app_title": "Titanic Survival Predictor",
        "nav_predict": "Predictor",
        "nav_how_it_works": "How it works",
        "lang_switch": "Français",
        "lang_target": "fr",
        
        # Form sections & labels
        "form_title": "Calculate Your Survival Probability",
        "form_subtitle": "Conditioned on tabular Bayesian inference powered by TabPFN v2.",
        "required_section_title": "Required Details",
        "required_section_desc": "Essential biographical and role parameters.",
        "optional_section_title": "Optional Details",
        "optional_section_desc": "Leave blank if unknown. TabPFN naturally handles missing data.",
        
        # Field labels & helpers
        "label_name": "Full Name",
        "label_sex": "Sex",
        "label_age": "Age (years)",
        "label_pclass": "Class / Department (Pclass)",
        "label_person_role": "Passenger / Crew Role",
        "label_sibsp": "Number of Siblings / Spouses Aboard (SibSp)",
        "label_parch": "Number of Parents / Children Aboard (Parch)",
        "label_fare": "Ticket Fare (£ British Pounds)",
        "label_embarked": "Port of Embarkation",
        "label_height": "Height (cm)",
        "label_weight": "Weight (kg)",
        "label_title": "Social Title",
        "label_home_dest": "Hometown / Final Destination",
        "label_occupation": "Occupation / Job",
        "btn_predict": "Calculate Survival Chances",
        "btn_predicting": "Running TabPFN Bayesian Inference...",
        
        # Choices
        "sex_male": "Male",
        "sex_female": "Female",
        "role_normal_passenger": "Normal Passenger",
        "role_engineering_crew": "Engineering Crew",
        "role_other_crew": "Other Crew (Deck, Victualling, Restaurant)",
        "embarked_s": "Southampton (S)",
        "embarked_c": "Cherbourg (C)",
        "embarked_q": "Queenstown (Q)",
        "embarked_b": "Belfast (B)",
        "select_placeholder": "-- Select an option --",
        "none_placeholder": "-- Optional --",
        
        # Results page
        "result_title": "Prediction Outcome",
        "status_survived": "SURVIVED",
        "status_died": "DID NOT SURVIVE",
        "metric_probability": "Survival Probability",
        "metric_confidence": "Model Confidence",
        "metric_completeness": "Data Completeness",
        "confidence_tooltip": "Defined as max(p, 1 - p), representing the certainty of the predicted outcome.",
        "completeness_tooltip": "Percentage of the 13 model features provided.",
        "btn_try_another": "Test Another Profile",
        "match_title": "Historical Match in Passenger Records",
        
        # Musician Easter Egg
        "musician_title": "The Titanic Band",
        "musician_subtitle": "April 15, 1912 — 02:20 AM",
        "musician_view_normal": "View standard model prediction",
        "audio_play": "Listen to commemorative recording",
        
        # Validation errors
        "error_required": "This field is required.",
        "error_invalid_number": "Please enter a valid numeric value.",
        "error_age_range": "Age must be between 0.1 and 120 years.",
        "error_fare_negative": "Fare cannot be negative.",
        
        # How It Works page
        "how_title": "How the Titanic Predictor Works",
        "how_intro": "An honest look at TabPFN meta-learning, historical feature dynamics, and limitations.",
    },
    
    "fr": {
        # App branding & navigation
        "app_title": "Prédicteur de Survie du Titanic",
        "nav_predict": "Prédicteur",
        "nav_how_it_works": "Comment ça marche",
        "lang_switch": "English",
        "lang_target": "en",
        
        # Form sections & labels
        "form_title": "Calculez vos chances de survie",
        "form_subtitle": "Inférence bayésienne tabulaire optimisée par TabPFN v2.",
        "required_section_title": "Champs Obligatoires",
        "required_section_desc": "Paramètres biographiques et rôle essentiels.",
        "optional_section_title": "Champs Optionnels",
        "optional_section_desc": "Laissez vide si inconnu. TabPFN traite nativement les valeurs manquantes.",
        
        # Field labels & helpers
        "label_name": "Nom complet",
        "label_sex": "Sexe",
        "label_age": "Âge (années)",
        "label_pclass": "Classe / Département (Pclass)",
        "label_person_role": "Rôle Passager / Équipage",
        "label_sibsp": "Frères/Sœurs/Époux à bord (SibSp)",
        "label_parch": "Parents/Enfants à bord (Parch)",
        "label_fare": "Prix du billet (£ Livres sterling)",
        "label_embarked": "Port d'embarquement",
        "label_height": "Taille (cm)",
        "label_weight": "Poids (kg)",
        "label_title": "Titre civil",
        "label_home_dest": "Ville d'origine / Destination finale",
        "label_occupation": "Profession / Métier",
        "btn_predict": "Calculer les chances de survie",
        "btn_predicting": "Inférence bayésienne TabPFN en cours...",
        
        # Choices
        "sex_male": "Homme",
        "sex_female": "Femme",
        "role_normal_passenger": "Passager standard",
        "role_engineering_crew": "Équipage mécanique (Engineering)",
        "role_other_crew": "Autre équipage (Pont, Restauration, Service)",
        "embarked_s": "Southampton (S)",
        "embarked_c": "Cherbourg (C)",
        "embarked_q": "Queenstown (Q)",
        "embarked_b": "Belfast (B)",
        "select_placeholder": "-- Sélectionner une option --",
        "none_placeholder": "-- Optionnel --",
        
        # Results page
        "result_title": "Résultat de la Prédiction",
        "status_survived": "A SURVÉCU",
        "status_died": "N'A PAS SURVÉCU",
        "metric_probability": "Probabilité de survie",
        "metric_confidence": "Confiance du modèle",
        "metric_completeness": "Complétude des données",
        "confidence_tooltip": "Défini par max(p, 1 - p), mesurant la certitude sur la classe prédite.",
        "completeness_tooltip": "Pourcentage des 13 caractéristiques renseignées.",
        "btn_try_another": "Tester un autre profil",
        "match_title": "Correspondance historique dans les registres",
        
        # Musician Easter Egg
        "musician_title": "L'Orchestre du Titanic",
        "musician_subtitle": "15 avril 1912 — 02h20",
        "musician_view_normal": "Consulter la prédiction standard du modèle",
        "audio_play": "Écouter l'enregistrement commémoratif",
        
        # Validation errors
        "error_required": "Ce champ est obligatoire.",
        "error_invalid_number": "Veuillez entrer une valeur numérique valide.",
        "error_age_range": "L'âge doit être compris entre 0,1 et 120 ans.",
        "error_fare_negative": "Le prix du billet ne peut pas être négatif.",
        
        # How It Works page
        "how_title": "Comment fonctionne le prédicteur",
        "how_intro": "Une analyse rigoureuse du méta-apprentissage TabPFN, des facteurs historiques et des limites.",
    }
}

# SECTION 5: Hard-coded outcome sentences (Exact specifications)

def get_passenger_tier_sentence(prob_percent: int, lang: str = "en") -> str:
    """
    Returns the exact hard-coded normal passenger sentence according to probability tier.
    """
    p = int(round(prob_percent))
    if p < 20:
        if lang == "fr":
            return f"Si vous aviez été à bord du Titanic, vous n'auriez eu que {p} % de chances de survie. Malheureusement, l'histoire ne vous aurait probablement pas épargné."
        return f"If you had been aboard the Titanic, you would have had only a {p}% chance of survival. Sadly, history would most likely not have been kind to you."
    elif p < 50:
        if lang == "fr":
            return f"Si vous aviez été à bord du Titanic, vous auriez eu {p} % de chances de survie. Les probabilités étaient contre vous, mais une place dans un canot de sauvetage n'était pas hors de portée."
        return f"If you had been aboard the Titanic, you would have had a {p}% chance of survival. The odds were against you, but a place in a lifeboat was not out of reach."
    elif p < 80:
        if lang == "fr":
            return f"Si vous aviez été à bord du Titanic, vous auriez eu {p} % de chances de survie. Vous auriez très probablement trouvé une place dans un canot de sauvetage."
        return f"If you had been aboard the Titanic, you would have had a {p}% chance of survival. You would most likely have found a seat in a lifeboat."
    else:
        if lang == "fr":
            return f"Si vous aviez été à bord du Titanic, vous auriez eu {p} % de chances de survie. La chance vous aurait souri cette nuit-là."
        return f"If you had been aboard the Titanic, you would have had a {p}% chance of survival. Fortune would have smiled on you that night."

def get_crew_sentence(prob_percent: int, lang: str = "en") -> str:
    """
    Returns the exact hard-coded crew sentence.
    """
    p = int(round(prob_percent))
    if lang == "fr":
        return f"Merci pour votre service. À bord du Titanic, vous auriez eu {p} % de chances de survie."
    return f"Thank you for your service. Aboard the Titanic, you would have had a {p}% chance of survival."

def get_musician_sentence(lang: str = "en") -> str:
    """
    Returns the exact hard-coded Musician easter egg text.
    """
    if lang == "fr":
        return (
            "L'orchestre a continué de jouer. La légende raconte que les musiciens ont joué "
            "jusqu'au bout pour que les autres puissent rejoindre les canots de sauvetage. "
            "Quelles que soient les probabilités, vous seriez resté à votre poste. Merci pour la musique."
        )
    return (
        "The band played on. Legend says the musicians kept playing until the very end "
        "so that others could reach the lifeboats. Whatever the odds, you would have stayed at your post. "
        "Thank you for the music."
    )

def format_match_message(name: str, role: str, age: str, pclass: str, home_dest: str, survived: bool, additional_matches: int = 0, lang: str = "en") -> str:
    """
    Formats the exact historical passenger match message.
    """
    dest_str_en = f" from {home_dest}" if home_dest and home_dest.lower() != "unknown" else ""
    dest_str_fr = f" depuis {home_dest}" if home_dest and home_dest.lower() != "unknown" else ""
    
    if survived:
        status_en = "Historically, this person survived."
        status_fr = "Historiquement, cette personne a survécu."
    else:
        status_en = "Sadly, this person did not survive."
        status_fr = "Malheureusement, cette personne n'a pas survécu."
        
    extra_en = f" and {additional_matches} other person(s) share this profile." if additional_matches > 0 else ""
    extra_fr = f" et {additional_matches} autre(s) personne(s) partagent ce profil." if additional_matches > 0 else ""

    if lang == "fr":
        msg = f"Vous êtes peut-être {name} ! {role}, {age} ans, voyageant en {pclass}{dest_str_fr}. {status_fr}{extra_fr}"
    else:
        msg = f"You might be {name}! A {role} aged {age}, traveling in {pclass}{dest_str_en}. {status_en}{extra_en}"
    return msg
