from . import views
from django.urls import path


urlpatterns = [
    path('poke-search/',views.PokeSearch,name='poke-search'),
    path('poke-view/',views.PokeView,name='poke-view')

]





