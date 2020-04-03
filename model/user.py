class User:
    def __init__(self, firstname=None, lastname=None, address1=None, postcode=None, city=None, country=None, email=None,
                 phone=None, password=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address1 = address1
        self.postcode = postcode
        self.city = city
        self.country = country
        self.email = email
        self.phone = phone
        self.password = password

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s" % (
        self.firstname, self.lastname, self.address1, self.postcode, self.city, self.country, self.email, self.phone,
        self.password)

