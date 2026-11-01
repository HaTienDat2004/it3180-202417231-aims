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

    def test_total_cost(self):
        cart = self.make_cart([
            DigitalVideoDisc("The Lion King", cost=19.95),
            DigitalVideoDisc("Star Wars", cost=24.95),
            DigitalVideoDisc("Aladdin", cost=18.99),
        ])
        self.assertAlmostEqual(cart.total_cost(), 63.89)

    def test_total_cost_with_discount(self):
        cart = self.make_cart([DigitalVideoDisc("Sample", cost=100)])
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80)

    def test_invalid_discount_percent(self):
        cart = self.make_cart([DigitalVideoDisc("Sample", cost=100)])
        for percent in (-1, 150):
            with self.subTest(percent=percent):
                with self.assertRaises(ValueError):
                    cart.total_cost_with_discount(percent)
