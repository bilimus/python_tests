from model.contact import Contact
import random
import string
import jsonpickle
import getopt
import sys
import os.path


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    #out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))