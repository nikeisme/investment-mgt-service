
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User, Investment
from api.serializers import InvestmentViewSerializer, InvestmentDetailViewSerializer


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
    투자 상세 화면
    """

    def get(self, request, pk):
        queryset = Investment.objects.get(id=pk)
        serializer = InvestmentDetailViewSerializer(queryset)
        return Response(data=serializer.data, status=status.HTTP_200_OK)