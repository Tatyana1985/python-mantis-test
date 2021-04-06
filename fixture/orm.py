from datetime import datetime

from pony.orm import *

from model.project import Project


class ORMFixture:

    db = Database()

    class ORMProject(db.Entity):
        _table_ = "mantis_project_table"
        id = PrimaryKey(int, column="id")
        name = Optional(str, column="name")
        status = Optional(int, column="status")
        inherit = Optional(int, column="inherit_global")
        view_status = Optional(int, column="view_state")
        description = Optional(str, column="description")

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    @db_session
    def get_project_list(self):
        # with db_session:
        return self.convert_project_to_model(select(p for p in ORMFixture.ORMProject))

    def convert_project_to_model(self, projects):
        def convert(project):
            return Project(id=str(project.id), name=project.name, status=project.status, inherit=project.inherit, view_status=project.view_status,
                           description=project.description)
        return list(map(convert, projects))