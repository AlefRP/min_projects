import unittest
from models.product import Product

class TestProduct(unittest.TestCase):

    def setUp(self: object) -> None:
        self.ps4: Product = Product("PS4", 200)
        self.xbox: Product = Product("Xbox", 300)

    def test_instance(self: object) -> None:
        self.assertIsInstance(self.ps4, Product)
        self.assertIsInstance(self.xbox, Product)

    def test_name(self: object) -> None:
        self.assertEqual(self.ps4.name, "PS4")
        self.assertEqual(self.xbox.name, "Xbox")
