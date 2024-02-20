import requests

urls = ["https://github.com",
        "https://google.com",
        "https://linkedin.com"]

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        print("%s is up" % url)
