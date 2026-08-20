from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            with open("index.html", "rb") as f:
                data = f.read()

            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

    def do_POST(self):
        if self.path == "/login":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode()

            print("\n[TEST LOGIN RECEIVED]")
            print(body)

            response = b"Login submitted - forensic test completed."
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)

server = HTTPServer(("127.0.0.1", 8080), Handler)

print("Test server running at http://127.0.0.1:8080")
server.serve_forever()
