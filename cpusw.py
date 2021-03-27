from lxml import etree

class Task:

    def __init__(self, name, source, memory, language, debugging, disable):
        self.name = name
        self.source = source
        self.memory = memory
        self.language = language
        self.debugging = debugging
        self.disable = disable


class CpuSw:

    def __init__(self):
        pass

    def _get_task_classes_trees(self):
        pass

    def _get_task_elem(self):
        pass

    def get_binaries(self):
        pass

    def get_libraries(self):
        pass