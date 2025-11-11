from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def post_calc(a,b,op):
    return client.post('/calculate', json={'a':a,'b':b,'op':op})

def test_add():
    r = post_calc(2,3,'add')
    assert r.status_code == 200 and r.json()['result'] == 5

def test_sub():
    r = post_calc(5,1,'sub')
    assert r.status_code == 200 and r.json()['result'] == 4

def test_mul():
    r = post_calc(3,4,'mul')
    assert r.status_code == 200 and r.json()['result'] == 12

def test_div():
    r = post_calc(10,2,'div')
    assert r.status_code == 200 and r.json()['result'] == 5

def test_div_by_zero():
    r = post_calc(1,0,'div')
    assert r.status_code == 400 and 'Division by zero' in r.json()['detail']
