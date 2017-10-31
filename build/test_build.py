import unittest
import os, json, csv
from update_values_helpers import *

data_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))


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

    def test_valid_json_data(self):
        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                try:
                    with open(os.path.join(data_dir,filename), 'r') as file:
                        json.loads(file.read())
                except ValueError:
                    self.fail("linting error found in {}".format(filename))

    def test_valid_csv_data(self):
        for filename in os.listdir(data_dir):
            if filename.endswith('.csv'):
                try:
                    with open(os.path.join(data_dir, filename), 'r') as csvfile:
                        for row in csv.reader(csvfile, delimiter=','):
                            if not bool(row) or not isinstance(row, list) or not all(isinstance(elem, str) for elem in row):
                                self.fail("error rendering csv file '{}' into list of strings.".format(filename))

                except Exception:
                    self.fail("error reading csv file: {}".format(filename))
