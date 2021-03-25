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
        self.build_options = _CPUPkgBuildOptions(self._get_build_options_node())
        self.online_configuration = _CPUPkgOnlineConfig(self._get_online_config_node())

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

    def _get_build_options_node(self):
        return self.cpu_pkg_tree.find(f".//{{{self.ns}}}Configuration/{{{self.ns}}}Build")

    def _get_online_config_node(self):
        return self.cpu_pkg_tree.find(f".//{{{self.ns}}}Configuration/{{{self.ns}}}OnlineConfiguration")


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
        attrib = self.element.attrib["PreBuildStep"]
        return self._str_to_params_list(attrib)

    @pre_build_steps.setter
    def pre_build_steps(self, value):
        str_val = self._params_list_to_str(value)
        self.element.attrib["PreBuildStep"] = str_val

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

    @staticmethod
    def _str_to_params_list(param):
        lst = param.split()
        return lst

    @staticmethod
    def _params_list_to_str(params_list):
        return " ,".join(params_list)


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
        params_str = self.element.attrib["DeviceParameters"]
        return self._param2list(params_str)

    @device_parameters.setter
    def device_parameters(self, value):
        self.element.attrib["DeviceParameters"] = self._list_param2str(value)

    @property
    def connection_parameters(self):
        params_str = self.element.attrib["ConnectionParameters"]
        return self._param2list(params_str)

    @connection_parameters.setter
    def connection_parameters(self, value):
        self.element.attrib["ConnectionParameters"] = self._list_param2str(value)

    def _param2list(self, params: str):
        p_str_list = params.split()
        out_params = []
        for p in p_str_list:
            out_params.append(self._param_str2tuple(p))
        return out_params

    def _param_str2tuple(self, param):
        param_value_lst = param.split("=")
        par = param_value_lst[0].replace("/", "")
        val = param_value_lst[1]
        return par, val

    def _list_param2str(self, params):
        lst = []
        for p in params:
            lst.append(self._param_tuple2str(*p))
        return " ".join(lst)

    def _param_tuple2str(self, param, val):
        return f"/{param}={val}"



if __name__ == "__main__":
    cpu_pkg_path = r"C:\_projects\test-prj\Physical\ArSim\PC\Cpu.pkg"
    cpu = CPUPkgParser(cpu_pkg_path)
    a = _CPUPkgBuildOptions(cpu.cpu_pkg_tree)
    r = cpu.runtime_version
    print(r)
    cpu.runtime_version = "C4.90"
