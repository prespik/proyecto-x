from api.utils.helpers import json_response

def api(request):
    action = request.query.action
    comm = request.query.comm
    baud = request.query.baud

    if action == "c":
        return json_response("Test Action C", 200, {})
    elif action == "r":
        return json_response("Test Action R", 300, {'id': 2001, 'value': 'Error'})
    else:
        return json_response("Acción inválida", 400, {})