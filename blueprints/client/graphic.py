from flask import Blueprint, render_template
from flask_entities import SessionHandler
from database import DB


b = Blueprint('client_graphic', __name__)

@b.route('/')
@b.route('/summary')
@SessionHandler.take_alerts
@SessionHandler.take_user_id
def index(user_id, alerts):
    wallets = DB.Wallets.select({'user_id': user_id})
    currencies = {}
    for wallet in wallets:
        if wallet.currency not in currencies:
            currencies.update({wallet.currency: {'total_amount': wallet.amount}})
        else:
            currencies[wallet.currency]['total_amount'] += wallet.amount
    return render_template('pages/summary.html', wallets = wallets, currencies = currencies, alerts = alerts)

@b.route('/spends')
def spends():
    return render_template('pages/spends.html')

@b.route('/incomes')
def incomes():
    return render_template('pages/incomes.html')