from django.urls import path

from . import views

urlpatterns = [
    path('map/', views.coordinates_squirrel),
    path('sightings/', views.all_squirrels),
    path('sightings/<int:Unique_Squirrel_ID>', views.edit_squirrel),
    path('sightings/add', views.add_squirrel),
]
