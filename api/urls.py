from django.urls import path

from api import views

urlpatterns = [
    path("investments/<int:pk>/", views.InvestmentView.as_view(), name="investment"),
    path("investments/detail/<int:pk>/",views.InvestmentDetailView.as_view(),name="investment-detail"),
    path("users/holdings/<int:pk>/", views.UserHoldingView.as_view(),name="user-holdings"),
]
