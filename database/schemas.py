from .utils.connector import Int, Str, Bool, Field as F
from .utils.funcs import SchemaBase


def add_user_related_fields(cls):
    original_fields = cls.fields
    cls.fields = [F('user_id', Int)] + original_fields
    return cls

def add_income_spend_fields(cls):
    original_fields = cls.fields
    cls.fields = original_fields + [F('is_income', Bool, default=False), F('is_spend', Bool, default=False)]
    return cls



class Web:
    class Users(SchemaBase):
        table_name = 'users'
        fields = [
            F('email', Str)
        ]

class Data:
    @add_user_related_fields
    class Wallets(SchemaBase):
        table_name = 'wallets'
        fields = [
            F('name', Str),
            F('amount', Int),
            F('currency', Str)
        ]

    @add_user_related_fields
    class Transfers(SchemaBase):
        table_name = 'transfers'
        fields = [
            F('from_wallet_id', Int),
            F('to_wallet_id', Int),
            F('amount', Int)
        ]

    @add_user_related_fields
    @add_income_spend_fields
    class Categories(SchemaBase):
        table_name = 'categories'
        fields = [
            F('name', Str),
        ]

    @add_user_related_fields
    @add_income_spend_fields
    class Listing(SchemaBase):
        table_name = 'listing'
        fields = [
            F('category_id', Int),
            F('wallet_id', Int),
            F('amount', Int),
            F('time', Int),
            F('comment', Str),
        ]

class DB:
    @staticmethod
    def get_all_schemas():
        return [getattr(DB, attr) for attr in dir(DB) if isinstance(getattr(DB, attr), type) and issubclass(getattr(DB, attr), SchemaBase)]
    
    Users = Web.Users
    Wallets = Data.Wallets
    Tranfers = Data.Transfers
    Categories = Data.Categories
    Listing = Data.Listing

