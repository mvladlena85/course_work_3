import json


def _load_data(path) -> list[dict]:
    """
    Функция возвращает список данные из файла.
    :param path:
            путь к файлу
    :return: list[dict]
            данные из файла
    """
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_posts_all() -> list[dict]:
    """
    Функция возвращает посты
    :return: list[dict]
            данные из файл
    """
    return _load_data('data/data.json')


def get_posts_by_user(user_name: str) -> list[dict]:
    """
    Функция возвращает посты определенного пользователя.
    Функция должна вызывать ошибку ValueError если такого пользователя нет и пустой список,
    если у пользователя нет постов.
    :param user_name: str
    :return:
    """
    all_posts = _load_data('data/data.json')
    if user_name not in get_users():
        raise ValueError('Нет такого пользователя')
    posts_by_user = []
    for post in all_posts:
        if post['poster_name'] == user_name:
            posts_by_user.append(post)
    return posts_by_user


def get_comments_by_post_id(post_id: int) -> list[dict]:
    """
    Функция возвращает комментарии определенного поста.
    Функция должна вызывать ошибку ValueError если такого поста нет и пустой список, если у поста нет комментов.
    :param post_id: int
            идентификатор поста
    :return: list[dict]
            список комментариев к посту
    """
    all_comments = _load_data('data/comments.json')
    comments = []
    for comment in all_comments:
        if comment['post_id'] == post_id:
            comments.append(comment)
    return comments


def search_for_posts(query: str) -> list[dict]:
    """
    Функция возвращает список постов по ключевому слову
    :param query: str
            критерий поиска
    :return: list[dict]
            список найденных постов
    """
    all_posts = _load_data('data/data.json')
    search_result = []

    for post in all_posts:
        if query.lower() in post['content'].lower():
            search_result.append(post)
    return search_result


def get_post_by_pk(pk: int) -> dict:
    """
    Функция возвращает один пост по его идентификатору.
    :param pk: int
    :return: dict
    """
    all_posts = _load_data('data/data.json')

    for post in all_posts:
        if post['pk'] == pk:
            return post


def get_users() -> set:
    all_comments = _load_data('data/comments.json')
    all_posts = _load_data('data/data.json')
    users = []
    for comment in all_comments:
        users.append(comment['commenter_name'])
    for post in all_posts:
        users.append(post['poster_name'])
    return set(users)
