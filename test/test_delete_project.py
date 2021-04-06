import random

from model.project import Project
def test_delete_project(app, orm):
    project = Project(name="Project" + str(random.randrange(100)),
                      status=random.choice(["development", "release", "stable", "obsolete"]),
                      inherit=random.choice([True, False]),
                      view_status=random.choice(["public", "private"]),
                      description="Description" + str(random.randrange(100)))
    if len(orm.get_project_list()) == 0:
        app.project.create(project)
    old_projects = orm.get_project_list()
    project = random.choice(old_projects)
    app.session.login("administrator", "root")
    app.project.delete(project)
    app.session.logout()
    old_projects.remove(project)
    new_projects = orm.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
