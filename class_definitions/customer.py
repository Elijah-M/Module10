"""
Author: Elijah Morishita
elmorishita@dmacc.edu
10/26/2020
This program is used for testing the use of classes and objects
"""


class Customer:

    # The constructor
    def __init__(self, customer_id, last_name="Morishita", first_name="Elijah",
                 phone_number="(555) 555-5555", address="123 Main St.\nDes Moines, IA 50265"):
        """
        This constructor sets the variables, with the exception of customer_id which is required
        :param customer_id:
        :param last_name:
        :param first_name:
        :param phone_number:
        :param address:
        """

        if isinstance(customer_id, int) == False:
            print("Non-numeric value entered")
            raise AttributeError

        self._customer_id = customer_id
        self._last_name = last_name
        self._first_name = first_name
        self._phone_number = phone_number
        self._address = address

    def __str__(self):
        """
        A string conversion method
        :return:
        """
        return "Customer ID: " + self._customer_id + "\n"\
        + self._last_name + ', ' + self._first_name + "\n"\
        + self._phone_number + "\n"\
        + self._address

    def __repr__(self):
        """
        An official true string conversion (more accurate)
        :return:
        """
        return "Customer ID: " + self._customer_id + "\n"\
        + self._last_name + ', ' + self._first_name + "\n"\
        + self._phone_number + "\n"\
        + self._address

    def display(self):
        """
        This function returns the string of a class object
        :return:
        """
        cust = Customer(str(''))
        return str(cust)


# Driver
customer1 = Customer(9)
print(customer1.display())

customer2 = Customer('e')
print(customer2.display())
