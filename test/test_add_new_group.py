# -*- coding: utf-8 -*-
# test_python_task_4

from model.group import Group


def test_add_new_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="ccc", header="ccc", footer="ccc"))
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_list = sorted(old_groups, key=lambda p: int(p.id))
    new_list = sorted(new_groups, key=lambda p: int(p.id))
    assert old_list == new_list[:-1]


#def test_add_new_empty_group(app):
#    old_groups = app.group.get_group_list()
#    app.group.create(Group(name="", header="", footer=""))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) + 1 == len(new_groups)
#    old_list = sorted(old_groups, key=lambda p: int(p.id))
#    new_list = sorted(new_groups, key=lambda p: int(p.id))
#    assert old_list == new_list[:-1]

