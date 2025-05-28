import uuid
import json
import os
from bottle import HTTPResponse
from api.utils.helpers import json_response


# Memoria simulada para almacenar archivos
UPLOAD_FOLDER = 'uploaded_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

files = {}

def list_files():
    print(">>> Listing Files!!")
    return json_response("Lista de archivos", 200, list(files.values()))

def get_file(file_id):
    file = files.get(file_id)
    if not file:
        return json_response("Archivo no encontrado", 404, {})
    return json_response("Archivo encontrado", 200, file)

def create_file(request):
    data = request.json
    print(">>> Received Json!!")
    print(data)
    if not data or 'name' not in data or 'content' not in data:
        return json_response("Faltan campos obligatorios", 400, {})

    file_id = str(uuid.uuid4())
    files[file_id] = {
        "id": file_id,
        "name": data['name'],
        "content": data['content']
    }
    return json_response("Archivo creado", 201, files[file_id])

def update_file(file_id, request):
    data = request.json
    if file_id not in files:
        return json_response("Archivo no encontrado", 404, {})
    
    files[file_id]['name'] = data.get('name', files[file_id]['name'])
    files[file_id]['content'] = data.get('content', files[file_id]['content'])

    return json_response("Archivo actualizado", 200, files[file_id])

def delete_file(file_id):
    if file_id not in files:
        return json_response("Archivo no encontrado", 404, {})
    deleted = files.pop(file_id)
    return json_response("Archivo eliminado", 200, deleted)

def upload_files(request):
    uploaded_files = request.files.getall('files')
    metadata_raw = request.forms.get('metadata', '')

    try:
        metadata = json.loads(metadata_raw) if metadata_raw else {}
    except Exception as e:
        return json_response("Error al parsear metadata JSON", 400, {"error": str(e)})

    if not uploaded_files:
        return json_response("No se recibieron archivos", 400, {})

    results = []

    for file_obj in uploaded_files:
        content = file_obj.file.read().decode('utf-8')  # o binario si prefieres

        file_path = os.path.join(UPLOAD_FOLDER, file_obj.filename)
        file_obj.save(file_path)  # Guarda el archivo en disco

        file_id = str(uuid.uuid4())
        files[file_id] = {
            "id": file_id,
            "name": file_obj.filename,
            "content": content,
            #"meta": metadata.get(file_obj.filename, {})  # por nombre
            "path": file_path,
            "meta": metadata.get(file_obj.filename, {})
        }
        results.append(files[file_id])

    return json_response("Archivos cargados correctamente", 201, results)