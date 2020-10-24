import requests


class Account:

    def __init__(self, token:str):
        """Constructor Method

        :param token: SmartThings Personal Access Token
        :type token: str
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
        """Calls the SmartThings API with given parameters

        :param method: Type of request i.e. get, post
        :type method: str
        :param path: Relative path added to main url
        :type path: str
        :param params: Parameters passed to the http request
        :type params: dict
        :param data: Data passed to the http request
        :type data: dict
        :raises NotImplementedError: Invalid value for the parameter: method
        :return: Response object from http request
        :rtype: requests.Response
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
                _temp[device["name"]] = device["deviceId"]
            _devices[location] = _temp
        return _devices

    def _get_scenes(self) -> dict:
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

    def command_device(self, deviceId:str, capability:str, command:dict, arguments:dict):
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
        response = self._api_call(
            method='post',
            path=f'/scenes/{sceneId}/execute',
            params=None,
            data=None,
        )
        return response.raise_for_status()
