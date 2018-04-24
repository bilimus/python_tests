# -*- coding: utf-8 -*-
# test_python_task_4a

from model.contact import Contact


def test_add_new_contact(app):
    app.contact.add(Contact(firstname ='Bill', middlename ='Bill', lastname ='Imus', \
                            nickname ='Billimus', title = 'QA Tester', company ='QA Solutions', address ='Somewhere in the Universe', \
                            home_phone ='+122222222', mobile ='+13333333', work_phone = '+14444444', fax ='+15555555', \
                            email_1 ='Bill_1@qa.com', email_2 ='Bill_2@qa.com', email_3 ='Bill_2@qa.com', homepage ='IhaveNoPage.com', \
                            byear ='2000', ayear='2001', city ='Sim City', phone2 ='+156666666', notes_here ='some notes here'))
