import requests
import json


class ApiClient(object):
    def __init__(self, base_url=None, timeout=10, **kargs):
        self.__base_url = base_url
        self.timeout = timeout
        self.config = None

    def base_url(self):
        return self.__base_url

    def url_for(self, endpoint):
        if not endpoint.startswith("/"):
            endpoint = f"/{endpoint}"
        if endpoint.endswith("/"):
            endpoint = endpoint[:-1]

        return self.__base_url + endpoint

    def get_request(self, endpoint, params=None, headers=None):
        if headers is None:
            token = self.config.get("token", "")
            headers = {
                "Authorization": f"Bearer {token}",
            }

        return requests.get(
            self.url_for(endpoint), params=params, headers=headers, timeout=self.timeout
        )

    def post_request(self, endpoint, params=None, data=None, headers=None):
        if not isinstance(data, str):
            data = json.dumps(data)

        if headers is None:
            token = self.config.get("token", "")
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            }

        return requests.post(
            self.url_for(endpoint),
            params=params,
            data=data,
            headers=headers,
            timeout=self.timeout,
        )

    def put_request(self, endpoint, params=None, data=None, headers=None):
        if not isinstance(data, str):
            data = json.dumps(data)

        if headers is None:
            token = self.config.get("token", "")
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            }

        return requests.put(
            self.url_for(endpoint),
            params=params,
            data=data,
            headers=headers,
            timeout=self.timeout,
        )

    def delete_request(self, endpoint, params=None, data=None, headers=None):
        pass
