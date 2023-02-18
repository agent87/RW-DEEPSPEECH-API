from fastapi.testclient import TestClient
from main import api 


client = TestClient(api)



#Test registration endpoint
def test_registration_main():
    response = client.post("/register")
    assert response.status_code == 200


#Test registration endpoint
def test_registration_main():
    response = client.post("/register")
    assert response.status_code == 200


#Test registration endpoint
def test_registration_main():
    response = client.post("/transcribe")
    assert response.status_code == 200


#Test registration endpoint
def test_registration_main():
    response = client.post("/register")
    assert response.status_code == 200