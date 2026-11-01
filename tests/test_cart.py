import io
import unittest
from contextlib import redirect_stdout

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class CartTests(unittest.TestCase):
    def make_cart(self, discs):
        cart = Cart()
        with redirect_stdout(io.StringIO()):
            for disc in discs:
                cart.add_dvd(disc)
        return cart

    def test_add_dvd_until_full(self):
        cart = Cart()
        with redirect_stdout(io.StringIO()):
            for index in range(MAX_NUMBERS_ORDERED):
                self.assertTrue(cart.add_dvd(DigitalVideoDisc(str(index))))
            self.assertFalse(cart.add_dvd(DigitalVideoDisc("21st DVD")))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)
