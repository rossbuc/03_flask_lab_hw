from flask import Blueprint, render_template
from models.order_list import orders

orders_blueprint = Blueprint("orders", __name__)

order_blueprint = Blueprint("order", __name__)

@orders_blueprint.route("/orders")
def index():
    return render_template("index.html", title="My Order List", order_list=orders)

@order_blueprint.route("/orders/<index>")
def order(index):
    return render_template("order.html", title=orders[int(index)].customer_name, order=orders[int(index)])

