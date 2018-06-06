from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
import random

def test_add_contact_to_group(app, db, orm_db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    if len(db.get_contact_list())==0:
        app.contact.add(Contact(firstname='test'))
    random_group = random.choice(db.get_group_list())
    contacts_out_of_group=orm_db.get_contacts_not_in_group(random_group)
    if len(contacts_out_of_group)==0:
        contacts_in_group = orm_db.get_contacts_in_group(random_group)
        random_contact = random.choice(contacts_in_group)
        app.contact.delete_contact_from_group(random_contact.id, random_group.id )
    random_contact_out_of_group = random.choice(contacts_out_of_group)
    app.contact.add_contact_to_group(random_contact_out_of_group.id, random_group.id)
    assert random_contact_out_of_group in orm_db.get_contacts_in_group(random_group)



