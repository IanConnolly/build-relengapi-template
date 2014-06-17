from flask import (
    Blueprint,
    render_template
)
# from relengapi import p, db...

bp = Blueprint('example', __name__, template_folder='templates',
               static_folder='static')
bp.root_widget_template('example-root-widget.html')


@bp.route('/')
def root():
    return render_template('example-index.html')
