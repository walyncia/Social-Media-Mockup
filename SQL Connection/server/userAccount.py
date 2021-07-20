from objects.abstract_UserAccount import AbstractUserAccount



class UserAccount(AbstractUserAccount):
    def __init__(self, Name, Username, Password, Email, Number, Join_Date):
        self.__Name = Name
        self.__Username = Username
        self.__Password = Password
        self.__Email = Email
        self.__Number = Number
        self.__Join_Date = Join_Date


    def get_Name (self, Name) -> str:
        return self.__Name

    def get_Username(self, Username) -> str:
        return self.__Username

    def get_Password(self, Password) -> str:
        return self.__Password

    def get_Email(self, Email)-> str:
        return self.__Email

    def get_Number(self, Number)-> str:
        return self.__Number


    def get_Join_Date (self, Join_Date)-> str:
        return self.__Join_Date

    def __str__ (self) -> str:
        return self.__Name +' ' + self.__Username +' ' + self.__Password +' ' + self.__Email +' ' + self.__Number +' ' + self.__Join_Date
