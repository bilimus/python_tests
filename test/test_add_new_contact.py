# -*- coding: utf-8 -*-
# test_python_task_4a

from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contacts = Contact(firstname ='Bill', middlename ='Bill', lastname ='Imus', \
                            nickname ='Billimus', title = 'QA Tester', company ='QA Solutions', address ='Somewhere in the Universe', \
                            home_phone ='+122222222', mobile ='+13333333', work_phone = '+14444444', fax ='+15555555', \
                            email_1 ='Bill_1@qa.com', email_2 ='Bill_2@qa.com', email_3 ='Bill_2@qa.com', homepage ='IhaveNoPage.com', \
                            byear ='2000', ayear='2001', city ='Sim City', phone2 ='+156666666', notes_here ='some notes here')
    app.contact.add(contacts)
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)