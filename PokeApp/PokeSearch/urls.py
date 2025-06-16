from . import views
from django.urls import path


urlpatterns = [
    path('',views.PokeSearch,name='poke-search')
]





