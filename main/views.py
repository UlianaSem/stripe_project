from django.conf import settings
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Item, Order
from main.services import create_stripe_session, create_stripe_tax, create_stripe_discount


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        return Response({'item': self.object, 'public_key': settings.STRIPE_PUBLIC_KEY},
                        template_name='main/item_detail.html')


class BuyCreate(APIView):

    def get(self, request, pk, format=None):
        item = get_object_or_404(Item, pk=pk)

        path = f"{self.request.scheme}://{self.request.META.get('HTTP_HOST')}/"

        session = create_stripe_session(price=int(item.price), name=item.name, currency=item.currency, path=path)
        return Response(data={'session_id': session}, status=status.HTTP_200_OK)


class OrderBuyCreate(APIView):

    def get(self, request, pk, format=None):
        order = get_object_or_404(Order, pk=pk)

        path = f"{self.request.scheme}://{self.request.META.get('HTTP_HOST')}/"
        tax, discount = None, None

        if order.tax:
            tax = create_stripe_tax(order.tax.value)

        if order.discount:
            discount = create_stripe_discount(order.discount.value)

        session = create_stripe_session(
            price=int(order.order_full_price), name=order.pk, tax=tax, discount=discount, path=path
        )
        return Response(data={'session_id': session}, status=status.HTTP_200_OK)


class GetSuccessResponse(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return Response(template_name='main/success.html')


class GetCancelResponse(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return Response(template_name='main/cancel.html')
