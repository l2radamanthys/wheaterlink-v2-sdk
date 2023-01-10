from client import ApiClient
from calculate_signature import calculate_signature
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

    def __date_to_timestamp(self, date_):
        return math.trunc(date_.timestamp())

    def timestamp_to_date(self, ts):
        return datetime.fromtimestamp(ts)

    def get_timestamp(self):
        return self.__date_to_timestamp(datetime.datetime.now())

    @property
    def base_query_params(self):
        query_params = {
            "api-key": self.config["api_key"],
            "t": self.get_timestamp(),
        }
        query_params["api-signature"] = calculate_signature(self.config["api_secret"], query_params)
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

    def get_sensor_catalog(self, raw_content=False):
        response = self.get_request(f"sensors-catalog", params=self.base_query_params)
        if raw_content:
            return response
        elif response.status_code == 200:
            return response.json().get("sensor_types")
        else:
            return response.json()

    def get_historic(self, station_id, start, end, raw_content=False):
        start_ts = self.__date_to_timestamp(start)
        end_ts = self.__date_to_timestamp(end)
        query_params = {
            "api-key": self.config["api_key"],
            "end-timestamp": end_ts,
            "start-timestamp": start_ts,
            "station-id":station_id,
            "t": self.get_timestamp(),
        }
        query_params["api-signature"] = calculate_signature(self.config["api_secret"], query_params)
        del query_params["station-id"]
        response = self.get_request(f"historic/{station_id}", params=query_params)
        if raw_content:
            return response
        elif response.status_code == 200:
            return response.json().get("sensors")[0]["data"]
        else:
            return response.json()