#!/usr/bin/env python3
"""
Simple HTTP server for NGØM World Clock

This script starts a local web server to serve the NGØM World Clock application.
It's useful for testing and development before uploading to a web host.

Usage:
    python3 server.py              # Start server on default port 8000
    python3 server.py 9000         # Start server on port 9000
    python3 server.py --help       # Show help message

Then open your browser to:
    http://localhost:8000
    (or http://localhost:<port> if you specified a different port)

Press Ctrl+C to stop the server.

No external dependencies required - uses Python standard library only.
"""

import http.server
import socketserver
import sys
import os
from pathlib import Path

DEFAULT_PORT = 8000
HOST = 'localhost'


def main():
    # Parse command line arguments
    port = DEFAULT_PORT

    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '--help']:
            print(__doc__)
            sys.exit(0)
        try:
            port = int(sys.argv[1])
            if port < 1 or port > 65535:
                raise ValueError("Port must be between 1 and 65535")
        except ValueError as e:
            print(f"Error: Invalid port number. {e}")
            print(f"Usage: python3 server.py [port]")
            sys.exit(1)

    # Change to the directory containing this script
    script_dir = Path(__file__).parent.absolute()
    os.chdir(script_dir)

    # Create the server
    handler = http.server.SimpleHTTPRequestHandler

    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"╔═══════════════════════════════════════════════════════╗")
            print(f"║          NGØM World Clock - Web Server               ║")
            print(f"╠═══════════════════════════════════════════════════════╣")
            print(f"║                                                       ║")
            print(f"║  Server running at: http://{HOST}:{port}")
            print(f"║  Press Ctrl+C to stop                                ║")
            print(f"║                                                       ║")
            print(f"║  Directory: {script_dir}")
            print(f"║                                                       ║")
            print(f"╚═══════════════════════════════════════════════════════╝")
            print()

            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48 or e.errno == 98:  # Port already in use
            print(f"Error: Port {port} is already in use.")
            print(f"Try a different port: python3 server.py 9000")
        else:
            print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
