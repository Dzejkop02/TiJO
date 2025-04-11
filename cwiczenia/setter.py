class User:
    def __init__(self, name, age):
        self._name = name
        if age < 0 or age > 150:
            raise ValueError(f"Nieprawidłowa wartość wieku: {age}")
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age < 0:
            print("Błąd: Wiek nie może być ujemny!")
            return
        if new_age > 150:
            print("Błąd: Wiek jest za duży!")
            return
        self._age = new_age


user = User("Jan", 30)
print(f"Poczatkowy wiek: {user.get_age()}")

user.set_age(-5)
print(f"Wiek po ustawieniu nieprawidlowej wartosci: {user.get_age()}")

user.set_age(200)
print(f"Wiek po ustawieniu absurdalnie duzej wartosci: {user.get_age()}")
