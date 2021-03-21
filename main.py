

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


class ASPathManager:
    def __init__(self, as_path):
        pass

    def get_global_as_path(self):
        pass

    def get_as_installation_path(self):
        pass

    def get_as_version(self):
        pass

    def get_as_dot_version(self):
        pass



# HW Configuration managment
class PhysicalParser:
    """ Parse physical directory to get available HW configurations """


class PhysicalCfgPkgParser:
    """ Get CPU folder for current hw configuration """


class CPUPkgParser:

    def __init__(self, cpu_pkg_path):
        self.path = cpu_pkg_path
        self.cpu_pkg_tree = None

    def get_option(self, options_name):
        raise NotImplementedError()

    def set_option(self, options_name, value):
        raise NotImplementedError()

    def get_runtime_version(self):
        raise NotImplementedError()

    def set_runtime_version(self):
        raise NotImplementedError()


    # get/set runtime version
    # get/set build options:
        # get/set additional build options
        # get/set additional include directories
        # get/set gcc version
        # get/set pre build steps
        # get/set post build steps
    # get/set transfer options
    
    def get_build_options(self):
        pass

    def get_transfer_options(self):
        pass


class _CPUPkgBuildOptions:

    def __init__(self, build_options_tree):
        self.tree = build_options_tree

    def set_build_options(self):
        raise NotImplementedError()

    def get_build_options(self):
        raise NotImplementedError()

    def get_gcc_version(self):
        raise NotImplementedError()

    def get_pre_build_steps(self):
        raise NotImplementedError()

    def set_pre_build_steps(self):
        raise NotImplementedError()

    def set_includes(self):
        raise NotImplementedError()

    def get_includes(self):
        raise NotImplementedError()


class _CPUPkgTransfer:

    def __init__(self, transfer_element):
        self.element = transfer_element

    def get_parameter(self, param_name):
        raise NotImplementedError()

    def set_parameter(self, param_name):
        raise NotImplementedError()

    def get_device_parameters(self):
        raise NotImplementedError()

    def set_device_parameters(self):
        raise NotImplementedError()

    def get_connection_parameters(self):
        raise NotImplementedError()

    def set_connection_parameters(self):
        raise NotImplementedError()

if __name__ == "__main__":
    pass
