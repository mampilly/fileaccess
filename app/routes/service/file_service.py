import requests
from base64 import b64encode

host = "https://api.github.com"


def test_health():
    return {"message": "Success"}


def user_details(username, password):
    data = {"user_details": get_user_details(username, password)}
    return data


def file_details(username, password, repository_name, file_path):

    data = {"file_details": fetch_file_details(
        username, password, repository_name, file_path)}
    return data


def get_user_details(username, password):
    try:
        endpoint = "/user"
        headers = authentication(username, password)
        user_details = requests.get(
            host+endpoint, headers=headers)
        if user_details.status_code == 200:
            user_data = user_details.json()
            return user_data
        return {"Message": "Issue with username or password", "status_code": user_details.status_code}
    except Exception as e:
        return {"Error": str(e)}


def get_pull_logs(username, password, repository_name):
    endpoint = "/repos/{}/{}/commits".format(
        username, repository_name)
    headers = authentication(username, password)
    user_details = requests.get(
        host+endpoint, headers=headers)
    if user_details.status_code == 200:
        user_data = user_details.json()
        return user_data
    return {"Message": "Issue with username or password", "status_code": user_details.status_code}


def fetch_file_details(username, password, repository_name, file_path):
    try:
        if not file_path:
            endpoint = "/repos/{}/{}/contents/".format(
                username, repository_name)
        else:
            endpoint = "/repos/{}/{}/contents/{}".format(
                username, repository_name, file_path)
        headers = authentication(username, password)
        file_details = requests.get(host+endpoint, headers=headers)
        if file_details.status_code == 200:
            file_data = file_details.json()
            # download_end_point = file_data[0]
            if type(file_data) == dict:
                download_end_point = file_data['download_url']
                file_content = requests.get(
                    download_end_point, headers=headers)

                if file_content.status_code == 200:
                    return file_content.content
            else:
                file_elements = []
                for i in file_data:
                    if 'download_url' in i.keys() and i['download_url']:
                        file_content = requests.get(
                            i['download_url'], headers=headers)
                        if file_content.status_code == 200:
                            file_elements.append(
                                {i['name']: file_content.content})
                return file_elements

        return {"message": "issue with file repo", "status_code": file_details.status_code}
    except Exception as e:
        return {"Error": str(e)}


def authentication(username, password):
    userAndPass = b64encode(
        bytes(username + ':' + password, "utf-8")).decode("ascii")
    headers = {'Authorization': 'Basic %s' % userAndPass}
    return headers
