import json
import textwrap
import urllib.request

API_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/Sweden_at_the_1978_European_Athletics_Championships"


# TODO Change the method to return only 'extract_html' section.
def fetch_extract_html():

    response = urllib.request.urlopen(API_URL)
    text = response.read()
    
    pass

if __name__ == "__main__":
    fetch_extract_html()
