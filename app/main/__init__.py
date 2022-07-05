from flask import Blueprint
from flask_breadcrumbs import default_breadcrumb_root

main = Blueprint('main', __name__)
default_breadcrumb_root(main, '.')

from . import views, errors
from ..models import Permissions


@main.app_context_processor
def inject_permissions():
    return dict(Permissions=Permissions)
