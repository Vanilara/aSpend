from database import DB
from flask_entities import ParamsHandler, SessionHandler, Alerts
from flask import Blueprint, session, redirect


b = Blueprint('client_modals', __name__)


@b.post('/add_wallet')
@SessionHandler.take_user_id
@ParamsHandler.take_form_params(['name', 'amount', 'currency'])
def add_wallet(user_id, name, amount, currency):
    if DB.Wallets.select({'user_id': user_id, 'name': name}) != []:
        alerts = Alerts(error = f'У вас уже есть кошелёк с именем {name}')
    else:
        DB.Wallets.insert({'user_id': user_id, 'name': name, 'amount': amount, 'currency': currency})
        alerts = Alerts(success = f'Кошелёк {name} создан')
    session['alerts'] = alerts
    return redirect('/summary')
    

@b.post('/insert_listing')
def insert_listing():
    pass

@b.post('/add_category')
def add_category():
    pass

@b.post('/add_transfer')
def add_transfer():
    pass




