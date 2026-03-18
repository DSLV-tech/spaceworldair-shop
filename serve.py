import os, sys
os.chdir('/Users/cristiandisalvo/Desktop/spaceworldair-shop')
sys.argv = ['server']
import http.server, socketserver
PORT = 7720
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
