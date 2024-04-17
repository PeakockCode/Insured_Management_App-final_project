import re


class ValidatingInformation:
    """
    A class for validating personal information.

    Methods:
    1. validate_name(name): Validates the provided name or surname.
    2. validate_age(age): Validates the provided age within a specific range.
    3. validate_phone(phone_number): Validates the provided phone number format.
    """

    @staticmethod
    def validate_name(name):
        """
        Validate the provided name or surname.

        Parameters:
            - name (str): The name or surname to be validated.

        Returns:
            bool: True if the name is valid (alphabetical and not empty), False otherwise.
        """
        if not name or not name.isalpha():
            print("The name or surname is mandatory information and must be alphabetical.")
            return False
        else:
            return True

    @staticmethod
    def validate_age(age):
        """
        Validate the provided age.

        Parameters:
            - age (int): The age to be validated.

        Returns:
            bool: True if the age is valid (integer between 1 and 99), False otherwise.
        """
        if not isinstance(age, int) or age < 1 or age > 99:
            print("The insured person must be number between 1 and 99 years old.")
            return False
        else:
            return True

    @staticmethod
    def validate_phone(phone_number):
        """
        Validate the provided phone number format.

        Parameters:
            - phone_number (str): The phone number to be validated.

        Returns:
            bool: True if the phone number is in the recommended format, False otherwise.
        """
        phone_pattern = re.compile(r'^\(?\+?[\d()-]{9,20}$')
        if phone_pattern.match(phone_number):
            return True
        else:
            print("Inserted wrong phone number. The recommended format is +420777888999 or (+420)-777-888-999.\n"
                  "The min and max number of digits you can insert is between 9 to 20.")
            print(
                "--------------------------------------------------------------------------------------------\n"
                "Footnote:\n"
                "--------------------------------------------------------------------------------------------\n"
                "*The typical mobile phone format in the Czech Republic consists\n"
                "of 12 digits and 1 symbol (+420777888999). The number includes \n"
                "the country code (+420) and 9 digits for the phone number (777888999)\n"
                "--------------------------------------------------------------------------------------------")
            return False
