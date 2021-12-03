'''Custom decorators for the application's view functions.
'''

# not yet tested with view functions

from functools import wraps
from flask import abort
from flask_login import current_user
from app.models import Permissions


def permission_required(permission):
    '''Checks whether the user has permission to run a view function.
    Based on: M. Grinberg...
    '''
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
