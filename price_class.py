__author__ = 'glennschultz'


class PriceTypes:
    def __init__(self, price_decimal, price_decimal_string, price_32nds, price_basis):
        """
        :type price_decimal string
        :type price_decimal_string string
        :type price_32nds string
        :type price_basis: string
        """
        self.price_decimal = price_decimal
        self.price_decimal_string = price_decimal_string
        self.price_32nds = price_32nds
        self.price_basis = price_basis
