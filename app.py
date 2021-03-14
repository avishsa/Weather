from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import controller

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parse_url = urlparse(self.path)
        query_components = parse_qs(parse_url.query)
        print(parse_url,query_components)
        if parse_url.path == '/weather/data':
            print('data')
            controller.get_data(self,query_components)
            return
        # if parse_url.path == '/weather/summarize':
        #     print('sum')
        #     self.wfile.write(bytes(controller.get_summerize(query_components)), 'utf-8')
        # if parse_url.path != '/weather/summarize' and parse_url.path!='/weather/data':
        #     print("no support")
        #     self.wfile.write(b"no support")







httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()