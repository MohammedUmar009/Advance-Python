import webbrowser
import tempfile
import os

html = """
<!DOCTYPE html>
<html>
<head>
    <title>My Current Location</title>
</head>
<body>
    <h2>Finding your current location...</h2>

    <script>
        navigator.geolocation.getCurrentPosition(
            function(position) {
                let latitude = position.coords.latitude;
                let longitude = position.coords.longitude;

                let mapUrl =
                    "https://www.google.com/maps?q="
                    + latitude + "," + longitude;

                window.location.href = mapUrl;
            },
            function(error) {
                document.body.innerHTML =
                    "<h2>Location permission was denied.</h2>";
            }
        );
    </script>
</body>
</html>
"""

file_path = os.path.join(tempfile.gettempdir(), "current_location.html")

with open(file_path, "w", encoding="utf-8") as file:
    file.write(html)

webbrowser.open("file:///" + file_path.replace("\\", "/"))