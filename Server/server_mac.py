import http.server
import socketserver
import webbrowser
import os
import re
import simple_doctor as sd
import level_generator as lg

# configuration
PREFIX = "[Sketcher-WEB]"
PORT = 8000
WEB_DIRECTORY = "../WebApp"
READER_DIRECTORY = "tmp/"
LEVEL_PATH = "../Client/ScienceBirds.app/Contents/Resources/Data/StreamingAssets/Levels/level-4.xml"

# handler
class reader_handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIRECTORY, **kwargs)

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")

    def do_PUT(self):
        if not os.path.exists(READER_DIRECTORY):
            os.makedirs(READER_DIRECTORY)
        
        file_length = int(self.headers['Content-Length'])
        filename = "temp.png"

        with open(READER_DIRECTORY+filename, 'wb') as output_file:
            output_file.write(self.rfile.read(file_length))
        
        lg.generate(LEVEL_PATH)
        print("output!")
        
        self._set_headers()
        self.wfile.write(self._html("PUT!"))

    def do_POST(self):
        if not os.path.exists(READER_DIRECTORY):
            os.makedirs(READER_DIRECTORY)
        file_length = int(self.headers['Content-Length'])
        data = self.rfile.read(file_length).decode("utf-8")
        predict = re.findall(r"result\=([a-z]*)\%0D", data)
        predict = "none" if len(predict) == 0 else predict[0]
        predict = sd.generate_sentences(sd.get_type(predict), predict)
        
        with open("../WebApp/predict.html", 'w') as a:
            a.write(predict)
        
        self._set_headers()
        self.wfile.write(self._html("Post!"))
        del predict


# start server
httpd = http.server.HTTPServer(('', PORT), reader_handler)
print(PREFIX, "Serving at port:", PORT)
webbrowser.open("http://localhost:"+str(PORT))
httpd.serve_forever()