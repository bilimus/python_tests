from model.group import Group

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.modify_first_group(Group(name="name modified", header="header modified", footer="footer modified"))
    app.group.return_to_group_page()
    app.session.logout()
