from abc import ABC, abstractmethod
from datetime import date
from typing import final


class AbstractUserAccount(ABC):
    """
      This abstract class represents a phone call between a caller (the
      phone number of the person who originates the call) and callee (the
      phone number of the person whose receives the phone call).  Phone
      calls begin and end at given times.
    """
    @abstractmethod
    def get_Name (self) -> str:
        """
        Returns:
             the name of the person with the twitter account
        """
        pass


    @abstractmethod
    def get_Username(self) -> str:
        """
            Returns:
                 the username of the person with the twitter account
        """
        pass

    @abstractmethod
    def get_Password(self) -> str:
        """
            Returns:
                 the password of the person with the twitter account
        """
        pass

    @abstractmethod
    def get_Email(self) -> str:
        """
            Returns:
                 the email of the person with the twitter account
        """
        pass

    @abstractmethod
    def get_Number(self) -> str:
        """
            Returns:
                 the email of the person with the twitter account
        """
        pass

    @abstractmethod
    def get_Join_Date (self) -> date:
        """
            Returns:
                the joining date of the person with the twitter account
        """
        pass

    @abstractmethod
    def get_Join_Date_string(self) -> str:
        """
            Returns:
                 a textual representation of the time the account this was recieved
        """
        pass




    @final
    def __str__(self)-> str:
        """
        Returns:
             a brief textual description of this phone call.
        """
        return \
            "Hello " + self.get_Name() +\
            "!\nUsername: " + self.get_Username() +\
            "\nEmail:" + self.get_Email() +\
            "Your password has been saved securely in our system. \n Thanks for joining on " + self.get_Join_Date_string();
