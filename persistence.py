import shelve


class Donor:
    def __init__(self, item, quantity, expiry, req, email):
        self.__item = item
        self.__quantity = quantity
        self.__expiry = expiry
        self.__req = req
        self.__email = email

    def set_item(self, item):
        self.__item = item

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_expiry(self, expiry):
            self.__expiry = expiry

    def set_req(self, req):
        self.__req = req

    def set_email(self,email):
        self.__email = email


    def get_item(self):
        return self.__item

    def get_quantity(self):
        return self.__quantity

    def get_expiry(self):
        return self.__expiry

    def get_req(self):
        return self.__req

    def get_email(self):
        return self.__email

shelve = shelve.open('Donor')

def create_donor(donor):
     shelve[donor.gety_email()] = donor


