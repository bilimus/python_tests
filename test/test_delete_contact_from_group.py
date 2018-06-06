from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_first_group(app, db, orm_db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname='test'))
    random_group = random.choice(db.get_group_list())
    if len(orm_db.get_contacts_in_group(random_group)) == 0:
        contacts_not_in_group = orm_db.get_contacts_not_in_group(random_group)
        random_contact = random.choice(contacts_not_in_group)
        app.contact.add_contact_to_group(random_contact.id, random_group.id)
    contacts_in_group = orm_db.get_contacts_in_group(random_group)
    random_contact = random.choice(contacts_in_group)
    app.contact.delete_contact_from_group(random_contact.id, random_group.id)
    assert random_contact not in orm_db.get_contacts_in_group(random_group)

