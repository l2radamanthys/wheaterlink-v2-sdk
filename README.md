# Wheaterlink V2 API

Unoficial [Wheaterlink V2 API](https://weatherlink.github.io/v2-api/api-reference) Client

Usage:

    from wheaterlink import WLClient

    client = WLClient(api_key, api_secret)

    stations = client.get_stations()

    station_id = 129681
    start = datetime.datetime.strptime("20/02/2022 00:00:00", "%d/%m/%Y %H:%M:%S")
    end = start + relativedelta(days=1)

    data = client.get_historic(station_id, start, end)


Availabled method list:

## Methadata

- `WLClient.get_stations(raw_content=False)`
- `WLClient.get_sensors(raw_content=False)`
- `WLClient.get_sensor_activity(raw_content=False)`
- `WLClient.get_sensor_catalog(sensor_type=None, raw_content=False)`

### Wheather Data

- `WLClient.get_historic(station_id, start, end, raw_content=False)`

