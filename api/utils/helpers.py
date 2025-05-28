import json
from bottle import HTTPResponse

def json_response(msg, status, data):
    message = {
        'status': status,
        'message': msg,
        'data': data
    }
    return HTTPResponse(
        body=json.dumps(message),
        status=status,
        headers={'Content-type': 'application/json'}
    )
