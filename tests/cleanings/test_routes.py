import json


def test_post_request_with_valid_data_should_create_cleaning(client):
    data = {"name":"test_john","description":"testing post!","cleaning_type":"spot_clean","price":30}
    response = client.post("/create/cleanings/",data=json.dumps(data)) #caution add / at last
    assert response.status_code == 200
    assert response.json()['id'] == 1