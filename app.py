from flask import Flask
from controllers.orders_controller import orders_blueprint
from controllers.transactions_controller import transactions_blueprint

app = Flask(__name__)
app.register_blueprint(orders_blueprint)
app.register_blueprint(transactions_blueprint)

@app.route('/')
def index():
    return "<h1>Hello There</h1>"