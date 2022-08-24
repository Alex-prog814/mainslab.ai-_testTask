from rest_framework import generics

from applications.bills.models import Bill
from applications.bills.serializers import BillSerializer, BillDocSerializer


class BillDocCreateView(generics.CreateAPIView):
    model = Bill
    serializer_class = BillDocSerializer


class BillCreateView(generics.CreateAPIView):
    model = Bill
    serializer_class = BillSerializer


class BillListView(generics.ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        client_name = self.request.query_params.get('client')
        client_org = self.request.query_params.get('org')

        if client_name is not None and client_org is not None:
            queryset = queryset.filter(client_name=client_name, client_org=client_org)
        elif client_name is not None:
            queryset = queryset.filter(client_name=client_name)
        elif client_org is not None:
            queryset = queryset.filter(client_org=client_org)
        return queryset
