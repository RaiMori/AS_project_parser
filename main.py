from pathlib import Path
import shutil
import subprocess
import lxml


class PhysicalConfiguration:
    
    def __init__(self, name, path):
        pass

    def build(self):
        pass

    def transfer(self):
        pass

    def run_unit_tests(self):
        pass

    def get_pre_build_events(self):
        pass

    def get_post_build_events(self):
        pass

    def set_pre_build_events(self):
        pass

    def set_post_build_events(self):
        pass

    def get_include_directories(self):
        pass

    def set_include_directories(self):
        pass


class AS_Build:
    """ Build BR Automation Studio project """
    def __init__(self, as_path, apj_path, configuration, rebuild=True, generate_ruc=True, simulation=True):
        self.as_path = as_path
        self.apj_path = apj_path
        self.config = configuration
        self.rebuild = rebuild
        self.generate_ruc = generate_ruc
        self.simulation = simulation

    def build(self):
        args = self.get_argumants()
        out = subprocess.run([self._get_as_builder_path(), *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return out

    def get_argumants(self):
        args_list = []
        args_list.append(self.apj_path)
        args_list.extend(["-c", self.config])
        # Build mode
        args_list.append("-buildMode")
        if self.rebuild:
            args_list.append("Rebuild")
        else:
            args_list.append("Build")
        # Build RUC Package for project transfer    
        if self.generate_ruc:
            args_list.append("-buildRUCPackage")
        # Build for simulation
        if self.simulation:
            args_list.append("-simulation")

        return args_list

    @staticmethod
    def parse_log(build_log):
        pass

    def _get_prj_path(self):
        raise NotImplementedError()

    def _get_as_builder_path(self):
        as_builder_path = Path(self.as_path).joinpath("Bin-En\BR.AS.Build.exe")
        return str(as_builder_path)


class PIL_File:

    def __init__(self):
        pass

    def get_pvi_parameters(self):
        pass

    def generate_pil(self):
        pass


class RUC_Transfer:

    def __init__(self):
        pass

    def generate_pil(self):
        pass

    def transfer(self):
        pass

    