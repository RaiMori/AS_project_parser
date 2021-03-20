import re
import subprocess
from pathlib import Path


class AS_Build:
    """ Build BR Automation Studio project """

    def __init__(
        self,
        as_path,
        apj_path,
        configuration,
        rebuild=True,
        generate_ruc=True,
        force_simulation=True,
        clean_all=False,
        clean_temp=False,
        clean_binary=False,
        clean_generated=False,
        clean_diagnosis=False,
        profile=False,
    ):
        self.as_path = as_path
        self.apj_path = self._check_as_prj_path(apj_path)
        self.config = configuration
        self.rebuild = rebuild
        self.generate_ruc = generate_ruc
        self.force_simulation = force_simulation
        self.clean_all = clean_all
        self.clean_temp = clean_temp
        self.clean_binary = clean_binary
        self.clean_generated = clean_generated
        self.clean_diagnosis = clean_diagnosis
        self.profile = profile

    def build(self):
        args = self.get_argumants()
        out = subprocess.run(
            [self._get_as_builder_path(), *args],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out.check_returncode()
        return out.stdout

    def get_argumants(self):
        args_list = []
        args_list.append(self.apj_path)
        args_list.extend(["-c", self.config])

        # Build mode
        args_list.append("-buildMode")
        if self.rebuild:
            args_list.append("Rebuild")
        else:
            args_list.append("Build")

        # Build RUC Package for project transfer
        if self.generate_ruc:
            args_list.append("-buildRUCPackage")

        # Build for simulation
        if self.force_simulation:
            args_list.append("-simulation")

        # Cleanup options
        if self.clean_all:
            args_list.append("-cleanAll")

        if self.clean_temp:
            args_list.append("-clean-temporary")

        if self.clean_binary:
            args_list.append("-clean-binary")

        if self.clean_diagnosis:
            args_list.append("-clean-diagnosis")

        if self.profile:
            args_list.append("-profile")

        return args_list

    @staticmethod
    def parse_log(build_log):
        parser = BuildLogParser(build_log)
        result = parser.parse()
        return result

    def _get_prj_path(self):
        raise NotImplementedError()

    @staticmethod
    def _check_as_prj_path(path):
        if not Path(path).is_file():
            raise FileNotFoundError(
                "AS project file(.apj) not found. Check path to AS project"
            )
        return path

    def _get_as_builder_path(self):
        as_builder_path = Path(self.as_path).joinpath(r"Bin-En\BR.AS.Build.exe")
        if not as_builder_path.is_file():
            raise FileNotFoundError(
                "BR.AS.Build.exe doesn't exist. Check path to AS installation dir"
            )
        return str(as_builder_path)


class BuildLogParser:
    def __init__(self, log):
        self.log = log

    def parse(self):
        results = self.get_results()
        return results

    def _get_issue_pattern(self, issue_name):
        return re.compile(f".*{issue_name} \\d*:.*")

    def get_all_warnings(self):
        pattern = self._get_issue_pattern("warning")
        warnings = re.findall(pattern, self.log)
        return warnings

    def get_all_errors(self):
        pattern = self._get_issue_pattern("error")
        errors = re.findall(pattern, self.log)
        return errors

    def get_results(self):
        errors = self.get_all_errors()
        warnings = self.get_all_warnings()
        results = {
            "errors_num": len(errors),
            "warnings_num": len(warnings),
            "errors": errors,
            "warnings": warnings,
        }
        return results


if __name__ == "__main__":
    as_path = r"C:\APPL\BrAutomation\AS49"
    prj_path = r"C:\_Git\plc-framework"
    builder = AS_Build(as_path, prj_path, "ArSim")
    builder.build()
