from django.conf import settings
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Item
from main.services import create_stripe_session


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

        session = create_stripe_session(price=int(item.price), name=item.name)
        return Response(data={'session_id': session}, status=status.HTTP_200_OK)
