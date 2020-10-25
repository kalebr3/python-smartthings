import requests


class Account:
    """
    Class for the creation of an instance of a SmartThings Account.

    Attributes
    ----------
    locations : dict
        Locations retrieved via the `_get_locations()` method.
    devices : dict
        Devices retrieved via the `_get_devices()` method.
    scenes : dict
        Scenes retrieved via the `_get_scenes()` method.

    Methods
    -------
    control_device(deviceId:str, capability:str, command:dict, arguments:dict)
        Sends a command to a specific device.
    execute_scene(sceneId:str)
        Executes the specified scene.
    """

    def __init__(self, token:str):
        """
        Constructor Method

        Parameters
        ----------
        token : str
            SmartThings Personal Access Token
        """

        print('Connecting to SmartThings Service...')
        self._token = token
        print('Retrieving Locations...')
        self.locations = self._get_locations()
        print('Retrieving Devices...')
        self.devices = self._get_devices()
        print('Retrieving Scenes...')
        self.scenes = self._get_scenes()
        print('Connected and Ready!')

    def _api_call(self, method:str, path:str, params:dict, data:dict) -> requests.Response:
        """
        Calls SmartThings API using given parameters.

        Parameters
        ----------
        method : str
            Type of http request. i.e. get, post
        path : str
            Relative path added to base url.
        params : dict
            Parameters passed to http request.
        data : dict
            Data passed to http request.

        Returns
        -------
        requests.Response
            Response from http request.

        Raises
        ------
        NotImplementedError
            Invalid value for parameter: method.
        """

        url = 'https://api.smartthings.com'
        headers = {
            'Accept': 'application/vnd.smartthings+json;v=1',
            'Authorization': f'Bearer {self._token}',
        }

        if method == 'get':
            response = requests.get(
                url + path,
                params=params,
                headers=headers,
                data=data,
            )
        elif method == 'post':
            response = requests.post(
                url + path,
                params=params,
                headers=headers,
                data=data,
            )
        else:
            raise NotImplementedError('INVALID VALUE FOR method ON FUCNTION _api_call')
        return response

    def _get_locations(self) -> dict:
        """
        Gets locations via `_api_call()`

        Returns
        -------
        dict
            Dictionary object populated with the locations retrieved.
        """

        _locations = {}
        response_json = self._api_call(
            method='get',
            path='/locations',
            params=None,
            data=None,
        ).json()
        for location in response_json['items']:
            _locations[location["name"]] = location["locationId"]
        return _locations

    def _get_devices(self) -> dict:
        """
        Gets devices via `_api_call()`

        Returns
        -------
        dict
            Dictionary object populated with the devices retrieved.
        """

        _devices = {}
        for location in self.locations:
            _temp = {}
            response_json = self._api_call(
                method='get',
                path='/devices',
                params={'locationId': self.locations[location]},
                data=None,
            ).json()
            for device in response_json['items']:
                _temp[device["label"]] = device["deviceId"]
            _devices[location] = _temp
        return _devices

    def _get_scenes(self) -> dict:
        """
        Gets scenes via `_api_call()`

        Returns
        -------
        dict
            Dictionary object populated with the scenes retrieved.
        """

        _scenes = {}
        for location in self.locations:
            _temp = {}
            response_json = self._api_call(
                method='get',
                path='/scenes',
                params={'locationId': self.locations[location]},
                data=None,
            ).json()
            for scene in response_json['items']:
                _temp[scene['sceneName']] = scene['sceneId']
            _scenes[location] = _temp
        return _scenes

    def control_device(self, deviceId:str, capability:str, command:dict, arguments:dict):
        """
        Sends a comand to a specified device.

        Parameters
        ----------
        deviceId : str
            The unique identifier of the device to control.
            Can be the identifier passed in as a string, or called via the
            `locations` dictionary.
        capability : str
            The device capability to control.
        command : dict
            The command to send to the device.
        arguments : dict
            Any additional arguments required by the capability controlled.
        """

        response = self._api_call(
            method='post',
            path=f'/devices/{deviceId}/commands',
            params=None,
            data={
                'capability': capability,
                'command': command,
                'arguments': arguments,
            },
        )
        return response.raise_for_status()

    def execute_scene(self, sceneId:str):
        """
        Executes the specified scene.

        Parameters
        ----------
        sceneId : str
            The unique identifier of the scene to execute.
            Can be the identifier passed in as a string, or referenced via the
            `scenes` dictionary.
        """

        response = self._api_call(
            method='post',
            path=f'/scenes/{sceneId}/execute',
            params=None,
            data=None,
        )
        return response.raise_for_status()
