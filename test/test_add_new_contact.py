# -*- coding: utf-8 -*-
# test_python_task_4a

from model.contact import Contact


def test_add_new_contact(app, json_contacts):
    contacts = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contacts)
    assert len(old_contacts)+1 == app.contact.count()
    old_contacts.append(contacts)
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)