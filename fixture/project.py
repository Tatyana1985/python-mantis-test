import random


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_manage_proj_page()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("//input[@value = 'Create New Project']").click()
        self.fill(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None

    def fill(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("status").click()
        wd.find_element_by_xpath("//select[@name='status']//option[text()='%s']" % project.status).click()
        if project.inherit:
            wd.find_element_by_xpath("//input[@type='checkbox']")
        wd.find_element_by_name("view_state").click()
        wd.find_element_by_xpath("//select[@name='view_state']//option[text()='%s']" % project.view_status).click()
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)

    project_cache = None

    def open_manage_proj_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/my_view_page.php"):
            wd.find_element_by_link_text("Manage").click()

    def delete(self, project):
        wd = self.app.wd
        self.open_manage_proj_page()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("//tr[contains(@class,'row')]//a[@href = 'manage_proj_edit_page.php?project_id=%s']" % project.id).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
