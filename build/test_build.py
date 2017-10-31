import unittest
from update_values_helper import *


class TestBuild(unittest.TestCase):

    def __init__(self):
        self.sample_school = SAMPLE_SCHOOL

    def test_humanize_date(self):
        self.assertEqual("Jan 2017", humanize_date("2017-01"))
        self.assertEqual("2017-13",  humanize_date("2017-13"))
        self.assertEqual("2017-00",  humanize_date("2017-00"))
