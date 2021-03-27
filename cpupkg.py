from typing import List, Tuple, Union

from lxml import etree

# HW Configuration managment


class PhysicalParser:
    """ Parse physical directory to get available HW configurations """


class PhysicalCfgPkgParser:
    """ Get CPU folder for current hw configuration """

    def __init__(self, physical_path):
        self.path = physical_path

    def _read_hw_configs(self):
        pass

    def get_hw_configs(self) -> List:
        pass


class CPUPkgParser:
    ns = "http://br-automation.co.at/AS/Cpu"

    def __init__(self, cpu_pkg_path):
        self.path = cpu_pkg_path
        self.cpu_pkg_tree = etree.parse(cpu_pkg_path)
        self.build_options = _CPUPkgBuildOptions(self._get_build_options_node())
        self.online_configuration = _CPUPkgOnlineConfig(self._get_online_config_node())
        self.transfer = _TransferOptions(self._get_transfer_node())

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
        else:
            raise TypeError("Runtime version should be a string value")

    def _get_runtime_version_node(self):
        return self.cpu_pkg_tree.find(
            f".//{{{self.ns}}}Configuration/{{{self.ns}}}AutomationRuntime"
        )

    def _get_build_options_node(self):
        return self.cpu_pkg_tree.find(
            f".//{{{self.ns}}}Configuration/{{{self.ns}}}Build"
        )

    def _get_online_config_node(self):
        return self.cpu_pkg_tree.find(
            f".//{{{self.ns}}}Configuration/{{{self.ns}}}OnlineConfiguration"
        )

    def _get_transfer_node(self):
        return self.cpu_pkg_tree.find(f".//{{{self.ns}}}Configuration/{{{self.ns}}}Transfer")

    def _write_to_file(self) -> None:
        self.cpu_pkg_tree.write(open(self.path, "wb"), pretty_print=True)

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

    def __init__(self, build_options_tree: etree.ElementTree) -> None:
        self.element = build_options_tree

    @property
    def build_options(self) -> str:
        attrib = self.element.attrib["AnsicAdditionalBuildOptions"]
        return attrib

    @build_options.setter
    def build_options(self, value: str) -> None:
        self.element.attrib["AnsicAdditionalBuildOptions"] = value

    @property
    def gcc_version(self) -> str:
        return self.element.attrib["GccVersion"]

    @gcc_version.setter
    def gcc_version(self, value: str) -> None:
        self.element.attrib["GccVersion"] = value

    @property
    def pre_build_steps(self) -> str:
        return self.element.attrib["PreBuildStep"]

    @pre_build_steps.setter
    def pre_build_steps(self, value: str) -> None:
        self.element.attrib["PreBuildStep"] = value

    @property
    def post_build_steps(self) -> str:
        return self.element.attrib["PostBuildStep"]

    @post_build_steps.setter
    def post_build_steps(self, value: str) -> None:
        self.element.attrib["PostBuildStep"] = value

    @property
    def additional_includes(self) -> List[str]:
        attrib = self.element.attrib["AnsicIncludeDirectories"]
        return self._str_to_params_list(attrib)

    @additional_includes.setter
    def additional_includes(self, value: List[str]) -> None:
        str_val = self._params_list_to_str(value)
        self.element.attrib["AnsicIncludeDirectories"] = str_val

    @staticmethod
    def _str_to_params_list(param: str) -> List[str]:
        lst = param.split()
        return lst

    @staticmethod
    def _params_list_to_str(params_list: List[str]) -> str:
        return ", ".join(params_list)


