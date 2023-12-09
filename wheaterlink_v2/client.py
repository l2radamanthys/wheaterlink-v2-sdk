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

    def get_config(self, key, default=None):
        return self.config.get(key, default)
    
    def get_default_headers(self):
        api_secret = self.get_config("api_secret", "")
        headers = {
            "X-Api-Secret": api_secret,
            "Content-Type": "application/json",
        }
        return headers

    def get_request(self, endpoint, params=None, headers=None):
        if headers is None:
            headers = self.get_default_headers()
            
        return requests.get(
            self.url_for(endpoint),
            params=params,
            headers=headers,
            timeout=self.timeout
        )

    def post_request(self, endpoint, params=None, data=None, headers=None):
        if not isinstance(data, str):
            data = json.dumps(data)

        if headers is None:
            headers = self.get_default_headers()

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
            headers = self.get_default_headers()

        return requests.put(
            self.url_for(endpoint),
            params=params,
            data=data,
            headers=headers,
            timeout=self.timeout,
        )

    def delete_request(self, endpoint, params=None, data=None, headers=None):
        if headers is None:
            headers = self.get_default_headers()
            
        return requests.delete(
            self.url_for(endpoint),
            params=params,
            headers=headers,
            timeout=self.timeout
        )
