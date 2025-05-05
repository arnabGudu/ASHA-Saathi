from http.server import BaseHTTPRequestHandler, HTTPServer

class RedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(301)
        self.send_header('Location', 'https://asha-saathi.streamlit.app')
        self.end_headers()

server_address = ('', 8085)
httpd = HTTPServer(server_address, RedirectHandler)
print("Redirecting on port 8085...")
httpd.serve_forever()