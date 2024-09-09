import requests
from datetime import datetime

USERNAME = "regen"
TOKEN = "hjkibnmadjfjadfboaubsdjasoninwu92nknko"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "hjkibnmadjfjadfboaubsdjasoninwu92nknko",
    "username": "regen",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)

# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# today = datetime(year=2024, month=11, day=9)

today = datetime.now()

pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_create_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you spend coding today? "),
}

response = requests.post(url=pixel_create_endpoint, json=pixel_create_config, headers=headers)
print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

pixel_update_config = {
    "quantity": "4.0",
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
