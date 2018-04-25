from model.group import Group

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name test", header="header test", footer="footer test"))
    app.group.modify_first_group(Group(name="name modified", header="header modified", footer="footer modified"))

def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name test"))
    app.group.modify_first_group(Group(name="name modified"))

def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="header test"))
    app.group.modify_first_group(Group(header="header modified"))

def test_modify_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="footer test"))
    app.group.modify_first_group(Group(footer="footer modified"))


