"""Example of how to use the Google OAuth2.0 flow to authenticate a user."""
import http.server
import subprocess
import threading
import platform
import requests
import hashlib
import time
import os

from urllib.parse import parse_qs, urlparse


_CLIENT_ID = "846353858263-726t7egbmpkbl2nv61fb0t8jqk0drjds." \
             "apps.googleusercontent.com"
_CLIENT_SECRET = "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"
TOKEN_URL = "https://oauth2.googleapis.com/token"
REDIRECT_URI = "http://localhost:8000/callback/"

class LoginManager:
    def __init__(self):
        self._server = None
        self._port = 0

    def start_web_server(self):
        """Kick off a thread for the local webserver."""
        th = threading.Thread(target=self._start_local_server)
        th.start()

    def _start_local_server(self):
        self._server = http.server.HTTPServer(("localhost", 8000), Handler)
        self._port = self._server.server_port
        print(f"Serving on port {self._port}")
        self._server.serve_forever()

    def open_browser(self):
        """Opens the browser to the login page."""
        # Waits for the server to start.
        while self._server is None:
            time.sleep(1)
        url = self.create_login_url()
        system = platform.system()
        if system == "Darwin":
            cmd = ["open", url]
        elif system == "Linux":
            cmd = ["xdg-open", url]
        elif system == "Windows":
            cmd = ["cmd", "/c", "start", url.replace("&", "^&")]
        else:
            raise RuntimeError(f"Unsupported system: {system}")
        subprocess.run(cmd, check=True)

    def create_login_url(self) -> str:
        """Generate the login URL."""
        nonce = hashlib.sha256(os.urandom(1024)).hexdigest()
        return (
        "https://accounts.google.com/o/oauth2/v2/auth?"
        "response_type=code&"
        f"client_id={_CLIENT_ID}&"
        "scope=openid%20email&"
        f"redirect_uri={REDIRECT_URI}&"
        f"nonce={nonce}")


class Handler(http.server.SimpleHTTPRequestHandler):
    """Handle the response from accounts.google.com."""

    # Sketchy static variable to hold response.
    info = None

    def do_GET(self):
        """Handle the GET request."""
        global token
        # Parse the query parameters from the callback URL
        query_components = parse_qs(urlparse(self.path).query)
        if "code" in query_components:
            # Exchange the authorization code for an access token
            auth_code = query_components["code"][0]
            payload = {
                "code": auth_code,
                "client_id": _CLIENT_ID,
                "client_secret": _CLIENT_SECRET,
                "redirect_uri": REDIRECT_URI,
                "grant_type": "authorization_code"
            }
            response = requests.post(TOKEN_URL, data=payload)
            if response.status_code == 200:
                token = response.json().get("access_token")
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(
                    b"<html><head><title>Authentication Successful"
                    b"</title></head>")
                self.wfile.write(
                    b"<body><h1>Authentication Successful!</h1></body></html>")
            else:
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"<html><head><title>Error</title></head>")
                self.wfile.write(
                    b"<body><h1>Failed to authenticate</h1></body></html>")
        else:
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<html><head><title>Error</title></head>")
            self.wfile.write(b"<body><h1>Bad Request</h1></body></html>")
