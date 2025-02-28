class ShoppingCart:

    def __init__(self):
        self.products = {}
        self.discount = 0

    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        if price < 0 or quantity <= 0:
            return False

        if product_name in self.products:
            self.products[product_name]['quantity'] += quantity
        else:
            self.products[product_name] = {'price': price, 'quantity': quantity}

        return True

    def remove_product(self, product_name: str) -> bool:
        return self.products.pop(product_name, None) is not None

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        if product_name in self.products and new_quantity > 0:
            self.products[product_name]['quantity'] = new_quantity
            return True
        return False

    def get_products(self):
        return list(self.products.keys())

    def count_products(self) -> int:
        return len(self.products)

    def get_total_price(self) -> int:
        total = sum(p['price'] * p['quantity'] for p in self.products.values())
        return total - (total * self.discount // 100)

    def apply_discount_code(self, discount_code: str) -> bool:
        valid_discounts = {"DISCOUNT10": 10, "DISCOUNT20": 20}
        if discount_code in valid_discounts:
            self.discount = valid_discounts[discount_code]
            return True
        return False

    def checkout(self) -> bool:
        if self.products:
            self.products.clear()
            self.discount = 0
            return True
        return False
