# HalcyonHTTPServer - Advanced HTTP Server
# Version: 1.4.0

import http.server
import socketserver
import os
import logging
import socket
from http_server_config import HOST, PORT, DIRECTORY  # Import configuration

# Ensure the serve folder exists
if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)

# Logging setup
LOG_FILE = "server.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler(LOG_FILE)],
)

# Track server statistics
REQUEST_COUNT = {"GET": 0, "POST": 0}

# Banner for script startup
def get_server_ip():
    """Determine the server's IP address."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except Exception:
        ip = "Unknown"
    return ip


BANNER = f"""
==============================================
           HalcyonHTTPServer v1.4.0
==============================================
 Server Host:    {HOST}
 Server Port:    {PORT}
 Server IP:      {get_server_ip()}
 Directory:      {os.path.abspath(DIRECTORY)}
 Log File:       {LOG_FILE}
==============================================
"""


class HalcyonHTTPHandler(http.server.SimpleHTTPRequestHandler):
    """
    Custom HTTP Request Handler for HalcyonHTTPServer.
    Serves files from the specified directory and logs all requests.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        """Log all requests to the console and server.log."""
        logging.info("%s - - [%s] %s", self.client_address[0], self.log_date_time_string(), format % args)

    def do_GET(self):
        """Handle GET requests and display detailed information."""
        global REQUEST_COUNT
        REQUEST_COUNT["GET"] += 1

        client_ip, client_port = self.client_address
        logging.info(f"GET request received: Path = {self.path}, Client IP = {client_ip}, Port = {client_port}")
        print(f"[GET] Client IP: {client_ip}, Port: {client_port}, Path: {self.path}")
        print(f"Headers: {dict(self.headers)}")
        print(f"Total GET requests handled: {REQUEST_COUNT['GET']}")

        super().do_GET()

    def do_POST(self):
        """Handle POST requests and display detailed information."""
        global REQUEST_COUNT
        REQUEST_COUNT["POST"] += 1

        client_ip, client_port = self.client_address
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode()

        logging.info(f"POST request received: Client IP = {client_ip}, Port = {client_port}, Data = {post_data}")
        print(f"[POST] Client IP: {client_ip}, Port: {client_port}")
        print(f"Headers: {dict(self.headers)}")
        print(f"Content Length: {content_length}")
        print(f"Data: {post_data}")
        print(f"Total POST requests handled: {REQUEST_COUNT['POST']}")

        # Respond with confirmation
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"POST data received and logged.")
        logging.info("POST response sent to client.")


def run_server():
    """
    Starts the HTTP server using the specified handler and configuration.
    """
    print(BANNER)
    logging.info("Starting HalcyonHTTPServer...")
    logging.info(f"Serving files from directory: {os.path.abspath(DIRECTORY)}")
    logging.info(f"Listening on {HOST}:{PORT} (Server IP: {get_server_ip()})")

    with socketserver.TCPServer((HOST, PORT), HalcyonHTTPHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            logging.info("HalcyonHTTPServer stopped by user.")
            print("\nServer stopped.")
        finally:
            logging.info(f"Total GET requests handled: {REQUEST_COUNT['GET']}")
            logging.info(f"Total POST requests handled: {REQUEST_COUNT['POST']}")
            print(f"Summary: Total GET = {REQUEST_COUNT['GET']}, Total POST = {REQUEST_COUNT['POST']}")
            httpd.server_close()
            logging.info("Server shutdown complete.")


if __name__ == "__main__":
    run_server()
