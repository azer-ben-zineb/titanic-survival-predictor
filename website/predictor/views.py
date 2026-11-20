import os
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import PredictorForm
from .ml_service import MLService
from .matching import match_passenger
from .messages_i18n import (
    MESSAGES,
    get_passenger_tier_sentence,
    get_crew_sentence,
    get_musician_sentence
)

def get_current_lang(request) -> str:
    return request.session.get('lang', 'en')

def set_language_view(request):
    new_lang = request.GET.get('lang', 'en')
    if new_lang in ['en', 'fr']:
        request.session['lang'] = new_lang
    next_url = request.META.get('HTTP_REFERER', '/')
    return redirect(next_url)

@require_http_methods(["GET", "POST"])
def predict_view(request):
    lang = get_current_lang(request)
    i18n = MESSAGES[lang]
    
    if request.method == "POST":
        form = PredictorForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            
            # 1. Run ML inference
            ml_svc = MLService.get_instance()
            ml_result = ml_svc.predict(cleaned_data)
            
            p_pct = ml_result["survival_percentage"]
            person_role = cleaned_data.get("Person_Role", "Normal Passenger")
            occupation = cleaned_data.get("Occupation", "")
            pclass = cleaned_data.get("Pclass", "")
            
            # 2. Check for Musician Easter Egg
            is_musician = (occupation == "Musician" or pclass == "Band")
            
            # 3. Determine hard-coded outcome sentence
            if person_role in ["Engineering Crew", "Other Crew"]:
                outcome_sentence = get_crew_sentence(p_pct, lang=lang)
            else:
                outcome_sentence = get_passenger_tier_sentence(p_pct, lang=lang)
                
            # 4. Historical Match
            match_result = match_passenger(cleaned_data, lang=lang)
            
            context = {
                "i18n": i18n,
                "current_lang": lang,
                "cleaned_data": cleaned_data,
                "ml_result": ml_result,
                "outcome_sentence": outcome_sentence,
                "match_result": match_result,
                "is_musician": is_musician,
                "musician_sentence": get_musician_sentence(lang=lang)
            }
            
            # If Musician is triggered, show dedicated Easter Egg view
            if is_musician:
                # Check if optional audio exists
                audio_path = os.path.join(os.path.dirname(__file__), "static", "audio", "titanic_band.mp3")
                context["has_audio"] = os.path.exists(audio_path)
                return render(request, "predictor/easter_egg.html", context)
                
            return render(request, "predictor/result.html", context)
    else:
        # Prepopulate with reasonable defaults or blank
        form = PredictorForm()

    return render(request, "predictor/index.html", {
        "form": form,
        "i18n": i18n,
        "current_lang": lang
    })

def how_it_works_view(request):
    lang = get_current_lang(request)
    i18n = MESSAGES[lang]
    return render(request, "predictor/how_it_works.html", {
        "i18n": i18n,
        "current_lang": lang
    })
