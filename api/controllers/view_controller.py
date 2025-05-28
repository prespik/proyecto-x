import os
from bottle import static_file

def view_page():
    file_path = os.path.join(os.path.dirname(__file__), '../views/index.html')
    return static_file('index.html', root=os.path.abspath(os.path.join(os.path.dirname(__file__), '../views/')))