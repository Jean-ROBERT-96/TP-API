from http.server import HTTPServer, SimpleHTTPRequestHandler

from context.db_context import DBContext

i = DBContext()

if __name__ == "__main__":
    server_adress = ("127.0.0.1", 8000)
    httpd = HTTPServer(server_adress, SimpleHTTPRequestHandler)
    print(f"Served on http://localhost:8000")
    httpd.serve_forever()