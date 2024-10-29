import requests

base_url = "https://ru.yougile.com"

my_headers = {
    "Authorization": "Bearer aK3bkvDCW6JF1mZNp302D6IyycNQc6NjXGMy7PSC-eBcx3tgI6DuiYQ2ehO1acWy",
    "Content-Type": "application/json"
}

my_project = {
    "title": "SkyPro"
}


def test_create_project():
    resp = requests.post(base_url + '/api-v2/projects', json=my_project, headers=my_headers)
    assert resp.status_code == 201

#без хедеров
def test_create_project_negative():
    resp = requests.post(base_url + '/api-v2/projects', json=my_project)
    assert resp.status_code == 401

def test_get_projects_list():
    projects_list = requests.get(base_url + '/api-v2/projects', headers=my_headers)
    lst = projects_list.json()
    assert len(lst) > 0


def test_change_id():
    #создать
    resp = requests.post(base_url + '/api-v2/projects', json=my_project, headers=my_headers)
    id_proj = resp.json()["id"]
    data = {
        "deleted": True,
        "title": "SkyPro2"
    }
    #поменять
    response = requests.put(base_url + f'/api-v2/projects/{id_proj}', json=data, headers=my_headers)
    assert response.json()["id"] == id_proj

    #получить id и сравнить
    project = requests.get(base_url + f'/api-v2/projects/{id_proj}', headers=my_headers)
    assert project.json()["title"] == "SkyPro2"

def test_change_id_nagetive():
    #создать
    resp = requests.post(base_url + '/api-v2/projects', json=my_project, headers=my_headers)
    id_proj = resp.json()["id"]
    data = {
        "deleted": True,
        "title": ""
    }
    #поменять
    response = requests.put(base_url + f'/api-v2/projects/{id_proj}', json=data, headers=my_headers)
    assert response.status_code == 400

def test_get_project_with_id():
    resp = requests.post(base_url + '/api-v2/projects', json=my_project, headers=my_headers)
    id_proj = resp.json()["id"]
    project = requests.get(base_url + f'/api-v2/projects/{id_proj}', headers=my_headers)
    assert project.json()["title"] == "SkyPro"
    

