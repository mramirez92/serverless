from http.server import BaseHTTPRequestHandler
from datetime import datetime


# declare subclass called handler that extends BaseHTTPRequestHandler
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        #this is what is going to show up on screen
        self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
        return
