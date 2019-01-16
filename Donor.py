import shelve
import uuid
from datetime import date

class Donor:
    def __init__(self, item, expiry, quantity, special_req):
        self.__item = ''
        self.__expiry = expiry
        self.__quanitity = quantity
        self.__special_req = special_req

        def get_item(self):
            return self.__item

        def set_item(self, item):
            self.__item = item

        def get_expiry(self):
            return self.__expiry

        def set_expiry(self, expiry):
            self.__expiry = expiry

        def get_quantity(self):
            return self.__quanitity

        def set_quantity(self, quantity):
            self.__quanitiy = quantity

        def get_special_req(self):
            return self.__special_req

        def set_sepcial_req(self):
            self.__special_req = special_req
