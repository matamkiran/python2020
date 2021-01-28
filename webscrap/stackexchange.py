# Import package
import requests
import json

# Assign URL to variable: url
url = 'https://api.stackexchange.com/2.2/tags?order=desc&sort=popular&site=stackoverflow'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])
    if(k=='items'):
        json_data_set=json_data[k]
   #     json_data_set=json_data[k]
   #     for key,value in json_data_set.items():
   #         print(key + " "+ value)


print(json_data_set)

strjson=json.dumps(json_data_set)

print(strjson)
