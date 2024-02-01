import pytest
from dmidecode.parse import DMIParse
from os import path


@pytest.fixture
def content():
    dump_path = path.join(path.dirname(__file__), "tests/fixtures/dmidecode.txt")

    with open(dump_path) as f:
        return f.read()


def test_parse(content: str):
    expected = {
        0: [
            {
                "DMIType": 0,
                "DMISize": 24,
                "DMIName": "BIOS Information",
                "Vendor": "Google",
                "Version": "Google",
                "Release Date": "07/12/2023",
                "Address": "0xE8000",
                "Runtime Size": "96 kB",
                "ROM Size": "64 kB",
                "BIOS Revision": "1.0",
                "Characteristics": [
                    "BIOS characteristics not supported",
                    "Targeted content distribution is supported",
                ],
            }
        ],
        1: [
            {
                "DMIType": 1,
                "DMISize": 27,
                "DMIName": "System Information",
                "Manufacturer": "Google",
                "Product Name": "Google Compute Engine",
                "Version": "Not Specified",
                "Serial Number": "GoogleCloud-8EBFB6FCE14327F972567743E80E23DE",
                "UUID": "8ebfb6fc-e143-27f9-7256-7743e80e23de",
                "Wake-up Type": "Power Switch",
                "SKU Number": "Not Specified",
                "Family": "Not Specified",
            }
        ],
        2: [
            {
                "DMIType": 2,
                "DMISize": 15,
                "DMIName": "Base Board Information",
                "Manufacturer": "Google",
                "Product Name": "Google Compute Engine",
                "Version": "Not Specified",
                "Serial Number": "Board-GoogleCloud-8EBFB6FCE14327F972567743E80E23DE",
                "Asset Tag": "8EBFB6FC-E143-27F9-7256-7743E80E23DE",
                "Features": ["Board is a hosting board"],
                "Location In Chassis": "Not Specified",
                "Chassis Handle": "0x0099",
                "Type": "Motherboard",
                "Contained Object Handles": "0",
            }
        ],
        3: [
            {
                "DMIType": 3,
                "DMISize": 20,
                "DMIName": "Chassis Information",
                "Manufacturer": "Google",
                "Type": "Other",
                "Lock": "Not Present",
                "Version": "Not Specified",
                "Serial Number": "Not Specified",
                "Asset Tag": "Not Specified",
                "Boot-up State": "Safe",
                "Power Supply State": "Safe",
                "Thermal State": "Safe",
                "Security Status": "Unknown",
                "OEM Information": "0x00000000",
                "Height": "Unspecified",
                "Number Of Power Cords": "Unspecified",
            }
        ],
        4: [
            {
                "DMIType": 4,
                "DMISize": 32,
                "DMIName": "Processor Information",
                "Socket Designation": "CPU 1",
                "Type": "Central Processor",
                "Family": "Other",
                "Manufacturer": "Google",
                "ID": "10 0F 83 00 FF FB 8B 17",
                "Version": "Not Specified",
                "Voltage": "Unknown",
                "External Clock": "Unknown",
                "Max Speed": "2000 MHz",
                "Current Speed": "2000 MHz",
                "Status": "Populated, Enabled",
                "Upgrade": "Other",
                "L1 Cache Handle": "Not Provided",
                "L2 Cache Handle": "Not Provided",
                "L3 Cache Handle": "Not Provided",
            },
            {
                "DMIType": 4,
                "DMISize": 32,
                "DMIName": "Processor Information",
                "Socket Designation": "CPU 2",
                "Type": "Central Processor",
                "Family": "Other",
                "Manufacturer": "Google",
                "ID": "10 0F 83 00 FF FB 8B 17",
                "Version": "Not Specified",
                "Voltage": "Unknown",
                "External Clock": "Unknown",
                "Max Speed": "2000 MHz",
                "Current Speed": "2000 MHz",
                "Status": "Populated, Enabled",
                "Upgrade": "Other",
                "L1 Cache Handle": "Not Provided",
                "L2 Cache Handle": "Not Provided",
                "L3 Cache Handle": "Not Provided",
            },
            {
                "DMIType": 4,
                "DMISize": 32,
                "DMIName": "Processor Information",
                "Socket Designation": "CPU 3",
                "Type": "Central Processor",
                "Family": "Other",
                "Manufacturer": "Google",
                "ID": "10 0F 83 00 FF FB 8B 17",
                "Version": "Not Specified",
                "Voltage": "Unknown",
                "External Clock": "Unknown",
                "Max Speed": "2000 MHz",
                "Current Speed": "2000 MHz",
                "Status": "Populated, Enabled",
                "Upgrade": "Other",
                "L1 Cache Handle": "Not Provided",
                "L2 Cache Handle": "Not Provided",
                "L3 Cache Handle": "Not Provided",
            },
            {
                "DMIType": 4,
                "DMISize": 32,
                "DMIName": "Processor Information",
                "Socket Designation": "CPU 4",
                "Type": "Central Processor",
                "Family": "Other",
                "Manufacturer": "Google",
                "ID": "10 0F 83 00 FF FB 8B 17",
                "Version": "Not Specified",
                "Voltage": "Unknown",
                "External Clock": "Unknown",
                "Max Speed": "2000 MHz",
                "Current Speed": "2000 MHz",
                "Status": "Populated, Enabled",
                "Upgrade": "Other",
                "L1 Cache Handle": "Not Provided",
                "L2 Cache Handle": "Not Provided",
                "L3 Cache Handle": "Not Provided",
            },
        ],
        16: [
            {
                "DMIType": 16,
                "DMISize": 15,
                "DMIName": "Physical Memory Array",
                "Location": "Other",
                "Use": "System Memory",
                "Error Correction Type": "Multi-bit ECC",
                "Maximum Capacity": "16 GB",
                "Error Information Handle": "Not Provided",
                "Number Of Devices": "1",
            }
        ],
        17: [
            {
                "DMIType": 17,
                "DMISize": 21,
                "DMIName": "Memory Device",
                "Array Handle": "0x0200",
                "Error Information Handle": "Not Provided",
                "Total Width": "64 bits",
                "Data Width": "64 bits",
                "Size": "16 GB",
                "Form Factor": "DIMM",
                "Set": "None",
                "Locator": "DIMM 0",
                "Bank Locator": "Not Specified",
                "Type": "RAM",
                "Type Detail": "Synchronous",
            }
        ],
        19: [
            {
                "DMIType": 19,
                "DMISize": 15,
                "DMIName": "Memory Array Mapped Address",
                "Starting Address": "0x00000000000",
                "Ending Address": "0x000BFFFFFFF",
                "Range Size": "3 GB",
                "Physical Array Handle": "0x0200",
                "Partition Width": "1",
            },
            {
                "DMIType": 19,
                "DMISize": 15,
                "DMIName": "Memory Array Mapped Address",
                "Starting Address": "0x00100000000",
                "Ending Address": "0x0043FFFFFFF",
                "Range Size": "13 GB",
                "Physical Array Handle": "0x0200",
                "Partition Width": "1",
            },
        ],
        20: [
            {
                "DMIType": 20,
                "DMISize": 19,
                "DMIName": "Memory Device Mapped Address",
                "Starting Address": "0x00000000000",
                "Ending Address": "0x000BFFFFFFF",
                "Range Size": "3 GB",
                "Physical Device Handle": "0x7000",
                "Memory Array Mapped Address Handle": "0x0300",
                "Partition Row Position": "1",
            },
            {
                "DMIType": 20,
                "DMISize": 19,
                "DMIName": "Memory Device Mapped Address",
                "Starting Address": "0x00100000000",
                "Ending Address": "0x0043FFFFFFF",
                "Range Size": "13 GB",
                "Physical Device Handle": "0x7000",
                "Memory Array Mapped Address Handle": "0x0301",
                "Partition Row Position": "1",
            },
        ],
        32: [
            {
                "DMIType": 32,
                "DMISize": 11,
                "DMIName": "System Boot Information",
                "Status": "No errors detected",
            }
        ],
    }
    p = DMIParse(content)
    for num, exp in expected.items():
        assert p.get(num) == exp
        name = DMIParse.type2str.get(num)
        if name:
            assert p.get(name) == exp


def test_manufacturer(content: str):
    p = DMIParse(content)
    assert p.manufacturer() == "Google"


def test_model(content: str):
    p = DMIParse(content)
    assert p.model() == "Google Compute Engine"


def test_serial_number(content: str):
    p = DMIParse(content)
    assert p.serial_number() == "GoogleCloud-8EBFB6FCE14327F972567743E80E23DE"


def test_cpu_num(content: str):
    p = DMIParse(content)
    assert p.cpu_num() == 0


def test_total_enabled_cores(content: str):
    p = DMIParse(content)
    assert p.total_enabled_cores() == 0


def test_total_ram(content: str):
    p = DMIParse(content)
    assert p.total_ram() == 16


def test_firmware(content: str):
    p = DMIParse(content)
    assert p.firmware() == "n/a"
