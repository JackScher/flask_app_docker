from marshmallow import Schema, fields, validate


class DataSchema(Schema):
    country = fields.Str(required=True, validate=[validate.Length(equal=2, error="Country code length should be 2")])
    city = fields.Str(required=True, validate=[validate.Length(min=1, max=60, error="City length should be in range 1, 60")])
    street = fields.Str(required=True, validate=[validate.Length(min=1, max=60, error="Street length should be in range 1, 60")])
    unit = fields.Str(validate=[validate.Length(min=1, max=60, error="Unit length should be in range 1, 60")])
    zip = fields.Str(required=True)
    first_name = fields.Str(required=True, validate=[validate.Length(min=1, max=60, error="First name length should be in range 1, 60")])
    last_name = fields.Str(required=True, validate=[validate.Length(min=1, max=60, error="Last name length should be in range 1, 60")])
    email = fields.Str(validate=validate.And(validate.Length(min=1, max=60, error="Email length should be in range 1, 60"), validate.Email(error="Not a valid email address")))
    phone = fields.Str(validate=[validate.Length(min=1, max=15, error="Phone length should be in range 1, 15")])
    company = fields.Str(validate=[validate.Length(min=1, max=60, error="Company length should be in range 1, 60")])
