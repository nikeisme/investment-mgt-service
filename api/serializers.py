from rest_framework import serializers

from api.models import User, Investment, UserHolding, DepositInfo


class InvestmentViewSerializer(serializers.ModelSerializer):

    """ 데이터 조회 - 투자 화면 """

    account_name = serializers.ReadOnlyField(source="account.account_name")
    account_number = serializers.ReadOnlyField(source="account.account_num")
    account_total= serializers.ReadOnlyField(source="account.account_total")
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

class InvestmentDetailViewSerializer(serializers.ModelSerializer):

    """ 데이터 조회 - 투자  상세 화면 """

    account_name = serializers.ReadOnlyField(source="user.account.account_name")
    account_number = serializers.ReadOnlyField(source="user.account.account_num")
    account_total= serializers.ReadOnlyField(source="user.account.account_total")
    investment_income_total = serializers.SerializerMethodField()
    investment_income_rate = serializers.SerializerMethodField()


    class Meta:
        model = Investment
        fields = [
        "account_name",
        "brokerage",
        "account_number",
        "account_total",
        "principal",
        "investment_income_total",
        "investment_income_rate",
        "user",
    ]

    def get_investment_income_total(self, obj):
        return obj.user.account.account_total - obj.principal

    def get_investment_income_rate(self, obj):
        return (obj.user.account.account_total - obj.principal) / (obj.principal * 100)


class UserHoldingViewSerializer(serializers.ModelSerializer):
    """데이터 조회 - 보유 종목 화면 API """

    holding_name = serializers.ReadOnlyField(source="holding.stock_name")
    asset_group = serializers.ReadOnlyField(source="holding.asset_group")
    isin = serializers.ReadOnlyField(source="holding.isin")
    appraisal_amount = serializers.SerializerMethodField()

    class Meta:
        model = UserHolding
        fields = ["holding_name", "asset_group", "appraisal_amount","isin"]

    def get_appraisal_amount(self, obj):
        return obj.quantity * obj.current_price


class DepositInfoSerializer(serializers.ModelSerializer):

    """ 입금 거래 정보 """

    transfer_identifier = serializers.IntegerField(source="id", read_only=True)


    class Meta:
        model = DepositInfo

        fields = [
            "account_num",
            "user_name",
            "transfer_amount",
            "transfer_identifier",
        ]

        extra_kwargs = {

            "account_num": {"write_only": True},
            "user_name": {"write_only": True},
            "transfer_amount": {"write_only": True},

        }

        """ extra_kwargs : write_only 특성을 적용 """

