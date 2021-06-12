from http.server import BaseHTTPRequestHandler
import pathlib
class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    print(pathlib.Path().absolute())
    self.send_response(200)
    self.send_header('Content-type', 'image/jpeg')
    self.end_headers()
    with open("./api/sample.jpg","rb") as f:
        self.wfile.write(f.read())