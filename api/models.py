from django.core.validators import MinValueValidator
from django.db import models


class Account (models.Model) :
    """계좌 정보 모델 """

    account_num = models.CharField("계좌번호", max_length=45,unique=True, null=False)
    account_name = models.CharField("계좌명", max_length=30,null=False)
    account_total = models.IntegerField("계좌 총 자산",default=0,null=True)

    class Meta:
        db_table = "accounts"

    def __str__(self):
        return self.account_name


class User(models.Model):
    """고객 정보 모델 """

    account = models.OneToOneField(Account,on_delete=models.SET_DEFAULT,related_name="user", default="0")
    user_name = models.CharField("고객 이름", max_length=45, null=False, blank=False)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.user_name


class Investment(models.Model):
    """고객 투자 정보 모델 """

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="investment")
    brokerage = models.CharField("증권사",max_length=45)
    principal = models.PositiveIntegerField("투자 원금", null=True,blank=True)

    class Meta:
        db_table = "investments"



class Stock(models.Model):
    """종목 정보 모델 """

    stock_name=models.CharField("종목명",max_length=45,unique=True,null=False,blank=False)
    isin= models.CharField("ISIN", max_length=45, unique=True, null=False, blank=False)
    asset_group = models.CharField("자산그룹", max_length=45)


    class Meta:
        db_table = "stocks"

    def __str__(self):
        return self.stock_name



class UserHolding(models.Model):
    """고객 보유 종목 정보 모델 """

    holding = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, related_name="user_holdings", on_delete=models.SET_NULL,null=True)
    quantity = models.PositiveIntegerField("보유 종목 수량", default=0)
    current_price = models.PositiveIntegerField("현재가", null=True, blank=True)

    class Meta:
        db_table = "user_holdings"

class DepositInfo(models.Model):
    """입금 거래 정보 모델 """

    user_name = models.CharField("고객명",max_length=45,null=False,blank=True)
    account_num = models.CharField("계좌번호",max_length=30,null=False,blank=True)
    transfer_amount = models.PositiveIntegerField("거래금액", null=False, blank=True)
    signature = models.CharField(max_length=300)
    status = models.BooleanField(default=False)


    class Meta:
        db_table = "deposit_logs"
