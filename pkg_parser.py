class Pkg_parser:
    def __init__(self, pkg_path):
        self.pkg_path = pkg_path

    def get_objects(self):
        raise NotImplementedError()


class CPUPkgParser:
    def __init__(self, path):
        self.path = path
