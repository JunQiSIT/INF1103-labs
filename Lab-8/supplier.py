class Supplier:
    def __init__(self, supplier_id, supplier_name, contact_email):
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.contact_email = contact_email

    @property
    def supplier_id(self):
        return self.supplier_id

    @property
    def supplier_name(self):
        return self.supplier_name

    @property
    def contact_email(self):
        return self.contact_email

    def display_information(self):
        print(f"Supplier ID: {self.supplier_id} | Name: {self.supplier_name} | Contact Email: {self.contact_email}")
