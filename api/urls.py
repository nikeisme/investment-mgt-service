from django.urls import path

from api import views

urlpatterns = [
    path("investments/<int:pk>/", views.InvestmentView.as_view(), name="investment"),
]
