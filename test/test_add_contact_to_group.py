from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
from model.group import Group



def test_add_new_contact_to_first_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    app.contact.add(Contact(firstname='test'))
    contact_id = app.contact.get_first_contact_id()
    group_id = app.group.get_first_group_id()
    app.contact.add_first_contact_to_first_group()

    db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')
    logic = False

    try:
        l = db.get_contacts_in_group(Group(id=group_id))
        for item in l:
            logic = logic or (item.id == contact_id)
    finally:
        pass

    assert logic

