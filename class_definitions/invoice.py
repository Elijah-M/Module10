"""
Author: Elijah Morishita
elmorishita@dmacc.edu
10/26/2020
This program is used for creating an example of the uses of a class
"""


class Invoice:
    """
    A constructor that sets the variables
    """
    def __init__(self, invoice_id, customer_id, last_name, first_name, phone_number, address, items_with_price={}):
        self._invoice_id = invoice_id
        self._customer_id = customer_id
        self._last_name = last_name
        self._first_name = first_name
        self._phone_number = phone_number
        self._address = address
        self._items_with_price = items_with_price

    def __str__(self):
        """
        A string conversion method
        :return:
        """
        return "Invoice ID: " + self._invoice_id + "\n" \
               "Customer ID: " + self._customer_id + "\n"\
               + self._last_name + ', ' + self._first_name + "\n" \
               + self._phone_number + "\n" \
               + self._address

    def __repr__(self):
        """
        An official true string conversion (more accurate)
        :return:
        """
        return "Invoice ID: " + self._invoice_id + "\n" \
               "Customer ID: " + self._customer_id + "\n"\
               + self._last_name + ', ' + self._first_name + "\n" \
               + self._phone_number + "\n" \
               + self._address

    def add_item(self, x):
        """
        This function adds items to a dictionary
        :param x:
        :return:
        """
        self._items_with_price.update(x)

    def create_invoice(self):
        """
        This function calculates the values of the dictionary, prints the tax total,
        and prints the full total
        :return:
        """
        print(invoice, "\n", "=" * 40)
        for x, y in self._items_with_price.items():
            print(x, y)

        tax = 0.06  # tax amount

        tax_total = list(self._items_with_price.values())  # converting the values of the dict to a list

        tax_total_sum = 0
        for x in range(0, len(tax_total)):
            tax_total_sum = tax_total_sum + tax_total[x]

        tax = tax_total_sum * tax  # Tax Total
        total = tax_total_sum + tax  # Total invoice with tax

        print("Tax.....", tax)
        print("Total...", total)


# Driver
invoice = Invoice("9908", "432", "Morishita", "Elijah", "(555) 555-5555", "123 Main st.\nDes Moines, IA 50265")
invoice.add_item({"Soda": 0.99})
invoice.add_item({"Hamburger": 3.99})
invoice.create_invoice()
