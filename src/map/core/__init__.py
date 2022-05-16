import requests


def yoga_centres(city="delhi"):
    """Returns the list of names and latitude, longitude of the top 10 yoga classes in a city"""
    countryRegion = "IN"  # India
    adminDistrict = "Delhi"
    locality = "Delhi"
    maxResults = 10
    key = "AmWjQTcIic09wxt3sTRCNZQZXlJ2vSF6cZVEW02y44Fg63PYzOlzmO1H1Hn9NVIg"
    url = f"http://dev.virtualearth.net/REST/v1/Locations?countryRegion={countryRegion}&locality={locality}&maxResults={maxResults}&key={key}"
    r = requests.request("GET", url)
    data = r.json()
    return data
