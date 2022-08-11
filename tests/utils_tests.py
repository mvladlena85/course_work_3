import json
import pytest
import utils
import random

key_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
exceptions_list = [('data/data.json', FileNotFoundError),
                   ('./data/test_data.json', json.JSONDecodeError)]


@pytest.mark.parametrize("path, exception", exceptions_list)
def test_load_data(path, exception):
    with pytest.raises(exception):
        utils._load_data(path)


def test_get_posts_all():
    posts = utils.get_posts_all()
    assert type(posts) == list, "Возвращает не список"
    posts_number = len(posts)
    assert posts_number > 0, "Пустой список"
    i = random.randint(0, posts_number - 1)
    print(i)
    assert set(posts[0].keys()) == key_should_be, "Некорректный список ключей"


def test_get_post_by_pk():
    post = utils.get_post_by_pk(2)
    assert post['pk'] == 2, "Неверный pk поста"


def test_get_posts_by_user():
    all_users = utils.get_users()
    poster_names = []
    all_posts = utils.get_posts_all()
    for post in all_posts:
        poster_names.append(post['poster_name'])
    poster_names_set = set(poster_names)
    non_poster_users = all_users.difference(poster_names_set)
    posts = utils.get_posts_by_user()



