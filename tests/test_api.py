def test_get_user_404(client):

    # Teste de Recuperação
    get_response = client.get(f"/users/1")
    assert get_response.status_code == 404 

def test_create_and_get_user_and_delete_user(client):
    
    payload = {
        "name": "teste",
        "email": "test@example.com"
    }

    response = client.post("/users", json=payload)
    assert response.status_code == 201
    user_id = response.json["id"]

    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 200

    del_response = client.delete(f"/users/{user_id}")
    assert del_response.status_code == 204

def test_create_and_delete_user(client):
    
    payload = {
        "name": "teste",
        "email": "test@example.com"
    }

    response = client.post("/users", json=payload)
    assert response.status_code == 201
    user_id = response.json["id"]

    del_response = client.delete(f"/users/{user_id}")
    assert del_response.status_code == 204

def test_create_two_users_and_list_and_delete_both_users(client):
    
    payload = {
        "name": "teste",
        "email": "test@example.com"
    }

    payload2 = {
        "name": "teste2",
        "email": "test2@example.com"
    }

    response = client.post("/users", json=payload)
    assert response.status_code == 201

    response2 = client.post("/users", json=payload2)
    assert response2.status_code == 201

    user_id1 = response.json["id"]
    user_id2 = response2.json["id"]

    list_response = client.get("/users")
    assert list_response.status_code == 200

    del_response = client.delete(f"/users/{user_id1}")
    assert del_response.status_code == 204

    del_response2 = client.delete(f"/users/{user_id2}")
    assert del_response2.status_code == 204