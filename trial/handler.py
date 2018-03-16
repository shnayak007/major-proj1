import http.server as server
import fb_trial as fb

# Handler class to process te request
class Myhandler(server.SimpleHTTPRequestHandler):
    def do_GET(self):
      data = self.headers.get("path")
      fb.loadData(data)
