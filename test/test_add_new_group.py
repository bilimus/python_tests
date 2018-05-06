# -*- coding: utf-8 -*-
# test_python_task_4

from model.group import Group
from sys import maxsize

def test_add_new_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="ccc", header="ccc", footer="ccc")
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    old_groups.append(group)
    new_groups = app.group.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_new_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    old_groups.append(group)
    new_groups = app.group.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

