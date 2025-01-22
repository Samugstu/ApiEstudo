from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test__tabuada_deve_retornar_um_array():
    client = TestClient(app)

    response = client.get('/tabuada/5')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == [       
            '5 X 0 = 5',
            '5 X 1 = 5',
            '5 X 2 = 5',
            '5 X 3 = 5',
            '5 X 4 = 5',
            '5 X 5 = 5',
            '5 X 6 = 5',
            '5 X 7 = 5',
            '5 X 8 = 5',
            '5 X 9 = 5',
        ]
    
