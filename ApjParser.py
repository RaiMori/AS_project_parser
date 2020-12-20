from os import path

class ApjParser:
    
    def __init__(self, project_folder_path, apj_name):
        self.path = project_folder_path
        self.apj_name = apj_name
        self.apj_path = path.join(project_folder_path, apj_name)
        self.project_version = ''
        raise NotImplementedError()

    def _check_apj_path(self):
        raise NotImplementedError()

    def _read_apj_file(self):
        raise NotImplementedError()

    def parse(self):
        raise NotImplementedError()

    def get_technology_packages(self):
        raise NotImplementedError()

    def get_variables(self):
        raise NotImplementedError

    def get_project_info(self):
        raise NotImplementedError()

    def get_ansi_c_parameters(self):
        raise NotImplementedError()

    def get_motion_parameters(self):
        raise NotImplementedError()

    def get_project_parameters(self):
        raise NotImplementedError()

    def get_iec_parameters(self):
        raise NotImplementedError()

