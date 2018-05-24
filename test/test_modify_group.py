from model.group import Group
from random import randrange


def test_modify_group(app, db, json_groups, check_ui):
    group = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


'''
def test_modify_first_group(app):
    group = Group(name="name modified", header="header modified", footer="footer modified")
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    print()
    print(sorted(old_groups, key=Group.id_or_max))
    print(sorted(new_groups, key=Group.id_or_max))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
'''
'''
def test_modify_group_name1(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="name modified")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    print()
    print(old_groups[index])
    old_groups[index] = group
    print(old_groups[index])
    print()
    print(sorted(old_groups, key=Group.id_or_max))
    print(sorted(new_groups, key=Group.id_or_max))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
'''
'''
def test_modify_first_group_header(app):
    group = Group(header="header test")
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
'''
'''
def test_modify_first_group_footer(app):
    group = Group(footer="footer test")
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
'''