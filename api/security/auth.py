
from bottle import request, response, HTTPResponse, hook

API_KEY = "AAHltRCrq8Yz2o8vWfseuEiQUTJWmbgY9p4"

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'

def require_api_key(func):
    def wrapper(*args, **kwargs):
        key = request.get_header('Authorization')
        if not key or key != f"Bearer {API_KEY}":
            return HTTPResponse(status=403, body='{"error": "Unauthorized"}')
        return func(*args, **kwargs)
    return wrapper
