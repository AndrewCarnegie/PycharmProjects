import requests
from IPython.display import Image


class GoogleMap(object):
    """Class that stores a PNG image"""
    def __init__(self, lat, long, satellite=True, zoom=10, size=(400, 400), sensor=False):
        """Define the map parameters"""
        base = "http://maps.googleapis.com/maps/api/staticmap?"
        params = dict(
                sensor=str(sensor).lower(),
                zoom=zoom,
                size="x".join(map(str, size)),
                center=",".join(map(str, (lat, long))),
                style="feature:all|element:labels|visibility:off"
                )

        if satellite:
            params["maptype"] = "satellite"

        # Fetch our PNG image data
        self.image = requests.get(base, params=params).content


Image(GoogleMap(51.0, 0.0).image)
