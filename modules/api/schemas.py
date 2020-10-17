"""Module with marshmallow schemas for API"""

from datetime import datetime

from marshmallow import Schema, fields, validate


class DateTimeField(fields.DateTime):
    """
    Custom DateTime field for marshmallow

    :url: https://github.com/marshmallow-code/marshmallow/issues/656#issuecomment-318587611
    """

    def _deserialize(self, value, attr, data, **kwargs):
        if isinstance(value, datetime):
            print(f'WTF')

            return value

        return super()._deserialize(value, attr, data, **kwargs)


class AddNewUser(Schema):
    """Schema for adding new user"""

    first_name = fields.Str(required=True)
    second_name = fields.Str(required=True)
    position = fields.Str(required=True)
    email = fields.Email(required=True)
    phone_number = fields.Str(required=True)

    is_internal = fields.Bool(required=False, default=False)


class AddNewDocument(Schema):
    """Schema for adding new documents"""

    document_name = fields.Str(required=True)
    document_type = fields.Str(required=True)
    date_of_creation = DateTimeField(required=True, format='%Y-%m-%d')
    date_of_registration = DateTimeField(required=True, format='%Y-%m-%d')

    creators_ids = fields.List(fields.Int, required=True)

    controllers_ids = fields.List(fields.Int, required=False)


class AddNewTask(Schema):
    """Schema for adding new tasks"""

    task_name = fields.Str(required=True)

    executor_id = fields.Int(required=True)
    document_id = fields.Int(required=True)


class UpdateTableSchema(Schema):
    """Schema for updating table"""

    last_n_days = fields.Int(required=False, default=0)
