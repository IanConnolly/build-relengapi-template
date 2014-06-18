from flask import (
    Blueprint,
    render_template
)
from flask.ext.login import (
    login_required
)
from relengapi import (
    p  # permissions object
)

bp = Blueprint('example', __name__, template_folder='templates',
               static_folder='static')
bp.root_widget_template('example-root-widget.html')

p.example.view.perm_example.doc('Example permission for example app')


@bp.route('/')
def root():
    return render_template('example-index.html')


@bp.route('/needlogin')
@login_required
def need_login():
    return "If you're seeing this then you're logged in!", 200


# You'll need to check the README to see how to set up the permissions for
# this route.
@bp.route('/needpermission')
@p.example.view.perm_example.require()
def need_permission():
    return "If you're seeing this then you set up task permissions right!", 200
