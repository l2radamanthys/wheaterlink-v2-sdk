from .client import ApiClient
import datetime
import math


API_URL = "https://api.weatherlink.com/v2"


class WLClient(ApiClient):
    def __init__(self, api_key, api_secret, timeout=600):
        super(WLClient, self).__init__(base_url=API_URL, timeout=timeout)
        self.config = {
            "base_url": API_URL,
            "api_key": api_key,
            "api_secret": api_secret
        }

    def _date_to_timestamp(self, date_):
        return math.trunc(date_.timestamp())

    def timestamp_to_date(self, ts):
        return datetime.fromtimestamp(ts)

    def get_timestamp(self):
        return self._date_to_timestamp(datetime.datetime.now())

    @property
    def base_query_params(self):
        query_params = {
            "api-key": self.get_config("api_key"),
        }
        return query_params

    def get_stations(self, raw_content=False):
        response = self.get_request(f"stations", params=self.base_query_params)
        if raw_content:
            return response
        elif response.status_code == 200:
            return response.json().get("stations")
        else:
            return response.json()

    def get_sensors(self, raw_content=False):
        response = self.get_request(f"sensors", params=self.base_query_params)
        if raw_content:
            return response
        elif response.status_code == 200:
            return response.json().get("sensors")
        else:
            return response.json()

    def get_sensor_activity(self, raw_content=False):
        response = self.get_request(f"sensors-activity", params=self.base_query_params)
        if raw_content:
            return response
        elif response.status_code == 200:
            return response.json().get("sensor-activity")
        else:
            return response.json()

    def get_sensor_catalog(self, sensor_type=None, raw_content=False):
        response = self.get_request(f"sensor-catalog", params=self.base_query_params)
        if raw_content:
            return response
        elif response.status_code == 200:
            data = response.json().get("sensor_types")
            if sensor_type != None:
                return next(filter(lambda x: x["sensor_type"] == sensor_type, data), None)
            return data
        else:
            return response.json()

    def get_historic(self, station_id, start, end, raw_content=False):
        start_ts = self._date_to_timestamp(start)
        end_ts = self._date_to_timestamp(end)
        query_params = {
            "api-key": self.get_config("api_key"),
            "end-timestamp": end_ts,
            "start-timestamp": start_ts,
        }
        response = self.get_request(f"historic/{station_id}", params=query_params)
        if raw_content:
            return response
        elif response.status_code == 200:
            return response.json().get("sensors")[0]["data"]
        else:
            return response.json()
