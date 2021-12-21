from models import Address, Contact


address_fields = [column for column in Address.__table__.columns if column.key in
                  ['country', 'city', 'street', 'unit', 'zip']]
contact_fields = [column for column in Contact.__table__.columns if column.key in
                  ['first_name', 'last_name', 'email', 'phone', 'company', 'address_id']]
