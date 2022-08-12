import json
import pytest
import utils
import random

key_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
comments_key_should_be = {"post_id", "commenter_name", "comment", "pk"}
exceptions_list = [('datas/data.json', FileNotFoundError),
                   ('tests/data/test_data.json', json.JSONDecodeError)]


comments_by_post_id_exceptions_list = ['34', 67]


@pytest.fixture()
def get_posters_list():
    all_posts = utils.get_posts_all()
    poster_names = [post['poster_name'] for post in all_posts]
    poster_names_set = set(poster_names)
    return list(poster_names_set)


@pytest.fixture()
def users_with_no_posts():
    all_comments = utils.load_data('data/comments.json')
    all_posts = utils.load_data('data/data.json')
    commentators = [comment['commenter_name'] for comment in all_comments]
    posters = [post['poster_name'] for post in all_posts]
    users_with_no_post = set(commentators).difference(set(posters))
    return list(users_with_no_post)


@pytest.fixture()
def pk_list():
    all_posts = utils.load_data('data/data.json')
    pk_list = [post['pk'] for post in all_posts]
    return pk_list


@pytest.mark.parametrize("path, exception", exceptions_list)
def test_load_data(path, exception):
    with pytest.raises(exception):
        utils.load_data(path)


def test_get_posts_all():
    posts = utils.get_posts_all()
    assert type(posts) == list, "Возвращает не список"
    posts_number = len(posts)
    assert posts_number > 0, "Пустой список"
    for i in range(0, posts_number):
        assert set(posts[i].keys()) == key_should_be, "Некорректный список ключей"


def test_get_post_by_pk():
    post = utils.get_post_by_pk(2)
    assert post['pk'] == 2, "Неверный pk поста"


def test_get_posts_by_user(get_posters_list):
    i = random.randint(0, len(get_posters_list) - 1)
    posts = utils.get_posts_by_user(get_posters_list[i])
    assert type(posts) == list, "Возвращает не список"
    posts_number = len(posts)
    assert posts_number > 0, "Пустой список"
    for j in range(0, posts_number):
        assert set(posts[j].keys()) == key_should_be, "Некорректный список ключей"


def test_get_posts_by_user_value_error():
    with pytest.raises(ValueError):
        utils.get_posts_by_user('bla-bla')


def test_get_posts_by_user_user_without_posts(users_with_no_posts):
    posts = utils.get_posts_by_user(users_with_no_posts[0])
    assert len(posts) == 0, "не пустой список"


@pytest.mark.parametrize("post_id", comments_by_post_id_exceptions_list)
def test_get_comments_by_post_id_errors(post_id):
    with pytest.raises(ValueError):
        utils.get_posts_by_user(post_id)


def test_get_comments_by_post_id(pk_list):
    i = random.randint(1, len(pk_list) - 1)
    comments = utils.get_comments_by_post_id(i)
    assert type(comments) == list, "Возвращает не список"
    comments_number = len(comments)
    assert comments_number > 0, "Пустой список"
    for j in range(0, comments_number):
        assert set(comments[j].keys()) == comments_key_should_be, "Некорректный список ключей"
    post_with_no_comments = utils.get_comments_by_post_id(8)
    assert post_with_no_comments == [], "У данного поста есть комментарии"


def test_search_for_posts():
    posts = utils.search_for_posts(' на ')
    assert len(posts) == 6
    posts_case_sensitivity = utils.search_for_posts(' На ')
    assert len(posts_case_sensitivity) == 6
    no_posts = utils.search_for_posts(' стрелы ')
    assert len(no_posts) == 0



