from bottle import route
from api.controllers import view_controller

@route('/api/view')
def view_page():
    return view_controller.view_page()