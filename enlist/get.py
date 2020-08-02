import json
from datetime import datetime
from .models.event import Event
from .values import CURRENT_YEAR

# https://www.cmpb.gov.sg/web/wcm/connect/cmpb/cmpbContent/CMPBHome/before-ns/Enlistment-dates/enlistment-dates?srv=cmpnt&source=library&cmpntname=CMPBDesign/sections/page-2-BeforeNS/enlistment-dates/NAV%20Calendar%20Events%20Json"


def get(in_json=False):
  # messy is from CMPPB
  with open('./enlist/data/messy-2020-dates.json') as f:
    data = json.load(f)

  event_list = []
  for event_dict in data["calendarEventList"][1:]:
    event = Event.from_json(event_dict)
    event_list.append(event)

  # sort by date
  event_list = sorted(
    event_list,
    key=lambda x: x.start.date()
  )

  # convert everything to json
  json_event_list = []
  if in_json:
    for event in event_list:
      json_event_list.append(event.to_json())
    return json_event_list

  return event_list
