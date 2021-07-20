from abc import ABC, abstractmethod


class AbstractUserAccount_DOA( ABC ):
    '''This bstarct class defines functions for database manipulation '''

    @abstractmethod
    def insert_User(self,user):
        pass

    @abstractmethod
    def update_User(self, user, Username):
        pass

    @abstractmethod
    def delete_User(self, Username):
        pass

    @abstractmethod
    def select_User(self, Username):
        pass

    @abstractmethod
    def search_users_byusername(self, Username):
        pass

    @abstractmethod
    def search_users_bynumber(self, Number):
        pass

    @abstractmethod
    def is_user_exists(self, user):
        pass


