from marshmallow import Schema, fields, validate


class AddNewUser(Schema):
    """Schema for adding new user"""

    first_name = fields.Str(required=True)
    second_name = fields.Str(required=True)
    position = fields.Str(required=True)
    email = fields.Email(required=True)
    phone_number = fields.Str(required=True)

    is_internal = fields.Bool(required=False, default=False)
