import requests

url = "https://jgentes-crime-data-v1.p.rapidapi.com/crime"

querystring = {"startdate":"9/19/2015","enddate":"9/25/2015","lat":"37.757815","long":"-122.5076392"}

headers = {
    'x-rapidapi-key': "1d1b5ffa8fmsh75601f5c441b803p1ab702jsn0a3b9f14fd48",
    'x-rapidapi-host': "jgentes-Crime-Data-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)