import random

from model.project import Project


def test_add_project(app, orm):

    project = Project(name="Project" + str(random.randrange(100)), status=random.choice(["development", "release", "stable", "obsolete"]), inherit=random.choice([True, False]),
                      view_status=random.choice(["public", "private"]), description="Description" + str(random.randrange(100)))
    old_projects = orm.get_project_list()
    app.session.login("administrator", "root")
    app.project.create(project)
    app.session.logout()
    new_projects = orm.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
