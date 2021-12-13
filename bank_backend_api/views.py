from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import UserstoreSerializer, CustomerSerializer, CustomerStatusSerialzer, AccountSeralizer
from bank_app.models import Customer, CustomerStatus, Account, UserStore
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = UserStore.objects.all()
    serializer_class = UserstoreSerializer


@api_view(['GET'])
def userdetails(request):
    user = User.objects.get(username=request.user)
    obj = UserStore.objects.get(username=user)
    serializer = UserstoreSerializer(obj)
    return Response(serializer.data)

@api_view(['GET'])
def success_login(request):
    return Response({"login": "success"})


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer



class CustomerDetail(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSeralizer


# this detail part will be dealt in ui
# class AccountDetail(generics.RetrieveUpdateAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSeralizer

@api_view(['GET', 'POST'])
def del_customer(request):
    obj = CustomerStatus.objects.get(customer_id=request.customer_id)
    obj.status = "deletion initited successfully"
    obj.save()
    return "success"


@api_view(['GET', 'POST'])
def update_customer(request):
    obj = CustomerStatus.objects.get(customer_id=request.customer_id)
    obj.satus = "update initiated"
    obj.save()
    return "success"


@api_view(['GET', 'POST'])
def create_customer(request):
    obj = CustomerStatus.objects.create(customer_id=request.customer_id, customer_ssn_id=request.customer_ssn_id, status="creation initiated")
    obj.save()
    return "success"


class CustomerStatusList(generics.ListAPIView):
    queryset = CustomerStatus.objects.all()
    serializer_class = CustomerStatusSerialzer