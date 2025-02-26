from django.urls import path
from .views import crud_classroom, classroom_delete



urlpatterns = [
    path("classroom/delete/<int:id>/", classroom_delete, name="classroom_delete" ),
    path("", crud_classroom, name="crud_classroom")
]