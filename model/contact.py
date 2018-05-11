from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, id=None, nickname=None, title=None, company=None, \
                 address=None, homephone=None, mobilephone=None, workphone=None, fax=None, email_1=None, email_2=None, \
                 email_3=None, homepage=None, byear=None, ayear=None, city=None, secondaryphone=None, notes_here=None,\
                 all_phones_from_home_page = None, all_e_mails_from_home_page = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.city = city
        self.secondaryphone = secondaryphone
        self.notes_here = notes_here
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_e_mails_from_home_page = all_e_mails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def __lt__(self, other):
        return self.id < other.id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize