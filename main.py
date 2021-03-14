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


class AS_Build:
    
    def __init__(self, as_path, apj_path, build_type="Rebuild", generate_ruc=True, simulation=True):
        self.as_path = as_path
        self.apj_path = apj_path
        self.build_type = build_type
        self.generate_ruc = generate_ruc
        self.simulation = simulation

    def build():
        pass

    def _get_as_builder_path(self):
        pass


class PIL_File:

    def __init__(self):
        pass

    def get_pvi_parameters(self):
        pass

    def generate_pil(self):
        pass


class RUC_Transfer:

    def __init__(self):
        pass

    def generate_pil(self):
        pass

    def transfer(self):
        pass

    