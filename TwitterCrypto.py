import requests
import keys
import pprint
import json


headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'Authorization': "Bearer {}".format(keys.BEARER_TOKEN)

}

# r = requests.get('https://api.twitter.com/2/tweets/search/recent?query=from:safemoon',headers=headers)

# print()
# pprint.pprint(r.json())
# print()


# alt_coin_rule = {
#     'add': [
#         {'value': '#altcoin -is:retweet'},
#     ]
# }

# rule_request = requests.post(
#     'https://api.twitter.com/2/tweets/search/stream/rules', headers=headers, json=alt_coin_rule)

# print()
# pprint.pprint(rule_request.json())
# print()


try:
    response = ''
    with requests.get("https://api.twitter.com/2/tweets/search/stream", headers=headers, stream=True) as stream:
        for line in stream.iter_lines():
            if line:
                json_response = json.loads(line)
                print(json.dumps(json_response, indent=4, sort_keys=True))
            #print(line.decode())
            #response = response + line.decode()
except KeyboardInterrupt:
    pass

# response = json.loads(stream)
# print()
# pprint.pprint(response)
# print()
# data = open('data/response.json', 'w')
# data.write(response)
# data.close()
