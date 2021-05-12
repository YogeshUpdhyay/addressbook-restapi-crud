from flask_restplus import fields
from api import api

add_address = api.model("add_address", {
    "name" : fields.String(),
    "address" : fields.String(),
    "city" : fields.String(),
    "state" : fields.String(),
    "country" : fields.String(),
    "pincode" : fields.String(),
    "phone_numbers" : fields.List(fields.String()),
    "email_address" : fields.String(),
})

updated_address = api.model("update_address", {
    "name" : fields.String(),
    "address" : fields.String(),
    "city" : fields.String(),
    "state" : fields.String(),
    "country" : fields.String(),
    "pincode" : fields.String(),
    "phone_numbers" : fields.List(fields.String()),
    "email_address" : fields.String(),
})
