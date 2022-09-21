
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User
from api.serializers import InvestmentViewSerializer


class InvestmentView(APIView):

    def get(self, request, pk):
        queryset = User.objects.get(id=pk)
        serializer = InvestmentViewSerializer(queryset)

        return Response(data=serializer.data, status=status.HTTP_200_OK)