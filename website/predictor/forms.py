import os
import json
from django import forms
from .messages_i18n import MESSAGES

# Load feature categories
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FEATURE_LIST_PATH = os.path.join(BASE_DIR, "ml", "artifacts", "feature_list.json")

def load_categories():
    if os.path.exists(FEATURE_LIST_PATH):
        with open(FEATURE_LIST_PATH, "r") as f:
            meta = json.load(f)
            return meta.get("categories", {})
    return {}

CATEGORIES = load_categories()

class PredictorForm(forms.Form):
    # Optional name for matching
    name = forms.CharField(
        max_length=120,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'e.g. John Jacob Astor'
        })
    )

    # Required fields
    Sex = forms.ChoiceField(
        required=True,
        choices=[
            ('', '-- Select Sex --'),
            ('female', 'Female'),
            ('male', 'Male')
        ],
        widget=forms.Select(attrs={'class': 'form-select', 'required': True})
    )

    Age = forms.FloatField(
        required=True,
        min_value=0.1,
        max_value=120.0,
        widget=forms.NumberInput(attrs={
            'class': 'form-input',
            'step': '0.1',
            'placeholder': 'e.g. 29.0',
            'required': True
        })
    )

    Person_Role = forms.ChoiceField(
        required=True,
        choices=[
            ('', '-- Select Role --'),
            ('Normal Passenger', 'Normal Passenger'),
            ('Engineering Crew', 'Engineering Crew'),
            ('Other Crew', 'Other Crew (Deck, Victualling, Restaurant)')
        ],
        widget=forms.Select(attrs={'class': 'form-select', 'required': True, 'id': 'id_Person_Role'})
    )

    Pclass = forms.ChoiceField(
        required=True,
        choices=[
            ('', '-- Select Class / Department --'),
            ('1', '1st Class Passenger'),
            ('2', '2nd Class Passenger'),
            ('3', '3rd Class Passenger'),
            ('Deck Crew', 'Deck Crew (Officers, Sailors)'),
            ('Engineering Crew', 'Engineering Crew (Firemen, Engineers)'),
            ('Victualling Crew', 'Victualling Crew (Stewards, Cooks)'),
            ('Restaurant Staff', 'Restaurant Staff (A la Carte)'),
            ('Band', 'Band / Musician')
        ],
        widget=forms.Select(attrs={'class': 'form-select', 'required': True, 'id': 'id_Pclass'})
    )

    # Optional fields
    SibSp = forms.IntegerField(
        required=False,
        min_value=0,
        max_value=20,
        widget=forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'e.g. 0'})
    )

    Parch = forms.IntegerField(
        required=False,
        min_value=0,
        max_value=20,
        widget=forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'e.g. 0'})
    )

    Fare = forms.FloatField(
        required=False,
        min_value=0.0,
        max_value=1000.0,
        widget=forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01', 'placeholder': 'e.g. 26.00'})
    )

    Embarked = forms.ChoiceField(
        required=False,
        choices=[
            ('', '-- Optional --'),
            ('S', 'Southampton (S)'),
            ('C', 'Cherbourg (C)'),
            ('Q', 'Queenstown (Q)'),
            ('B', 'Belfast (B)')
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    Height_cm = forms.FloatField(
        required=False,
        min_value=30.0,
        max_value=250.0,
        widget=forms.NumberInput(attrs={'class': 'form-input', 'step': '0.1', 'placeholder': 'e.g. 172.0'})
    )

    Weight_kg = forms.FloatField(
        required=False,
        min_value=2.0,
        max_value=250.0,
        widget=forms.NumberInput(attrs={'class': 'form-input', 'step': '0.1', 'placeholder': 'e.g. 70.0'})
    )

    Title = forms.ChoiceField(
        required=False,
        choices=[('', '-- Optional --')] + [
            (t, t) for t in CATEGORIES.get("Title", ["Mr", "Miss", "Mrs", "Master", "Dr", "Rev", "Col", "Major"])
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    raw_home_dests = CATEGORIES.get("Home_Dest", [])
    clean_home_dests = sorted(list(set(h.strip() for h in raw_home_dests if h and h.strip() and h.strip().lower() != 'unknown')))
    home_dest_choices = [('', '-- Optional --')] + [(h, h) for h in clean_home_dests]

    Home_Dest = forms.ChoiceField(
        required=False,
        choices=home_dest_choices,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # Dropdown for Occupation / Job built from the real values in CSV (including Musician)
    raw_occ_list = CATEGORIES.get("Occupation", [])
    # Strip whitespace and deduplicate choices
    clean_occs = sorted(list(set(o.strip() for o in raw_occ_list if o and o.strip())))
    occ_choices = [('', '-- Optional --')]
    if "Musician" in clean_occs:
        occ_choices.append(("Musician", "Musician (Band / Passenger)"))
    for o in clean_occs:
        if o != "Musician":
            occ_choices.append((o, o))

    Occupation = forms.ChoiceField(
        required=False,
        choices=occ_choices,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def clean_Age(self):
        age = self.cleaned_data.get('Age')
        if age is not None and (age < 0.1 or age > 120):
            raise forms.ValidationError("Age must be between 0.1 and 120 years.")
        return age

    def clean_Fare(self):
        fare = self.cleaned_data.get('Fare')
        if fare is not None and fare < 0:
            raise forms.ValidationError("Fare cannot be negative.")
        return fare
