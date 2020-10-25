# Python SmartThings

| Version | Stage   |
| ------- | ------- |
|  1.0.0  | Release |

This purpose for the creation of this package is twofold. The main reason I
created this package is to be able to issue commands to my Z-Wave devices via
my SmartThings Hub from a RaspberryPi running Falcon Player software. The other
reason for the creation of this package is to further my knowledge of the Python
programming language.

## Dependencies

- Python >=3.7
- Packages
  - requests

## Installation

```
pip3 install python-smartthings
```

## How to Use

Import package to project.

```python
import SmartThings
```

Create an instance of a SmartThings account using your Personal Access Token.

> Vist [https://account.smartthings.com/tokens](https://account.smartthings.com/tokens)
> to create or revoke Personal Access Tokens.

```python
ST = SmartThings.Account(PERSONAL_ACCESS_TOKEN)
```

After creating an instance of the Account class, three dictionaries will be
created from API requests.

```python
ST.locations # {LOCATION_NAME:LOCATION_ID}
ST.devices   # {LOCATION_NAME:{DEVICE_NAME:DEVICE_ID}}
ST.scenes    # {LOCATION_NAME:{SCENE_NAME:SCENE_ID}}
```

These dictionaries can be used with the included methods to execute actions on
devices and scenes.

```python
ST.control_device(ST.devices[LOCATION_NAME][DEVICE_NAME], capability=None, command=None, arguments=None)
# Reference the SmartThings API documentation for information regarding the
# format of capabilities, commands, and arguments

ST.execute_scene(ST.scenes[LOCATION_NAME][DEVICE_NAME])
```