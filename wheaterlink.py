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

    def get_stations(self):
        query_params = {
            "api-key": self.config["api_key"],
            "t": self.get_timestamp(),
        }
        query_params["api-signature"] = calculate_signature(self.config["api_secret"], query_params)
        return self.get_request(f"stations", params=query_params)

    def get_historic(self, station_id, start, end):
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
        return self.get_request(f"historic/{station_id}", params=query_params)
