import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchByTitleTests(unittest.TestCase):
    """Regression tests for title search are added with the hotfix."""

    def test_search_by_title_case_insensitive(self):
        discs = [DigitalVideoDisc("The Lion King"), DigitalVideoDisc("Aladdin")]
        self.assertEqual(search_by_title(discs, "lion"), [discs[0]])
        self.assertEqual(search_by_title(discs, "LION"), [discs[0]])
        self.assertEqual(search_by_title(discs, "missing"), [])
