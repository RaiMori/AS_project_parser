import re
from pathlib import Path
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


if __name__ == "__main__":
    pass
