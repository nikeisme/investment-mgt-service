from django.core.validators import MinValueValidator
from django.db import models


class Account (models.Model) :

    account_num = models.CharField("계좌번호", max_length=45,unique=True, null=False)
    account_name = models.CharField("계좌명", max_length=30,null=False)
    account_total = models.IntegerField("계좌 총 자산",default=0,null=True)

    class Meta:
        db_table = "accounts"

    def __str__(self):
        return self.account_name


class User(models.Model):

    account = models.OneToOneField(Account,on_delete=models.SET_DEFAULT,related_name="user", default="0")
    user_name = models.CharField("유저이름", max_length=45, null=False, blank=False)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.user_name


class Investment(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="investment")
    brokerage = models.CharField("증권사",max_length=45)
    principal = models.IntegerField("투자 원금", null=True,blank=True)

    class Meta:
        db_table = "investments"



class Stock(models.Model):

    stock_name=models.CharField("종목명",max_length=45,unique=True,null=False,blank=False)
    isin= models.CharField("ISIN", max_length=45, unique=True, null=False, blank=False)
    asset_group = models.CharField("자산그룹", max_length=45)


    class Meta:
        db_table = "stocks"

    def __str__(self):
        return self.stock_name



class UserHolding(models.Model):

    holding = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, related_name="user_holdings", on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField("보유 종목 수량", default=1)
    current_price = models.IntegerField("현재가", null=True, blank=True)

    class Meta:
        db_table = "user_holdings"
