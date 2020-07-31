from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

from enlist.get import get
from enlist.values import CURRENT_YEAR


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.send_header("Access-Control-Allow-Origin", "*")
    self.end_headers()

    events_list = get(in_json=True)

    resp = {
        'year': CURRENT_YEAR,
        'events_list': events_list
    }
    self.wfile.write(json.dumps(resp).encode())
    return
