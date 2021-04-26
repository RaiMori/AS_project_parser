from pathlib import Path

class GlobalASInstallation:

    def __init__(self, global_as_path):
        self.global_path = Path(global_as_path)

    def get_installed_as_versions(self):
        ver_dirs = self.global_path.glob("/AS[0-9]*/")
        for v in ver_dirs:
            yield v.name

    def get_as_path(self, version):
        if version in self.get_installed_as_versions():
            as_path = self.global_path / version
        else:
            raise ValueError(f"AS version {version} doesn't exist")

    def get_pvi_transfer(self, version):
        pvi_transfer_path = self._get_pvi_dir(version) / "PVI" / "Tools" / "PVITranafer" / "PVITransfer.exe"
        if pvi_transfer_path.is_file():
            return pvi_transfer_path
        else:
            raise ValueError(f"PVITransfer.exe for {version} doesn't exist")

    def _get_pvi_dir(self, version):
        pvi_dir = self._get_global_pvi_dir() / version
        if pvi_dir.is_dir():
            return pvi_dir
        else:
            raise ValueError(f"PVI version {version} doen't exist")

    def _get_common_as_dir(self):
        return self.global_path / "AS"


    def _get_as_path(self):
        pass

    def _get_global_pvi_dir(self):
        return self.global_path.joinpath("PVI")


g = GlobalASInstallation("C:/BrAutomation/")

print("")

class ASInstallation:
    def __init__(self, installation_path):
        self.path = installation_path

    def get_as_builder(self):
        pass

    def get_gcc_dir(self):
        pass

    def get_upgrades_list(self):
        pass
