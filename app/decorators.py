'''Custom decorators for the application's view functions.

Based on: M. Grinberg, Flask...
'''

# not yet tested with view functions

from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permissions


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    permission_required(Permissions.ADMIN)(f)
