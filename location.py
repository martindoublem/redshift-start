import requests


def location():
    api_url = "https://demo.ip-api.com/json/?fields=33288191&lang=en"
    headers = {
        "Host": "demo.ip-api.com",
        "Origin": "https://ip-api.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Referer": "https://ip-api.com/"
    }
    result = requests.get(api_url, headers=headers).json()
    lat, lon = result['lat'], result['lon']
    return "%s:%s" % (lat, lon)


if __name__ == "__main__":
    print(location())
