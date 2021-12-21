from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1111@localhost/flask_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60))
    phone = db.Column(db.String(15))
    company = db.Column(db.String(60))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    @classmethod
    def create(cls, **kw):
        obj = cls(first_name=kw.get('first_name', '').strip(), last_name=kw.get('last_name', '').strip(),
                  email=kw.get('email', '').strip(), phone=kw.get('phone', '').strip(),
                  company=kw.get('company', '').strip(), address_id=kw.get('address_id'))
        db.session.add(obj)
        db.session.commit()
        return obj

    def __repr__(self):
        return f'Contact {self.id}'


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(2), nullable=False)
    city = db.Column(db.String(60), nullable=False)
    street = db.Column(db.String(60), nullable=False)
    unit = db.Column(db.String(60))
    zip = db.Column(db.Integer)

    @classmethod
    def create(cls, **kw):
        obj = cls(country=kw.get('country', '').strip().upper(), city=kw.get('city', '').strip(),
                  street=kw.get('street', '').strip(), unit=kw.get('unit', '').strip(), zip=kw.get('zip'))
        db.session.add(obj)
        db.session.commit()
        return obj.id

    def __repr__(self):
        return f'Address {self.id}'
