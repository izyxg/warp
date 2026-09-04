"""Static server for local development.

python -m http.server caches aggressively, which means an edited index.html
keeps serving the old copy until you hard-refresh. This sends no-store on
everything so a plain reload is always the current file.

    python serve.py [port]
"""
import os
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class NoCache(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write("%s %s\n" % (self.command, self.path))


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5173
    root = os.path.dirname(os.path.abspath(__file__))
    handler = partial(NoCache, directory=root)
    print("warp -> http://localhost:%d  (no-store)" % port, flush=True)
    print("     serving %s" % root, flush=True)
    ThreadingHTTPServer(("127.0.0.1", port), handler).serve_forever()
