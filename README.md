# py-dmidecode

Small tool that parses ouput of dmidecode command

## How to use
```python
from dmidecode import DMIParse
import subprocess

# run dmidecode and store its output
raw = subprocess.check_output("dmidecode", stderr=_subprocess.PIPE)

# create parsing instance by passing dmidecode output
dmi = DMIParse(raw)

# some of the pre-defined queries
print('Processor type: ', dmi.cpu_type())
print('Number of processors: ', dmi.cpu_num())
print('Cores count: ', dmi.total_cores())
print('Total RAM in GB: ', dmi.total_ram())
print('Serial number: ', dmi.serial_number())
print('Manufacturer: ', dmi.manufacturer())
print('Firmware: ', dmi.firmware())
```

Other information can be easily retrieved by analyzing dmi.data and module code.