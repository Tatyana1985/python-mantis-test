from suds.client import Client
from suds import WebFault

from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def transform (self, projects_element):
        return Project(id=str(projects_element.id), name=projects_element.name, status=projects_element.status.id, inherit = None,
                       view_status=projects_element.view_state.id, description=projects_element.description)

    def get_projects_list_for_user(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        projects_array = []
        try:
            projects_array = client.service.mc_projects_get_user_accessible(username, password)
        except WebFault:
            assert (str(WebFault))
        if len(projects_array) > 0:
            return list(map(self.transform, projects_array))
        else:
            return projects_array




