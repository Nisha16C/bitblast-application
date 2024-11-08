import requests

project_id=1
private_token="glpat-QnYftX2oXsc9N5xSxG4n"
base_url="http://gitlab-ce.os3.com/api/v4/"
headers = {"PRIVATE-TOKEN": private_token}

formData = {
    'ref' : 'ankitv-test'
}


response = requests.post(base_url + f"projects/{project_id}/pipeline", headers=headers, json=formData,
                             verify=False)

print(response)