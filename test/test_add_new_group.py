from model.group import Group


def test_add_new_group(app, db,check_ui, json_groups):
    group = json_groups
    #print(group)
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    #print()
    #print(sorted(old_groups, key=Group.id_or_max))
    #print(sorted(new_groups, key=Group.id_or_max))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
