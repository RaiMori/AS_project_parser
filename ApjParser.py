from os import path
import lxml

class ApjParser:
    
    def __init__(self, project_folder_path, apj_name=None):
        self.path = project_folder_path
        if apj_name:
            self.apj_name = apj_name
        else:
            self.apj_name = self._find_apj_file(project_folder_path)
        self.apj_path = path.join(project_folder_path, apj_name)
        if self._check_apj_path():
            pass
        else:
            raise ValueError('Unable to find apj file. Please check path to project')

    def _check_apj_path(self):
        raise NotImplementedError()

    def _read_apj_file(self) -> str:
        with open(self.apj_path, 'r') as f:
            content = f.read()

        return content

    @staticmethod
    def _find_apj_file(project_path):
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


if __name__=="__main__":
    prj_path = ''
    apj_name = 'PLC_Framework.apj'
    apj_parser = ApjParser(prj_path, apj_name)
