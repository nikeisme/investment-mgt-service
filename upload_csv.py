import os
import django
from django.core.exceptions import ValidationError

import csv

from django.db import transaction

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend_core.settings.local")
django.setup()

from api.models import Stock, Account, User, Investment, UserHolding


CSV_ACCOUNT_ASSET = "./csv/account_asset_info_set.csv"
CSV_ACCOUNT_BASIC = "./csv/account_basic_info_set.csv"
CSV_ASSET_GROUP = "./csv/asset_group_info_set.csv"


def upload_asset_group_info(csv_asset_group):

    with open(csv_asset_group) as in_file:
        data_reader = csv.reader(in_file)
        result = {
            "total_csv_rows": 0,
            "success_rows": 0,
            "failed_rows": 0,
            "invalid_rows": [],
        }
        for idx, row in enumerate(data_reader):

            if idx == 0:
                continue

            try:
                stock_name, ISIN, asset_group_name = row[0], row[1], row[2]

                if not (stock_name and ISIN and asset_group_name):
                    raise KeyError("row 데이터가 충분치 않습니다.")

                if Stock.objects.filter(stock_name=stock_name):
                    raise ValidationError("중복된 종목명이 존재합니다.")

                if Stock.objects.filter(isin=ISIN):
                    raise ValidationError("중복된 ISIN이 존재합니다.")

                Stock.objects.create(
                    stock_name=stock_name, isin=ISIN, asset_group=asset_group_name
                )
                result["success_rows"] += 1

            except Exception as e:

                result["failed_rows"] += 1
                result["invalid_rows"].append(
                    {"error row": idx + 1, "error detail": str(e)}
                )
                continue

            result["total_csv_rows"] += 1

        return result


def upload_asset_info(csv_asset_info):

    with open(csv_asset_info) as in_file:
        data_reader = csv.reader(in_file)
        result = {
            "total_csv_rows": 0,
            "success_rows": 0,
            "failed_rows": 0,
            "invalid_rows": [],
        }
        for idx, row in enumerate(data_reader):

            if idx == 0:
                continue

            try:
                (
                    user_name,
                    brokerage,
                    account_num,
                    account_name,
                    ISIN,
                    current_price,
                    holding_quantity,
                ) = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])

                if not (
                    user_name
                    and brokerage
                    and account_num
                    and account_name
                    and current_price
                    and holding_quantity
                ):
                    raise ValidationError("row 데이터가 충분치 않습니다.")

                stock = Stock.objects.get(isin=ISIN)
                stock.current_price = current_price
                stock.save()

                account = Account.objects.get_or_create(
                    account_name=account_name,
                    account_num=account_num,
                )[0]

                user = User.objects.get_or_create(account=account, user_name=user_name)[0]
                investment = Investment.objects.get_or_create(
                    user=user, brokerage=brokerage
                )[0]

                user_holding = UserHolding.objects.get_or_create(
                    holding=stock, user=user
                )[0]
                user_holding.quantity = holding_quantity
                user_holding.current_price = current_price
                user_holding.save()

                result["success_rows"] += 1

            except Exception as e:
                result["failed_rows"] += 1
                result["invalid_rows"].append(
                    {"error row": idx + 1, "error detail": str(e)}
                )
                continue

            result["total_csv_rows"] += 1

        return result


def upload_asset_basic(csv_asset_basic):

    with open(csv_asset_basic) as in_file:
        data_reader = csv.reader(in_file)
        result = {
            "total_csv_rows": 0,
            "success_rows": 0,
            "failed_rows": 0,
            "invalid_rows": [],
        }

        for idx, row in enumerate(data_reader):
            # 헤더는 건너뜀
            if idx == 0:
                continue

            try:
                account_num, principal = row[0], row[1]
                if not (account_num and principal):
                    raise ValidationError("row 데이터가 충분치 않습니다.")

                account = Account.objects.get(account_num=account_num)
                investment = account.user.investment
                investment.principal = principal
                investment.save()

                result["success_rows"] += 1

            except Exception as e:
                result["failed_rows"] += 1
                result["invalid_rows"].append(
                    {"error row": idx + 1, "error detail": str(e)}
                )
                continue

            result["total_csv_rows"] += 1
        return result


@transaction.atomic
def calculate_account_total():
    try:
        users = User.objects.all()
        for user in users:
            user_account = user.account
            user_account.account_total = 0

            for user_holding in user.user_holdings.all():
                user_account.account_total += (
                    user_holding.current_price * user_holding.quantity
                )

            user_account.save()

    except Exception as e:
        transaction.set_rollback(rollback=True)
        raise ValidationError(str(e))


if __name__ == "__main__":
    upload_asset_group_info(CSV_ASSET_GROUP)
    upload_asset_info(CSV_ACCOUNT_ASSET)
    upload_asset_basic(CSV_ACCOUNT_BASIC)
    calculate_account_total()
