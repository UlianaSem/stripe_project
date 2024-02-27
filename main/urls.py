from django.urls import path

from main.apps import MainConfig
from main.views import ItemDetailView, BuyCreate, OrderBuyCreate, \
    GetSuccessResponse, GetCancelResponse

app_name = MainConfig.name

urlpatterns = [
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item'),
    path('buy/<int:pk>/', BuyCreate.as_view(), name='buy'),
    path('buy_order/<int:pk>/', OrderBuyCreate.as_view(), name='buy-order'),
    path('success/', GetSuccessResponse.as_view(), name='success'),
    path('cancel/', GetCancelResponse.as_view(), name='cancel'),
]
