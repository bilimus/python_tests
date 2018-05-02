from model.group import Group

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name test", header="header test", footer="footer test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="name modified", header="header modified", footer="footer modified"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="name modified"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="header test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="header modified"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="footer test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="footer modified"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
