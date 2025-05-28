from api.server import run_service

config = {
    'DEV': {
        'host_ip': '0.0.0.0',
        'host_port': 8081
    }
}

if __name__ == '__main__':
    run_service(config)