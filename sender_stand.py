import configuration
import requests
import data

# Марина Максимова, 12 когорта - Финальный проект. Инженер по тестированию плюс
def new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER,
                         json=body)


order_track = new_order(data.order_body).json()["track"]


def get_order(track_order):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER + str(track_order))


def test_get_new_order():
    response = new_order(data.order_body)
    track = response.json()["track"]

    response_order = get_order(order_track)
    assert response_order.status_code == 200
