from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from api.models import Customer
from api.serializers import CustomerSerializer


class CutomerListCreateView(ListAPIView,CreateAPIView):

    serializer_class=CustomerSerializer
    queryset=Customer.objects.all()

class CustomerRetrieveUpdateDestroyView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):

    serializer_class=CustomerSerializer
    queryset=Customer.objects.all()

