from pathlib import Path

class ASProject:

    def __init__(self, prj_path):
        if Path(prj_path).is_dir():
            self.root_path = prj_path
        else:
            raise Exception("Path to AS project doesn't exist")

        # Check apj file. Return name and path
        # Check and set Logical dir
        # Check and set Physical dir
        # Read all HW configurations
        # Create objects for each config

    def __getattribute__(self, attr_name):
        pass

    def _find_apj(self):
        raise NotImplementedError()

    def _check_dir_exist(self):
        raise NotImplementedError()

    def _read_hw_configs(self):
        raise NotImplementedError()

    def _create_configs_objs(self):
        raise NotImplementedError()