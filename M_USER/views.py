from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from M_USER.decorators import test
from .serializers import UserProfileSerializer, AccountSerializer, TopUpSerializer
from .models import UserProfile, Account, TopUP

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .decorators import superuser_required, justuser_required, specificuser_required


class SignUpView(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class AccountList(APIView):
    def get(self, request, format=None):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator([login_required, test], name='dispatch')
class TopUp(APIView):
    def post(self, request, format=None):
        serializer = TopUpSerializer
        if serializer.is_valid():
            serializer.save()
            topup_acc = serializer.data['topup_account']
            amount = serializer.data['amount']

            try:
                Tp = Account.objects.get(account_number=topup_acc)
                if Tp.balance < amount:
                    return Response("Insufficient Balance!!!", status=status.HTTP_400_BAD_REQUEST)
                else:
                    Tp.balance -= amount
                    Tp.save()
                    return Response("TopUP Succesful!!!", status=status.HTTP_201_CREATED)

            except ObjectDoesNotExist:
                return Response("Test", status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
