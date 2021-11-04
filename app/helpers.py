'''Helper functions for the app.
'''

from app.models import ResponsibilityName
from flask import request, current_app

def get_responsibility_identifiers(responsibility_id=None):
    '''Returns tuple with responsibility id and name or redirects to 404 page
    if no responsibility found with a given responsibility_id.
    '''
    if responsibility_id is None: return None, None
    responsibility = ResponsibilityName.query.filter_by(
            id=responsibility_id).first_or_404()

    return responsibility_id, responsibility.responsibility_name
    

def paginate(query, per_page=0, start_page=0):
    '''Returns default query pagination for view functions.
    '''
    _start_page = start_page or request.args.get('page', 1, type=int)

    return query.paginate(
        _start_page,
        per_page=per_page or current_app.config['LIST_ENTRIES_PER_PAGE'],
        error_out=True)
