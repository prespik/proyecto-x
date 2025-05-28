from bottle import run, WSGIRefServer
from api.routes import api_routes
from api.routes import file_routes
from api.routes import view_routes
from api.security.auth import enable_cors
import threading

class QuietWSGIRefServer(WSGIRefServer):
    quiet = True

def start_server(config):
    run(host=config['DEV']['host_ip'], port=config['DEV']['host_port'], debug=False, server=QuietWSGIRefServer)

def run_service(config):
    print(">>> Api Service Started")
    server_thread = threading.Thread(target=start_server, args=(config,))
    server_thread.daemon = True
    server_thread.start()
