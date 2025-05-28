from bottle import route, request
from api.security.auth import require_api_key
from api.controllers import api_controller

@route('/')
def default():
    pass

@route('/api')
@require_api_key
def api():
    return api_controller.api(request)
