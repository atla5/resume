import unittest
from update_values_helpers import *


SAMPLE_SCHOOL = {
    "company_name": "COMPANY_NAME",
    "company_url": "https://www.company-url.com",
    "advisor_name": "FNAME LNAME",
    "advisor_contact": "fname.lname@company.org",
    "advisor_position": "position",
    "location_city": "CITY",
    "location_state": "MA",
    "time_start": "2017-01",
    "time_end": "2017-12",
    "position": "POSITION AT COMPANY",
    "responsibilities": [
      "RESPONSIBILITY ONE...",
      "RESPONSIBILITY TWO...",
      "RESPONSIBILITY THREE..."
    ],
    "summary_short": "A short description",
    "summary_long": "A not so short description of what i did when i worked here."
  }


class TestBuild(unittest.TestCase):

    def test_humanize_date(self):
        self.assertEqual("Jan 2017", humanize_date("2017-01"))
        self.assertEqual("2017-13",  humanize_date("2017-13"))
        self.assertEqual("2017-00",  humanize_date("2017-00"))

    def test_humanize_list(self):
        self.assertEqual("one fish, two fish, red fish, blue fish", humanize_list(["one fish", "two fish", "red fish", "blue fish"]))
        self.assertEqual("one fish, two fish", humanize_list(["one fish", "two fish"]))
        self.assertEqual("one fish", humanize_list(["one fish"]))
        self.assertEqual("", humanize_list([""]))
        self.assertEqual("1, 2, 3, 4", humanize_list([1, 2, 3, "4"]))
