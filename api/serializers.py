from rest_framework import serializers

from api.models import User

class InvestmentViewSerializer(serializers.ModelSerializer):

    account_name = serializers.ReadOnlyField(source="account.account_name")
    account_number = serializers.ReadOnlyField(source="account.account_num")
    account_total= serializers.ReadOnlyField(source="account.account_toal")
    brokerage = serializers.ReadOnlyField(source="investment.brokerage")

    class Meta:
        model = User
        fields = [
            "user_name",
            "account_name",
            "account_number",
            "brokerage",
            "account_total",
            "investment",
        ]

 # class InvestmentDetailViewSerializer(serializers.ModelSerializer):
 #     """
 #    데이터 조회 - 투자상세화면
 #     """
 #
 # class InvestmentDetailViewSerializer(serializers.ModelSerializer):
 #     """
 #    데이터 조회 - 보유종목화면 API
 #    """