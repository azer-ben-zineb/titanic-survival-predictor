from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_view, name='predict'),
    path('how-it-works/', views.how_it_works_view, name='how_it_works'),
    path('set-language/', views.set_language_view, name='set_language'),
]
