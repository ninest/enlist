import datetime

from .category import Category
from .event_types import BMT

DATE_FORMAT = "%b %d, %Y"


class Event:
  def __init__(self, title, start, end, category):
    self.title = title
    self.start = start
    self.end = end
    self.category = category

  @staticmethod
  def from_json(json_dict):

    # remove unknown/unknown from title
    title = json_dict["title"].split("unknown/unknown")[0]

    # parse dates
    try:
      start = datetime.datetime.strptime(json_dict["startDate"], DATE_FORMAT)
    except:
      start = None

    try:
      end = datetime.datetime.strptime(json_dict["endDate"], DATE_FORMAT)
    except:
      end = None

    # category is can be BMT or public holiday
    category = json_dict["categories"]
    if "BMT" in category:
      category = Category.BMT
    else:
      category = Category.PUBLIC_HOLIDAY

    return Event(title=title, start=start, end=end, category=category,)

  def to_json(self):
    dic = {
        "title": self.title,
        "start": int(int(self.start.strftime("%s%f"))/1000),
        "category": self.category.value
    }
    if self.end:
      dic["end"] = int(int(self.start.strftime("%s%f"))/1000)
    return dic

  def __str__(self):
    if self.start == self.end:
      return f"<{self.title} - {self.category} - {self.start}>"
    else:
      return f"<{self.title} - {self.category} - {self.start} to {self.end} >"
