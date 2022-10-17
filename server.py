import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from repository import all, create, delete, retrieve, update


class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    def get_all_or_single(self, resource, id):
        if id is not None:
            response = retrieve(resource, id)

            if response is not None:
                self._set_headers(200)
            else:
                self._set_headers(404)
                response = ''
            
        else:
            self._set_headers(200)
            response = all(resource)

        return response

    def do_GET(self):
        response = None
        (resource, id) = self.parse_url(self.path)
        response = self.get_all_or_single(resource, id)
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server """

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body) #converts string to a dictionary

        response = None
        (resource, id) = self.parse_url(self.path)
        if resource == "styles" or "sizes" or "metals":
            self._set_headers(405)
        else:
            self._set_headers(201)
            response = create(resource, post_body)
        self.wfile.write(json.dumps(response).encode())
    
    def do_DELETE(self):
        """Handles DELETE requests to the server"""
        
        (resource, id) = self.parse_url(self.path)
        if resource == "styles" or "sizes" or "metals" or "orders":
            self._set_headers(405)
        else:
            self._set_headers(204)
            delete(resource, id)
        self.wfile.write("").encode()

    def do_PUT(self):
        """Handles PUT requests to the server """
        
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        (resource, id) = self.parse_url(self.path)

        if resource == "styles" or "sizes" or "orders":
            self._set_headers(405)
        else:
            self._set_headers(204)
            update(resource, id, post_body)
        self.wfile.write("").encode()

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()
    
    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple

# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
