from django.urls import path

from main.apps import MainConfig
from main.views import ItemDetailView, BuyCreate

app_name = MainConfig.name

urlpatterns = [
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item'),
    path('buy/<int:pk>/', BuyCreate.as_view(), name='buy'),
]
