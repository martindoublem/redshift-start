import requests
import os


class LocationConf(object):
    def __init__(self):
        self.location = self.get_location()

    def get_location(self):
        api_url = "https://demo.ip-api.com/json/?fields=33288191&lang=en"
        headers = {
            "Host": "demo.ip-api.com",
            "Origin": "https://ip-api.com",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "cors",
            "Referer": "https://ip-api.com/"
        }
        result = requests.get(api_url, headers=headers).json()
        location = {'lat': result['lat'], 'lon': result['lon']}
        return location

    def write_file(self):
        dir = "/home/doublem/.config/redshift/"
        os.chdir(dir)
        conf = 'redshift.conf'
        new_file = []
        with open(conf, 'r') as f:
            for line in f.readlines():
                if 'lat' in line:
                    line = 'lat=%s\n' % self.location['lat']
                if 'lon' in line:
                    line = 'lon=%s\n' % self.location['lon']
                new_file.append(line)
        with open(conf, 'w') as f:
            f.write(''.join(new_file))


if __name__ == "__main__":
    conf = LocationConf()
    conf.write_file()
