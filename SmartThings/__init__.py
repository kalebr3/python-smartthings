"""
Python SmartThings

Classes
-------
SmartThings.Account

Methods
-------
Account.control_device(deviceId: str, capability: str, command: dict, arguments: dict)
    Sends a specific command to the specified device.
Account.execute_scene(sceneId: str)
    Executes the specified scene.
"""

from .Account import Account