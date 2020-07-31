from enum import Enum, unique


@unique
class BMT(Enum):
  AB = "PES A/B BMT"
  AB_PTP = "PES A/B BMT (PTP)"
  C = "PES C BMT"
  E = "PES E BMT"


# @unique
# class PublicHoliday(Enum):
#   NEW_YEAR = "New Year"
#   CHINESE_NEW_YEAR = "Chinese New Year"