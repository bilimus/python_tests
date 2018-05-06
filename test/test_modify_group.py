from model.group import Group
from random import randrange

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
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="name modified")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

'''
def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="header test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="header modified"))
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_list = sorted(old_groups, key=lambda p: int(p.id))
    new_list = sorted(new_groups, key=lambda p: int(p.id))
    assert old_list[:-1] == new_list[:-1]

def test_modify_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="footer test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="footer modified"))
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_list = sorted(old_groups, key=lambda p: int(p.id))
    new_list = sorted(new_groups, key=lambda p: int(p.id))
    assert old_list[:-1] == new_list[:-1] 
    
'''