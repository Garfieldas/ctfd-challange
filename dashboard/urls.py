from django.urls import path
from . import views

urlpatterns = [
    path("", views.taxes, name="taxes"),
    path("<int:pk>/", views.dashboard, name="dashboard"),
]
