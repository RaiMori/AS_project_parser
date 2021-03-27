from pathlib import Path


class ASHWConfiguration:

    def __init__(self, cfg_dir, cfg_name):
        self.cfg_dir = cfg_dir
        self.name = cfg_name

    def build(self):
        raise NotImplementedError()

    def transfer(self):
        raise NotImplementedError()

    def _get_cpu_pkg(self):
        raise NotImplementedError()

    def _get_cpu_sw(self):
        raise NotImplementedError()

    def _get_config_pkg(self):
        raise NotImplementedError()