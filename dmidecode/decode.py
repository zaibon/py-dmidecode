import subprocess

from dmidecode.parse import DMIParse


class DMIDecode(DMIParse):
    """Wrapper over DMIParse which runs dmidecode locally"""

    def __init__(self, command="dmidecode"):
        self.dmidecode = command
        raw = self._run()
        super().__init__(raw)

    def _run(self):
        # let subprocess merge stderr with stdout
        with subprocess.Popen(self.dmidecode, stderr=subprocess.STDOUT, stdout=subprocess.PIPE) as proc:
            stdout, _ = proc.communicate()
            if proc.returncode > 0:
                raise RuntimeError("{} failed with an error:\n{}".format(self.dmidecode, stdout.decode()))
            else:
                return stdout.decode()
