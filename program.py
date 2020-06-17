from flask import Flask
from flask_injector import FlaskInjector
from injector import singleton
from app.main.services.membership_service import MembershipService


app = Flask(__name__)

from app.main.controllers.membership_controller import blueprint
app.register_blueprint(blueprint)


def configure_dependencies(binder):
    binder.bind(MembershipService, to=MembershipService, scope=singleton)


FlaskInjector(app=app, modules=[configure_dependencies])


@app.route('/')
def hello_world():
    return 'Hello World!'