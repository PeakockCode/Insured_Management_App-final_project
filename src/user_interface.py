from insured_records import InsuredRecords
from validating_information import ValidatingInformation
from insured_person import InsuredPerson


class UserInterface:
    """
    Class initialize user interface to get data from users
    and read and print data about clients from the Evidence of Insured Persons database
    """
    def __init__(self):
        """
         Initialization method to create an instance of the UserInterface class.

        Attributes:
                - _evidence: Initialize object of the Insured Record class (database and methods) to run user interface
                - _last_id_number (int): simple unique id number
        """
        self._evidence = InsuredRecords()
        self._last_id_number = 0

    def _main_menu(self):
        """
        Menu options for the user
        """
        return ("----------------------------------------------\n"
                "Evidence of Insured Persons (EoIP)\n"
                "______________________________________________\n"
                "Menu:\n"
                "----------------------------------------------\n"
                "1. Add New Insured\n"
                "2. View details about all clients\n"
                "3. Search information about client\n"
                "4. Exit\n"
                "----------------------------------------------\n"
                "Select one option from menu:\n")

    def run_evidence_software(self):
        """
        Main program loop to manage records of insured clients
        (creating new clients, printing records, searching for specific individuals).
        """
        choice = 0
        while choice != 4:
            try:
                # Get user input for menu selection
                choice = int(input(self._main_menu()).strip())
                # Execute the selected option
                if choice == 1:
                    self.create_insured_person()
                    print("Press ENTER to continue.")
                    input()
                elif choice == 2:
                    print(self._evidence)
                    print("Press ENTER to continue.")
                    input()
                elif choice == 3:
                    # Allow searching for insured persons by name
                    search_switch = True
                    while search_switch:
                        first_name = input("Insert searching first name:")
                        surname = input("Insert searching surname:")
                        search_person = self._evidence.search_by_full_name(first_name, surname)
                        print(search_person)
                        # Allow repeating the searching process
                        retry = input("Do you want to try searching again? (Y/N):").lower()
                        if retry != 'y':
                            search_switch = False
                elif choice == 4:
                    # Exit the application
                    print("Thank you for using our service. "
                          "You are now exiting the Evidence of Insured Persons (EoIE) application...")
                else:
                    # Handle invalid menu choices
                    print("Invalid choice. Please choose a valid option between 1 and 4. Press ENTER to continue.")
                    input()
            except ValueError:
                # Handle non-integer input for menu selection
                print("Invalid input. Please enter a valid option between 1 and 4. Press ENTER to continue.")
                input()

    def get_personal_details(self, identify_detail):
        """
        Get and validate personal details based on the provided type.

        Parameters:
            - identify_detail (str): Type of personal detail to be selected.

        Returns:
            - Validated personal detail.
        """
        while True:
            try:
                personal_detail = self.user_input(identify_detail)
                # Validate and capitalize the input if it is a name or surname
                if identify_detail == "name" or identify_detail == "surname":
                    if ValidatingInformation.validate_name(personal_detail):
                        return personal_detail.capitalize()

                # Convert input to integer and validate if it is an age
                elif identify_detail == "age":
                    personal_detail = int(personal_detail)
                    if ValidatingInformation.validate_age(personal_detail):
                        return personal_detail

                # Validate input as a phone number
                elif identify_detail == "phone number":
                    if ValidatingInformation.validate_phone(personal_detail):
                        return personal_detail
        # Handle the exception for invalid input
            except ValueError:
                print("Invalid input. Please enter a valid input (string for name or integer between 1 - 99 for age).\n"
                      "Phone number must be without spaces and can contain 9 - 20 digits.")

    def user_input(self, identify_detail):
        """
        "Obtain user input regarding specific personal details. Convert string input to an integer (age) if necessary."

        Parameters:
            - identify_detail (str): personal user information/detail about name, surname, age, etc.

            Returns:
            - Personal user information/detail (str)
              """
        # Prompt the user to input personal details based on the provided type
        user_detail = input(f"Please, insert {identify_detail}: ").strip()
        if identify_detail == "age":
            return int(user_detail)
        return user_detail

    def generate_insurance_id(self):
        """
        Generates a new insurance number by incrementing the last allocated number.
        Returns:
            int: The newly generated ID number.
        """
        # Generate a unique client ID
        self._last_id_number += 1
        return self._last_id_number

    def create_insured_person(self):
        """
        Create an InsuredPerson object with validated personal details.

        Returns:
            - InsuredPerson: Object representing the insured person with validated details.
        """
        # Collect and validate personal details (through get_personal_details method) for creating an InsuredPerson
        id_number = self.generate_insurance_id()
        first_name = self.get_personal_details("name")
        surname = self.get_personal_details("surname")
        age = self.get_personal_details("age")
        phone_number = self.get_personal_details("phone number")

        # Create an InsuredPerson object with the validated details
        insured_person = InsuredPerson(id_number, first_name, surname, age, phone_number)
        # Save the evidence and display the saved data
        self._evidence.add_insured_person(insured_person)
        print(f"All data saved:\n{insured_person}")
