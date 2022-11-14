from flask import render_template, request, redirect, abort
from flask import current_app as app
from . import bp
from main.data.utilities import DataManager 


"""
Default page shpwing color
"""
@bp.route('/', methods=["GET"])
def home():
    app.logger.info("Accessing home page")
    _color = app.config['COLOR']
    return render_template('home.html', color=_color)


"""
Heath status check routine
"""
@bp.route('/healthz', methods=["GET"])
def health():
    app.logger.info("Getting service health status")
    if DataManager.testdb():
        _database = 'ok'
    else:
        _database= 'fail'


    _status = {
        "health": "ok",
        "environment": app.config['ENV'],
        "database": _database
    }
    return _status


## Jinja Functions 
@bp.context_processor
def utilities():
    def color_code(color):
        match color:
            case 'red':
                _code = '#FF0000'
            case 'blue':
                _code = '#0000FF'
            case 'green':
                _code = '#00FF00'
            case 'yellow':
                _code = '#FFFF00'
            case _:
                _code = '#800080'

        return _code

    return dict(color_code=color_code)
