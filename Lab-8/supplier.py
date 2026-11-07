class Supplier:
    def __init__(self, supplier_id, supplier_name, contact_email):
        self._supplier_id = supplier_id
        self._supplier_name = supplier_name
        self._contact_email = contact_email

    @property
    def supplier_id(self):
        return self._supplier_id

    @property
    def supplier_name(self):
        return self._supplier_name

    @property
    def contact_email(self):
        return self._contact_email

    def display_information(self):
        print(f"Supplier ID: {self._supplier_id} | Name: {self._supplier_name} | Contact Email: {self._contact_email}")
