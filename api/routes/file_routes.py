from bottle import route, request
from api.security.auth import require_api_key
from api.controllers import file_controller

@route('/api/files', method='GET')
@require_api_key
def list_files():
    return file_controller.list_files()

@route('/api/files/<file_id>', method='GET')
@require_api_key
def get_file(file_id):
    return file_controller.get_file(file_id)

@route('/api/files', method='POST')
@require_api_key
def create_file():
    return file_controller.create_file(request)

@route('/api/files/<file_id>', method='PUT')
@require_api_key
def update_file(file_id):
    return file_controller.update_file(file_id, request)

@route('/api/files/<file_id>', method='DELETE')
@require_api_key
def delete_file(file_id):
    return file_controller.delete_file(file_id)

@route('/api/files/upload', method='POST')
@require_api_key
def upload_files():
    return file_controller.upload_files(request)