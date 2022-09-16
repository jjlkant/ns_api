import configparser
import os
import requests
import urllib.parse

import pandas as pd


class NSApi:
    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config.read(
            os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config.ini"))
        )
        self.session = requests.Session()
        self.base_url = "https://gateway.apiportal.ns.nl"
        # Request headers
        self.headers = {
            "Ocp-Apim-Subscription-Key": self._config.get("NS-API", "OCP-APIM-KEY"),
        }

    def get(self, url):
        return self.session.get(url=self.base_url + url, headers=self.headers)

    def get_df(self, url):
        r = self.get(url)
        r.raise_for_status()
        return pd.DataFrame(r.json())

    def get_disruptions(self, *, is_active=False):
        params = urllib.parse.urlencode({"isActive": is_active})
        return self.get_df(f"/reisinformatie-api/api/v3/disruptions?{params}")


if __name__ == "__main__":
    ns_api = NSApi()
    r = ns_api.get_disruptions()
    
    print("pause")
