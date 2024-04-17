class InsuredPerson:

    """
    Class representing an insured person.

    Attributes:
        _id_number (int): ID number belonging to the insured person.
        _first_name (str): First name of the insured person.
        _surname (str): Surname of the insured person.
        _age (int): Age of the insured person.
        _phone_number (str): Phone number of the insured person.
    """

    def __init__(self, id_number, first_name, surname, age, phone_number):

        """
        Initialization method to create an instance of the InsuredPerson class.

        Parameters:
            id_number (int): ID number belonging to the insured person.
            first_name (str): First name of the insured person.
            surname (str): Surname of the insured person.
            age (int): Age of the insured person.
            phone_number (str): Phone number of the insured person.
        """
        self._id_number = id_number
        self._first_name = first_name
        self._surname = surname
        self._age = age
        self._phone_number = phone_number

    def __str__(self):

        """
        To string method that returns a formatted text with information about the insured person.

        Returns:
            str: Formatted text with information about the insured person.
        """

        return (f"ID: {self._id_number}\nName: {self._first_name}\nSurname: {self._surname}\n"
                f"Age: {self._age}\nPhone: {self._phone_number}")

    @property
    def id_number(self):
        return self._id_number

    @property
    def first_name(self):
        return self._first_name

    @property
    def surname(self):
        return self._surname

    @property
    def age(self):
        return self._age

    @property
    def phone_number(self):
        return self._phone_number
