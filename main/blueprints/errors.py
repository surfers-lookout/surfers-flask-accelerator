from flask import render_template
from . import bp

@bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error_description=e.description)

@bp.app_errorhandler(500)
def page_not_found(e):
    return render_template('500.html', error_description=e.description)
