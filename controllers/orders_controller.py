from flask import Blueprint, render_template
from models.order_list import orders

orders_blueprint = Blueprint("orders", __name__)



@orders_blueprint.route("/orders")
def index():
    return render_template("index.html", title="My Order List", order_list=orders)

@orders_blueprint.route("/orders/<index>")
def order(index):
    order = orders[int(index)]
    return render_template("order.html", title=order.customer_name, order=order)

