import sqlite3
from objects.UserAccount_doa import AbstractUserAccount_DOA


class SQL_DOA( AbstractUserAccount_DOA):
    '''This bstarct class defines functions for database manipulation '''
    def __init__(self, dbfile):
        self.dbfile = dbfile

    def insert_User(self,user):
        if not self.is_user_exists(user):
            conn = sqlite3.connect(self.dbfile)
            c = conn.cursor()
            data = (user["Name"], user["Username"],user["Password"],user["Email"], user["Number"], user["Join_Date"])
            print(user)
            c.execute('INSERT INTO UserData ( Name, Username, Password, Email, Number, Join_Date ) VALUES (?,?,?,?,?,?);', data)
            conn.commit()
            conn.close()
        #return Username


    def update_User(self, user, Username):
        pass


    def delete_User(self, Username):
        pass


    def select_User(self, Username):
        conn = sqlite3.connect(self.dbfile)
        c = conn.cursor()
        UserID = (Username)
        c.execute ("SELECT * FROM UserData WHERE Username=?;", (UserID,))
        return c.fetchone()


    def search_users_byusername(self, Username):
        pass


    def search_users_bynumber(self, Number):
        pass

    def is_user_exists(self, user):
        conn = sqlite3.connect(self.dbfile)
        c = conn.cursor()
        c.execute('select * from UserData where Email=?', (user["Email"],))
        rows =c.fetchone()
        if rows:
            return True
        else:
            return False

if __name__ == '__main__':
    doa = SQL_DOA('SocialMedia.db')
    user = dict()
    user['Name'] = 'Lyncia Brown'
    user['Username'] = 'BrownLyn'
    user['Password'] = '43nkCDJ2@@.!9'
    user['Email'] = "brownL12@yahoo.com"
    user['Number'] = "3024932300"
    user['Join_Date'] = "12/06/2017"
    print(doa.insert_User(user))
    #print(doa.select_User('Remyting29'))
    #print(doa.is_user_exists(user))