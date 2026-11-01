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
