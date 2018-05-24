from model.contact import Contact
from random import randrange

def test_delete_some_contact(app, db, contact_json, chek_ui):
    contact = contact_json
    if len(db.get_contact_list()) == 0:
        app.contact.add(contact)
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    db.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1]=[]
    assert old_contacts == new_contacts

'''
def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname='test first name'))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1]=[]
    assert old_contacts == new_contacts
'''