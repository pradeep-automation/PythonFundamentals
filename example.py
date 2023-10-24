import requests
import json


# payload = {
#     "name": "Hello",
#     "job": "leader"
# }
with open("data.txt", "r") as f:
    payload = f.read()
    
    print(json.dumps(payload))
    # res = requests.post("https://reqres.in/api/users", json=json.loads(payload))
    #
    # print(res.json())
    # assert 201 == res.status_code

headers = {"Authorization": "token cd61f441132925ff42be888217818e6d506baa02"}
res = requests.get("https://vet-qa.membership-nonprod.petco.com/v1/practice/search",
                   params={"vetsource_id": "40000774"}, headers= headers)
print(res.status_code)
assert "Independent 3" == (res.json()["items"][0]["name"]), "We are expecting Independent 3 here"

