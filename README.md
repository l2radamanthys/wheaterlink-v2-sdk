# Wheaterlink V2 API

Unoficial [Wheaterlink](https://www.weatherlink.com/) API Client

Usage:

    from wheaterlink import WLClient

    client = WLClient(api_key, api_secret)

    stations = client.get_stations()

    station_id = 129681
    start = datetime.datetime.strptime("20/02/2022 00:00:00", "%d/%m/%Y %H:%M:%S")
    end = start + relativedelta(days=1)

    data = client.get_historic(station_id, start, end)