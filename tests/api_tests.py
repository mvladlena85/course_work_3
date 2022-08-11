
from run import app


key_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_api_all_posts():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    json = response.json
    assert type(json) == list
    assert set(json[0].keys()) == key_should_be


def test_api_post():
    response = app.test_client().get('/api/posts/2')
    assert response.status_code == 200
    json = response.json
    assert type(json) == dict
    assert set(json.keys()) == key_should_be
