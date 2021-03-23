from lxml import etree

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
    ns = "http://br-automation.co.at/AS/Cpu"
    def __init__(self, cpu_pkg_path):
        self.path = cpu_pkg_path
        self.cpu_pkg_tree = etree.parse(cpu_pkg_path)

    def get_option(self, options_name):
        raise NotImplementedError()

    def set_option(self, options_name, value):
        raise NotImplementedError()

    @property
    def runtime_version(self):
        return self._get_runtime_version_node().attrib["Version"]

    @runtime_version.setter
    def runtime_version(self, val):
        if isinstance(val, str):
            self._get_runtime_version_node().attrib["Version"] = val
            self.cpu_pkg_tree.write(open(self.path, "wb"), pretty_print=True)
            #etree.write(self.path, etree.tostring(self.cpu_pkg_tree, pretty_print=True))
        else:
            raise TypeError("Runtime version should be a string value")

    def _get_runtime_version_node(self):
        return self.cpu_pkg_tree.find(f".//{{{self.ns}}}Configuration/{{{self.ns}}}AutomationRuntime")


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
    ns = CPUPkgParser.ns
    def __init__(self, build_options_tree: etree.ElementTree):
        self.element = build_options_tree

    @property
    def build_options(self):
        return self.element.attrib["AnsicAdditionalBuildOptions"]

    @build_options.setter
    def get_build_options(self, value):
        self.element.attrib["AnsicAdditionalBuildOptions"] = value

    @property
    def gcc_version(self):
        return self.element.attrib["GccVersion"]

    @gcc_version.setter
    def gcc_version(self, value):
        self.element.attrib["GccVersion"] = value
    
    @property
    def pre_build_steps(self):
        return self.element.attrib["PreBuildStep"]

    @pre_build_steps.setter
    def pre_build_steps(self, value):
        self.element.attrib["PreBuildStep"] = value

    @property
    def post_build_steps(self):
        return self.element.attrib["PostBuildStep"]

    @post_build_steps.setter
    def post_build_steps(self, value):
        self.element.attrib["PostBuildStep"] = value

    @property
    def additionsl_includes(self):
        return self.element.attrib["AnsicIncludeDirectories"]

    @additionsl_includes.setter
    def additional_includes(self, value):
        self.element.attrib["AnsicIncludeDirectories"] = value


class _CPUPkgOnlineConfig:
    ns = CPUPkgParser.ns
    def __init__(self, online_config_element):
        self.element = online_config_element

    @property
    def name(self):
        return self.element.attrib["Name"]

    @name.setter
    def name(self, value):
        self.element.attrib["Name"] = value

    @property
    def device_type(self):
        return self.element.attrib["DeviceType"]

    @device_type.setter
    def device_type(self, value):
        self.element.attrib["DeviceType"] = value

    @property
    def device_parameters(self):
        return self.element.attrib["DeviceParameters"]

    @device_parameters.setter
    def device_parameters(self, value):
        self.element.attrib["DeviceParameters"] = value

    @property
    def connection_parameters(self):
        return self.element.attrib["ConnectionParameters"]

    @connection_parameters.setter
    def connection_parameters(self, value):
        self.element.attrib["ConnectionParameters"] = value



if __name__ == "__main__":
    cpu_pkg_path = r"C:\_projects\test-prj\Physical\ArSim\PC\Cpu.pkg"
    cpu = CPUPkgParser(cpu_pkg_path)
    a = _CPUPkgBuildOptions(cpu.cpu_pkg_tree)
    r = cpu.runtime_version
    print(r)
    cpu.runtime_version = "C4.90"
