from flask import Blueprint, render_template
from models.transaction_list import transactions

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route('/transactions')
def index():
    return render_template("transactions.html", title="List of Transactions", transaction_list=transactions)