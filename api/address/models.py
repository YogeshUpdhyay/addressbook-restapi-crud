from mongoengine import Document
from mongoengine.fields import *

class Address(Document):
    name = StringField()
    address = StringField()
    city = StringField()
    state = StringField()
    country = StringField()
    pincode = StringField()
    phone_numbers = ListField(StringField())
    email_address = StringField()

    def payload(self):
        return {
            "id": str(self.id),
            "name" : self.name,
            "address" : self.address,
            "city" : self.city,
            "state" : self.state,
            "country" : self.country,
            "pincode" : self.pincode,
            "phone_numbers" : self.phone_numbers,
            "email_address" : self.email_address
        }