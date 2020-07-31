import pytest
import datetime
from enlist.models.event import Event
from enlist.models.category import Category


@pytest.fixture(scope='module')
def json_event():
  event = Event.from_json({
      "title": "New Yearunknown/unknown",
      "startDate": "Jan 1, 2019",
      "endDate": "Jan 1, 2019",
      "categories": "/CMPB Portal Content/Calendar Taxonomy/Public Holiday",
  })
  yield event


@pytest.fixture(scope='module')
def coded_event():
  yield Event(
      title="New Year",
      start=datetime.datetime(2019, 1, 1),
      end=datetime.datetime(2019, 1, 1),
      category=Category.PUBLIC_HOLIDAY
  )


def test_title(json_event, coded_event):
  assert json_event.title == coded_event.title

def test_category(json_event, coded_event):
  assert json_event.category == coded_event.category

def test_dates(json_event, coded_event):
  assert json_event.start == coded_event.start
  assert json_event.end == coded_event.end
