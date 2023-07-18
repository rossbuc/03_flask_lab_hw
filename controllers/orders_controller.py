from flask import Blueprint, render_template
from models.order_list import orders

orders_blueprint = Blueprint("orders", __name__)

@orders_blueprint.route("/orders")
def index():
    return render_template("index.html", title="My Order List", order_list=orders)

@orders_blueprint.route("/orders/<index>")
def get_order(index):
    return f"{orders[int(index)].topping}" "<h1>This is the order youre looking for</h1>"