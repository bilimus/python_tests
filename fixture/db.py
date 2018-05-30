import pymysql.cursors
from model.group import Group
from model.contact import Contact
import re


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,database=name, user=user, password=password)
        #self.connection.autocommit_mode = True
        self.connection.autocommit(True)


    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=re.sub("\s+", " ", name).strip(),
                                  header=re.sub("\s+", " ", header).strip(), footer=re.sub("\s+", " ", footer).strip()))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, lastname, firstname, address from addressbook WHERE deprecated = 0")
            for row in cursor:
                (id, lastname, firstname, address) = row
                list.append(Contact(id=str(id), lastname=re.sub("\s+", " ", lastname).strip(),
                        firstname=re.sub("\s+", " ", firstname).strip(), address=re.sub("\s+", " ", address).strip()))
        finally:
            cursor.close()
        return list

    def get_full_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, lastname, firstname, address, home, mobile, work, phone2, email, email2, email3"
                           " from addressbook WHERE deprecated = 0")
            for row in cursor:
                (id, lastname, firstname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(Contact(id=str(id), lastname=re.sub("\s+", " ", lastname).strip(),
                        firstname=re.sub("\s+", " ", firstname).strip(), address=re.sub("\s+", " ", address).strip(),
                        homephone=re.sub("\s+", " ", home).strip(),mobilephone=re.sub("\s+", " ", mobile).strip(),
                        workphone=re.sub("\s+", " ", work).strip(), secondaryphone=re.sub("\s+", " ", phone2).strip(),
                        email_1 =re.sub("\s+", " ", email).strip(),
                        email_2=re.sub("\s+", " ", email2).strip(),email_3 =re.sub("\s+", " ", email3).strip(),))

        finally:
            cursor.close()
        return list



    def destroy (self):
        self.connection.close()