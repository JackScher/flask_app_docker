from flask import Flask, jsonify, request
from marshmallow import ValidationError

from models import Address, Contact
from schemas import DataSchema
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from config import address_fields, contact_fields


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1111@localhost/flask_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def create_filters(fields: list) -> list:
    data_args = {field: request.args.get(field.key, None) for field in fields if
                 request.args.get(field.key, None) is not None}
    return [field.like(data_args[field]) for field in data_args]


@app.route('/', methods=['GET', 'POST'])
def main():
    data_schema = DataSchema()
    many_data_schema = DataSchema(many=True)
    if request.method == 'GET':
        if not request.args:
            data = Contact.query.all()
            data = many_data_schema.dump(data)
            return jsonify(data), 200

        address_filters = create_filters(address_fields)
        contact_filters = create_filters(contact_fields)

        contacts = Contact.query.filter(and_(True, *contact_filters)).join(Address).filter(and_(True, *address_filters)).all()
        contacts = many_data_schema.dump(contacts)
        return jsonify(contacts), 200

    if request.method == 'POST':
        if not request.is_json:
            return jsonify("Not JSON request."), 415
        data = request.get_json()
        try:
            validated_data = data_schema.load(data)
            validated_data["address_id"] = Address.create(**validated_data)
            created_contact = Contact.create(**validated_data)
            created_contact = data_schema.dump(created_contact)
            return jsonify(created_contact), 201
        except ValidationError as err:
            return err.messages, 422


if __name__ == '__main__':
    app.run(debug=True)
