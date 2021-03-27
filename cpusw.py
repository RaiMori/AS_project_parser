from lxml import etree
from typing import List, Dict


class Task:

    def __init__(self, name, source, memory, language, debugging, disable):
        self.name = name
        self.source = source
        self.memory = memory
        self.language = language
        self.debugging = debugging
        self.disable = disable


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

    def get_libraries(self) -> List:
        pass

    def add_library(self) -> None:
        pass

    def get_binaries(self) -> List:
        pass

    def add_binary(self) -> None:
        pass

    def _get_task_classes_nodes(self) -> List:
        return self.cpusw_tree.findall(f".//{{{self.ns}}}TaskClass")

    def _get_task_elem(self, task_class_elem: etree.Element) -> List:
        return task_class_elem.findall(f".//{{{self.ns}}}Task")

    def _get_binaries(self) -> List:
        return self.cpusw_tree.findall(f"./{{{self.ns}}}Binaries/{{{self.ns}}}BinaryObject")

    def _get_libraries_node(self) -> List:
        return self.cpusw_tree.findall(f"./{{{self.ns}}}Libraries/{{{self.ns}}}LibraryObject")
