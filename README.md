# py-dmidecode

Small tool that parse the ouput of the dmidecode command

## How to use
```python
import dmidecode

# parse the full output
data = dmidecode.parse()

# request only a certain type
data = dmidecode.get_by_type(1)
```