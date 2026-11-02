import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title
from aims.search import search_by_category


class SearchByCategoryTests(unittest.TestCase):
    def test_search_by_category(self):
        discs = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Star Wars", "Science Fiction"),
            DigitalVideoDisc("Aladdin", "Animation"),
        ]
        self.assertEqual(
            [disc.title for disc in search_by_category(discs, "animation")],
            ["The Lion King", "Aladdin"],
        )


class SearchByTitleTests(unittest.TestCase):
    """Regression tests for title search are added with the hotfix."""

    def test_search_by_title_case_insensitive(self):
        discs = [DigitalVideoDisc("The Lion King"), DigitalVideoDisc("Aladdin")]
        self.assertEqual(search_by_title(discs, "lion"), [discs[0]])
        self.assertEqual(search_by_title(discs, "LION"), [discs[0]])
        self.assertEqual(search_by_title(discs, "missing"), [])
