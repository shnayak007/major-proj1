from handler import Myhandler
import socketserver

PORT = 4000

with socketserver.TCPServer(("127.0.0.1", PORT), Myhandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