class _CPUPkgOnlineConfig:
    ns = CPUPkgParser.ns

    def __init__(self, online_config_element: etree.Element):
        self.element = online_config_element

    @property
    def name(self) -> str:
        return self.element.attrib["Name"]

    @name.setter
    def name(self, value: str) -> None:
        self.element.attrib["Name"] = value

    @property
    def device_type(self) -> str:
        return self.element.attrib["DeviceType"]

    @device_type.setter
    def device_type(self, value: str) -> None:
        self.element.attrib["DeviceType"] = value

    @property
    def device_parameters(self) -> str:
        return self.element.attrib["DeviceParameters"]

    @device_parameters.setter
    def device_parameters(self, value: str) -> None:
        self.element.attrib["DeviceParameters"] = value

    def get_device_params_list(self) -> List[Tuple[str, str]]:
        params_str = self.element.attrib["DeviceParameters"]
        return self._param2list(params_str)

    def set_device_params_list(self, value: List[Tuple[str, str]]) -> None:
        if isinstance(value, List):
            self.element.attrib["DeviceParameters"] = self._list_param2str(value)
        else:
            raise TypeError("Connection parameters should be a list.")

    @property
    def connection_parameters(self) -> str:
        return self.element.attrib["ConnectionParameters"]

    @connection_parameters.setter
    def connection_parameters(self, value: str) -> None:
        self.element.attrib["ConnectionParameters"] = value

    def get_connection_params_list(self) -> List[Tuple[str, str]]:
        params_str = self.element.attrib["ConnectionParameters"]
        return self._param2list(params_str)

    def set_connection_params_list(self, value: List[Tuple[str, str]]) -> None:
        if isinstance(value, List):
            self.element.attrib["ConnectionParameters"] = self._list_param2str(value)
        else:
            raise TypeError("Connection parameters should be a list.")

    def _param2list(self, params: str) -> List[Tuple[str, str]]:
        p_str_list = params.split()
        out_params = []
        for p in p_str_list:
            out_params.append(self._param_str2tuple(p))
        return out_params

    def _param_str2tuple(self, param: str) -> Tuple[str, str]:
        param_value_lst = param.split("=")
        par = param_value_lst[0].replace("/", "")
        val = param_value_lst[1]
        return par, val

    def _list_param2str(self, params: List[Tuple[str, str]]) -> str:
        lst = []
        for p in params:
            lst.append(self._param_tuple2str(*p))
        return " ".join(lst)

    def _param_tuple2str(self, param: str, val: str) -> str:
        return f"/{param}={val}"


BOOL_VALUES = [True, False]

class _TransferOptions:

    str2bool = {"True": True, "False": False}
    bool2str = {True: "True", False: "False"}

    attributes = [{"name": 'AddToUserPart', "type": bool, "allowed_vals": ""},
                  {"name": 'AdditionalUserDir', "type": str, "allowed_vals": ""},
                  {"name": 'AllowDowngrade', "type": bool, "allowed_vals": ""},
                  {"name": 'AllowInitialTransfer', "type": bool, "allowed_vals": ""},
                  {"name": 'AllowPartitioning', "type": bool, "allowed_vals": ""},
                  {"name": 'ExecuteInitExitProgram', "type": bool, "allowed_vals": ""},
                  {"name": 'ForceInitialTransfer', "type": bool, "allowed_vals": ""},
                  {"name": 'IdentificationTypeValue', "type": str, "allowed_vals": ""},
                  {"name": 'IgnoreVersion', "type": bool, "allowed_vals": ""},
                  {"name": 'KeepNonVolatileMemory', "type": bool, "allowed_vals": ""},
                  {"name": 'ModuleSystemForPip', "type": str, "allowed_vals": ""},
                  {"name": 'PreserveVariableValues', "type": bool, "allowed_vals": ""},
                  {"name": 'ProjectConsistent', "type": bool, "allowed_vals": ""},
                  {"name": 'RebootDuringTransfer', "type": bool, "allowed_vals": ""},
                  {"name": 'RunUnitTestsAfterTransfer', "type": bool, "allowed_vals": ""},
                  {"name": 'TargetIdentificationType', "type": str, "allowed_vals": ""},
                  {"name": 'TryToBootInRunMode', "type": bool, "allowed_vals": ""},
                  {"name": 'UserFilesIgnoreDifference', "type": bool, "allowed_vals": ""},
                  ]

    def __init__(self, transfer_elem: etree.Element) -> None:
        self.atrbs_dict = {a['name']:a for a in self.attributes}
        
        self.element = transfer_elem

    def __getattr__(self, name):
        return self._get_attrib(name)

    def __dir__(self):
        return dir(_TransferOptions) + list(self.atrbs_dict.keys())

    def _get_attrib(self, name: str) -> 'Union[str, bool]':
        atrb = self.atrbs_dict.get(name, None)
        if atrb:
            value =  self._get_param_value(name)
            if atrb["type"] == bool:
                return self.str2bool[value]
            else:
                return value

    def _set_attrib(self, val):
        pass

    def _get_param_value(self, value: str) -> str:
        return self.element.attrib[value]



if __name__ == "__main__":
    cpu_pkg_path = r"C:\_projects\test-prj\Physical\ArSim\PC\Cpu.pkg"
    cpu = CPUPkgParser(cpu_pkg_path)
    a = _CPUPkgBuildOptions(cpu.cpu_pkg_tree)
    r = cpu.runtime_version
    print(r)
    cpu.online_configuration.device_type
    cpu.online_configuration.device_parameters
    cpu.online_configuration.connection_parameters

    cpu.online_configuration.set_device_params_list(
        [("IF", "opcua"), ("LOPO", "8082"), ("SA", "2805")]
    )
