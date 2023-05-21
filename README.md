# py-dmidecode

Small tool that parses output of dmidecode command

## How to use

```python
from dmidecode import DMIDecode
import subprocess

# create parsing instance by passing dmidecode output
dmi = DMIDecode()

# some of the pre-defined queries
print('Manufacturer:\t', dmi.manufacturer())
print('Model:\t\t', dmi.model())
print('Firmware:\t', dmi.firmware())
print('Serial number:\t', dmi.serial_number())
print('Processor type:\t', dmi.cpu_type())
print('Number of CPUs:\t', dmi.cpu_num())
print('Cores count:\t', dmi.total_enabled_cores())
print('Total RAM:\t{} GB'.format(dmi.total_ram()))
```

Alternatively instead of running dmidecode locally you can use DMIParse by passing dmidecode output as an argument:

```python
from dmidecode import DMIParse
dmi = DMIParse(raw)
```

Other information can be easily retrieved by analyzing dmi.data and module code.

## Possible limitations

Tested with dmidecode versions 2.11, 2.12 and 3.2
