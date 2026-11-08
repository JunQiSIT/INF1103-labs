class Supplier:
    def __init__(self, supplier_id: int, supplier_name: str, contact_email: str):
        self._supplier_id = supplier_id
        self._supplier_name = supplier_name
        self._contact_email = contact_email

    # Getters and Setters for supplier attributes
    @property
    def supplier_id(self):
        return self._supplier_id

    @property
    def supplier_name(self):
        return self._supplier_name

    @property
    def contact_email(self):
        return self._contact_email

    @supplier_id.setter
    def supplier_id(self, value: int):
        self._supplier_id = value

    @supplier_name.setter
    def supplier_name(self, value: str):
        self._supplier_name = value

    @contact_email.setter
    def contact_email(self, value: str):
        self._contact_email = value

    def display_information(self):
        print(f"Supplier ID: {self._supplier_id} | Supplier Name: {self._supplier_name} | Contact Email: {self._contact_email}")
