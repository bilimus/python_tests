from model.contact import Contact
import random
import string

constant = [
    Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1",
    nickname="nickname1", title="title1", company="company1", address="address1",
    homephone="homephone1", mobilephone="mobilephone1", workphone ="workphone1", fax="fax1",
    email_1 ="amail_11", email_2="email_21", email_3="email_31", homepage="homepage1",
    byear="byear1", ayear="ayear1", city ="city1", secondaryphone="seconfdaryphone1", notes_here="notice_here1"),

    Contact(firstname="firstname2", middlename="middlename2", lastname="lastname2",
    nickname="nickname2", title="title2", company="company2" , address="address2",
    homephone="homephone2", mobilephone="mobilephone2", workphone ="workphone2", fax="fax2",
    email_1 ="amail_12", email_2="email_22", email_3="email_32", homepage="homepage2",
    byear="byear2", ayear="ayear2", city ="city2", secondaryphone="seconfdaryphone2", notes_here="notice_here2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname ='', middlename ='', lastname ='', \
                       nickname ='', title = '', company ='', address ='', \
                       homephone ='', mobilephone ='', workphone = '', fax ='', \
                       email_1 ='', email_2 ='', email_3 ='', homepage ='', \
                       byear ='', ayear='', city ='', secondaryphone='', notes_here ='')] + [\
        Contact(firstname =random_string("firstname", 10).strip(),middlename= random_string("middlename", 10).strip(),
        lastname =random_string("lastname", 10).strip(), \
                       nickname =random_string("nickname", 10).strip(), title = random_string("title", 10).strip(),
        company =random_string("company", 10).strip(), address =random_string("address", 10).strip(), \
                       homephone =random_string("homephone", 10).strip(), mobilephone =random_string("mobilephone", 10).strip(),
        workphone = random_string("workphone", 10).strip(), fax =random_string("fax", 10).strip(), \
                       email_1 =random_string("email_1", 10).strip(), email_2 =random_string("email_2", 10).strip(),
        email_3 =random_string("email_3", 10).strip(), homepage =random_string("homepage", 10).strip(), \
                       byear =random_string("byear", 10).strip(), ayear=random_string("ayear", 10).strip(),
        city =random_string("city", 10).strip(), secondaryphone=random_string("secondaryphone", 10).strip(),
        notes_here =random_string("notes_here", 10).strip())\
        for i in range(5)]