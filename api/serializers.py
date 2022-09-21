from rest_framework import serializers

from api.models import User

class InvestmentViewSerializer(serializers.ModelSerializer):
    """
    데이터 조회 - 투자화면
     """

 class InvestmentDetailViewSerializer(serializers.ModelSerializer):
     """
    데이터 조회 - 투자상세화면
     """

 class InvestmentDetailViewSerializer(serializers.ModelSerializer):
     """
    데이터 조회 - 보유종목화면 API
    """