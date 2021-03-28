from lxml import etree
from typing import List, Dict, Any


class SWObject:

    @classmethod
    def from_element(cls, elem: etree.Element) -> 'SWObject':
        name = elem.attrib["Name"]
        src = elem.attrib["Source"]
        mem = elem.attrib["Memory"]
        lang = elem.attrib["Language"]
        debug = elem.attrib.get("Debugging","False")
        disable = elem.attrib.get("Disable", "False")

        return SWObject(name, src, mem, lang, debug, disable)

    def __init__(self, name, source, memory="UserROM", language="ANSIC", debugging="True", disable="False"):
        self.name = name
        self.source = source
        self.memory = memory
        self.language = language
        self.debugging = debugging
        self.disable = disable

    def as_dict(self) -> Dict[str, Any]:
        return dict(name=self.name,
                    source=self.source,
                    memory=self.memory,
                    language=self.language,
                    debugging=self.debugging,
                    disable=self.disable
                    )

class TaskClass:
    ns = "http://br-automation.co.at/AS/SwConfiguration"
    def __init__(self, tk_element):
        self.element = tk_element
        self.name = self.element.attrib["Name"]
        self.tasks = self._get_tasks()

    def as_dict(self):
        tasks_list = []
        for t in self.tasks:
            tasks_list.append(t.as_dict())
        return {self.name: tasks_list}

    def _get_tasks(self, as_dict=False):
        tasks_elems = self.element.findall(f".//{{{self.ns}}}Task")
        tasks = []
        for t in tasks_elems:
            task = SWObject.from_element(t)
            if as_dict:
                tasks.append(task.as_dict())
            else:
                tasks.append(task)
        return tasks




class CpuSw:
    ns = "http://br-automation.co.at/AS/SwConfiguration"

    def __init__(self, cpusw_file):
        self.path = cpusw_file
        self.cpusw_tree = etree.parse(cpusw_file)

    def get_task_classes(self):
        pass

    def get_tasks(self, task_class: str) -> Dict:
        pass

    def get_task(self, task_name: str, task_class: str = "") -> Dict:
        pass

    def add_task(self, task_class, task_name):
        pass

    def get_libraries(self, as_dict=False) -> List:
        return self._get_swobject("libraries", as_dict=as_dict)

    def add_library(self) -> None:
        pass

    def get_binaries(self, as_dict=False) -> None:
        return self._get_swobject("binaries", as_dict=as_dict)

    def _get_swobject(self, otype: str, as_dict=False) -> List:
        if otype == 'binaries':
            get_obj = self._get_binaries_node
        elif otype == 'libraries':
            get_obj = self._get_libraries_node
        elif otype == 'task':
            get_obj == self._get_task_classes_nodes
        b_nodes = get_obj()
        binaries_list = []
        for i in b_nodes:
            obj = SWObject.from_element(i)
            if as_dict:
                obj = obj.as_dict()
            binaries_list.append(obj)
        return binaries_list

    def add_binary(self) -> None:
        pass

    def _get_task_classes_nodes(self) -> List:
        return self.cpusw_tree.findall(f".//{{{self.ns}}}TaskClass")

    def _get_task_nodes(self, task_class_elem: etree.Element) -> List:
        return task_class_elem.findall(f".//{{{self.ns}}}Task")

    def _get_binaries_node(self) -> List:
        return self.cpusw_tree.findall(f"./{{{self.ns}}}Binaries/{{{self.ns}}}BinaryObject")

    def _get_libraries_node(self) -> List:
        return self.cpusw_tree.findall(f"./{{{self.ns}}}Libraries/{{{self.ns}}}LibraryObject")


if __name__ == "__main__":
    cpusw_path = r"C:\_projects\test-prj\Physical\ArSim\PC\Cpu.sw"
    sw = CpuSw(cpusw_path)
    print([i for i in sw.get_binaries(as_dict=True)])
    a = sw.get_libraries(as_dict=True)
    print('')
