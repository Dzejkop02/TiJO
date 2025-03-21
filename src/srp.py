# Naruszona zasada SRP

class Order:
    def __init__(self, id, items, customer):
        self.id = id
        self.items = items
        self.customer = customer


class OrderValidator:
    def validate(self, order):
        print("Walidacja zamówienia.")


class OrderRepository:
    def save(self, order):
        print("Zapisywanie zamówienia do bazy danych.")


class EmailSender:
    def send_confirmation(self, order):
        print("Wysyłanie e-maila potwierdzającego.")


class OrderProcessor:
    def __init__(self, validator, repository, email_sender):
        self.validator = validator
        self.repository = repository
        self.email_sender = email_sender

    def process_order(self, order):
        self.validator.validate(order)
        self.repository.save(order)
        self.email_sender.send_confirmation(order)


class OrderProcessor:
    def __init__(self, validator, repository, email_sender):
        self.validator = validator
        self.repository = repository
        self.email_sender = email_sender

    def process_order(self, order):
        self.validator.validate(order)
        self.repository.save(order)
        self.email_sender.send_confirmation(order)


order = Order("123", ["Produkt A", "Produkt B"], "Jan Kowalski")
validator = OrderValidator()
repository = OrderRepository()
email_sender = EmailSender()
processor = OrderProcessor(validator, repository, email_sender)
