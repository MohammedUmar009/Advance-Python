import webbrowser
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8000

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Current Location</title>
</head>

<body>
    <h2>Getting your current location...</h2>

    <script>
        if (navigator.geolocation) {

            navigator.geolocation.getCurrentPosition(
                function(position) {

                    let latitude = position.coords.latitude;
                    let longitude = position.coords.longitude;

                    // Open Google Maps at current location
                    let mapURL =
                        "https://www.google.com/maps?q="
                        + latitude + "," + longitude;

                    window.location.href = mapURL;
                },

                function(error) {
                    document.body.innerHTML =
                        "<h2>Location permission denied.</h2>" +
                        "<p>Please allow location access in Chrome.</p>";
                }
            );

        } else {
            document.body.innerHTML =
                "<h2>Geolocation is not supported.</h2>";
        }
    </script>
</body>
</html>
"""


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):
        pass


server = HTTPServer(("localhost", PORT), MyHandler)

# Open Chrome/browser
threading.Timer(
    1,
    lambda: webbrowser.open("http://localhost:8000")
).start()

print("Opening Chrome...")
print("Allow location permission when Chrome asks.")

server.serve_forever()py "python 14.py"