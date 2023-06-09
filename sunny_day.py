import requests, pprint


# url = "http://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid=71d19286fea826083bb6034cb77c82d2&units=metric"
# r = requests.get(url)
# print(r.json())


class Weather:

    def __init__(self, api_key, lat=None, lon=None):
        if lat and lon:
            url = url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("Please provide the coordinates")

    def next_12h(self):
        return self.data['list'][:4]
        # return len(self.data['list'])

    def next_12h_simplified(self):
        pass


latitude = 43.25
longitude = 76.95
weather = Weather(api_key="71d19286fea826083bb6034cb77c82d2", lat=latitude, lon=longitude)
pprint.pprint(weather.next_12h())
