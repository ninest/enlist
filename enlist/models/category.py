from enum import Enum, unique


@unique
class Category(Enum):
  BMT = "BMT"
  PUBLIC_HOLIDAY = "Public Holiday"