from model.group import Group

def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="name modified", header="header modified", footer="footer modified"))

def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="name modified"))

def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header="header modified"))

def test_modify_first_group_footer(app):
    app.group.modify_first_group(Group(footer="footer modified"))


