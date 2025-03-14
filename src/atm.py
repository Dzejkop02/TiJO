class InvalidPinException(Exception):
    pass


class InsufficientFundsException(Exception):
    pass


class ATM:
    """
    Klasa reprezentujÄca bankomat (ATM) z podstawowymi operacjami bankowymi.
    """

    def __init__(self):
        self.accounts = {
            1234: 1500.0,
            0000: 500.0,
            4321: 3000.0
        }

    def check_balance(self, pin: int) -> float:
        """
        Sprawdza saldo konta uĹźytkownika.

        :param pin: PIN uĹźytkownika.
        :return: Saldo konta uĹźytkownika.
        :raises InvalidPinException: JeĹli podany PIN jest nieprawidĹowy.
        """
        if pin not in self.accounts:
            raise InvalidPinException("Nieprawidłowy PIN")
        return self.accounts[pin]

    def deposit(self, pin: int, amount: float) -> float:
        """
        WpĹaca Ĺrodki na konto uĹźytkownika.

        :param pin: PIN uĹźytkownika.
        :param amount: Kwota do wpĹacenia.
        :return: Aktualne saldo po wpĹacie.
        :raises InvalidPinException: JeĹli podany PIN jest nieprawidĹowy.
        """
        if pin not in self.accounts:
            raise InvalidPinException("Nieprawidłowy PIN")
        if amount <= 0:
            raise ValueError("Kwota musi być większa od zera")
        self.accounts[pin] += amount
        return self.accounts[pin]

    def withdraw(self, pin: int, amount: float) -> float:
        """
        WypĹaca Ĺrodki z konta uĹźytkownika.

        :param pin: PIN uĹźytkownika.
        :param amount: Kwota do wypĹacenia.
        :return: Aktualne saldo po wypĹacie.
        :raises InsufficientFundsException: JeĹli saldo jest niewystarczajÄce.
        :raises InvalidPinException: JeĹli podany PIN jest nieprawidĹowy.
        """
        if pin not in self.accounts:
            raise InvalidPinException("Nieprawidłowy PIN")
        if amount <= 0:
            raise ValueError("Kwota musi być większa od zera")
        if self.accounts[pin] < amount:
            raise InsufficientFundsException("Brak wystarczających środków")
        self.accounts[pin] -= amount
        return self.accounts[pin]
