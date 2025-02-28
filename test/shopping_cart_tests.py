import unittest
from src.shopping_cart import ShoppingCart


class TestCart(unittest.TestCase):
    def setUp(self):
        print("* setUp()")
        self.cart = ShoppingCart()

    def test_add_product(self):
        print("* test_add_product()")
        # Arrange
        product_name, price, quantity = "Apple", 2, 3
        expected_products = ["Apple"]

        # Act
        result = self.cart.add_product(product_name, price, quantity)

        # Assert
        self.assertTrue(result)
        self.assertEqual(self.cart.get_products(), expected_products)

    def test_remove_product(self):
        print("* test_remove_product()")
        # Arrange
        self.cart.add_product("Apple", 2, 3)

        # Act
        result = self.cart.remove_product("Apple")

        # Assert
        self.assertTrue(result)
        self.assertEqual(self.cart.get_products(), [])

    def test_update_quantity(self):
        print("* test_update_quantity()")
        # Arrange
        self.cart.add_product("Apple", 2, 3)
        new_quantity = 5

        # Act
        result = self.cart.update_quantity("Apple", new_quantity)

        # Assert
        self.assertTrue(result)
        self.assertFalse(self.cart.update_quantity("Banana", 2))

    def test_count_products(self):
        print("* test_count_products()")
        # Arrange
        self.cart.add_product("Apple", 2, 3)
        self.cart.add_product("Banana", 1, 2)
        expected_count = 2

        # Act
        result = self.cart.count_products()

        # Assert
        self.assertEqual(result, expected_count)

    def test_get_total_price(self):
        print("* test_get_total_price()")
        # Arrange
        self.cart.add_product("Apple", 2, 3)
        self.cart.add_product("Banana", 1, 2)
        expected_total = 8

        # Act
        result = self.cart.get_total_price()

        # Assert
        self.assertEqual(result, expected_total)

    def test_apply_discount_code(self):
        print("* test_apply_discount_code()")
        # Arrange
        self.cart.add_product("Apple", 2, 3)
        discount_code = "DISCOUNT10"
        expected_total = 6

        # Act
        result = self.cart.apply_discount_code(discount_code)
        total_price = self.cart.get_total_price()

        # Assert
        self.assertTrue(result)
        self.assertEqual(total_price, expected_total)

    def test_checkout(self):
        print("* test_checkout()")
        # Arrange
        self.cart.add_product("Apple", 2, 3)

        # Act
        result = self.cart.checkout()
        product_count = self.cart.count_products()

        # Assert
        self.assertTrue(result)
        self.assertEqual(product_count, 0)


if __name__ == "__main__":
    unittest.main()
