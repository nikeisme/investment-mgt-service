import jwt
import bcrypt
from django.db import transaction
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User, Investment, UserHolding, DepositInfo, Account
from api.serializers import InvestmentViewSerializer, InvestmentDetailViewSerializer, UserHoldingViewSerializer, \
    DepositInfoSerializer, AssetSerializer
from backend_core.settings.common import SECRET_KEY


class InvestmentView(APIView):
    """
    투자 화면 View
    """

    def get(self, request, pk):
        queryset = User.objects.get(id=pk)
        serializer = InvestmentViewSerializer(queryset)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class InvestmentDetailView(APIView):

    """
    투자 상세 화면 View
    """

    def get(self, request, pk):
        queryset = Investment.objects.get(id=pk)
        serializer = InvestmentDetailViewSerializer(queryset)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



class UserHoldingView(APIView):

    """보유 종목 화면 View"""

    def get(self, request, pk):
        queryset = UserHolding.objects.filter(user=User.objects.get(id=pk))
        serializer = UserHoldingViewSerializer(queryset,many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class InvestmentDeposit(APIView):
    """입금 거래 화면 View"""

    def post(self, request):
        payload = {**request.data}
        signature = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        serializer = DepositInfoSerializer(data={**payload,"signature": signature})

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

    def put(self, request):
        depositinfo = DepositInfo.objects.get(id=request.data.get("transfer_identifier"))
        serializer = AssetSerializer(depositinfo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)