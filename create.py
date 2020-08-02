import datetime
import json
from enlist.get import get
from enlist.values import CURRENT_YEAR

event_list = get(in_json=True)

with open(f"{CURRENT_YEAR}-dates.json", "w") as f:
  json.dump(event_list, f)