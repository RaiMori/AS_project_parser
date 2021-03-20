class PIL_File:
    def __init__(self, prj_path):
        pass

    def get_pvi_parameters(self):
        raise NotImplementedError()

    def set_custom_pvi_parameters(self):
        raise NotImplementedError()

    def generate_pil(self):
        raise NotImplementedError()


class RUC_Transfer:
    def __init__(self, global_as_path, ruc_path):
        raise NotImplementedError()

    def generate_pil(self):
        raise NotImplementedError()

    def transfer(self):
        raise NotImplementedError()

    def _get_pvi_exe_path(self):
        raise NotImplementedError()
