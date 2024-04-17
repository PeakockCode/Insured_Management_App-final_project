class InsuredRecords:
    """
    Class for managing insured records.
    """

    def __init__(self):
        """
        Initialize the InsuredRecord class.

        Attributes:
            - _insured_data_db (dict): Database to store insured person data where the client ID serves as the key.
        """

        self._insured_data_db = {}

    def __str__(self):
        """
        Return a string representation of all clients.

        Returns:
            str: Formatted string containing information (client id, full name, age, etc.) about all clients.
        """
        result = ""
        if self._insured_data_db:
            # Iterate over the database and create a formatted string
            # for each client containing name, surname, age and phone.
            print(f"ID{'':<15}\tName{'':<15}\tSurname{'':<15}\tAge{'':<15}\tPhone")
            for client_id, client_data in self._insured_data_db.items():
                result += (f"{client_id:<18}\t{client_data['name']:<18}\t{client_data['surname']:<20}\t"
                           f"{client_data['age']:<18}\t{client_data['phone']}\n")
        else:
            result += "No clients available!\n"
        return result

    def add_insured_person(self, insured_person):
        """
        Add a new insured person to the database.

        Returns:
            dict: The updated insured data database after adding the new person.
        """
        # Add the new insured person's data to the database
        self._insured_data_db[insured_person.id_number] = {
            "name": insured_person.first_name,
            "surname": insured_person.surname,
            "age": insured_person.age,
            "phone": insured_person.phone_number,
        }

    def search_by_full_name(self, first_name, surname):
        """
        Search for clients by their full name.

        Parameters:
            first_name (str): The first name of the client.
            surname (str): The surname of the client.

        Returns:
            list: A list of dictionaries containing matching client details
                  (Name, Surname, Age, Phone).
        """
        matching_clients = []
        # Check if both the first name and surname are strings
        if not isinstance(first_name, str) or not isinstance(surname, str):
            return "Please provide valid first name and surname."
        # Iterate through the database stored in the dictionary
        for client_id, client_data in self._insured_data_db.items():
            # Compare whether the searched first name and surname match the data in the database
            if (client_data['name'].lower() == first_name.lower()
                    and client_data['surname'].lower() == surname.lower()):
                # Add client data (in the form of a dictionary) to the matching_clients list
                matching_clients.append({"ID": client_id, "Name": client_data['name'],
                                         "Surname": client_data['surname'], "Age": client_data['age'],
                                         "Phone": client_data['phone']})
        # Check if any clients were found
        if not matching_clients:
            return "No clients with this name and surname available!"
        # Return the list of clients
        return matching_clients
