import requests
import pytest

base_url = "https://ru.yougile.com/"

my_headers = {
        "Authorization" : "Bearer aK3bkvDCW6JF1mZNp302D6IyycNQc6NjXGMy7PSC-eBcx3tgI6DuiYQ2ehO1acWy",
        "Content-Type" : "application/json"
    }

my_project = {
        "title" : "SkyPro",
        "users" : {
            "h12hb3b4j" : "worker",
            "h12hb3b4jbu3" : "admin"
        }
    }

def test_create_project():
    resp = requests.post(base_url + '/api-v2/projects', json=my_project, headers=my_headers)

    response_body = resp.json()
    assert resp.status_code == 201

def test_get_projects_list():
    projects_list = requests.get(base_url + '/api-v2/projects', headers=my_headers)
    list = projects_list.json()
    assert len(list) > 0

def test_change_id(id="12t3vh"):
    data = {
    "deleted": true,
    "title" : "SkyPro",
        "users" : {
            "h12hb3b4j" : "worker",
            "h12hb3b4jbu3" : "admin"
            }
    }
    requests.put(base_url + '/api-v2/projects/{id}', json=data, headers=my_headers)


def test_get_project_with_id(id="12t3vh"):
    project = requests.get(base_url + '/api-v2/projects/{id}', id, headers=my_headers)
    print(project)
