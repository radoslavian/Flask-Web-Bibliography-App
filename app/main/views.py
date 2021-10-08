'''Main view functions for the application.
'''

from . import main
from flask import render_template

@main.route('/', methods=['GET', 'POST'])
def index():
    # url_for('main.index') # main - przestrzeń nazw
    # url_for('.index') # przestrzeń n. akt. żądania
    return render_template('base.html')
