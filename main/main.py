from flask import Blueprint, render_template, request, abort

from utils import get_post_by_pk, get_comments_by_post_id, get_posts_all, search_for_posts, get_posts_by_user

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@main_blueprint.route('/posts/<int:postid>')
def post_page(postid):
    post = get_post_by_pk(postid)
    if post is None:
        abort(404)
    comments = get_comments_by_post_id(post['pk'])
    comments_number = len(comments)
    return render_template('post.html', post=post, comments=comments, comments_number=comments_number)


@main_blueprint.route('/search/')
def search_results():
    search_key = request.args['s']
    search_result = search_for_posts(search_key)
    search_count = len(search_result)
    return render_template('search.html', search_result=search_result, search_count=search_count)


@main_blueprint.route('/users/<username>')
def users_posts(username):
    posts = get_posts_by_user(username)
    if len(posts) == 0:
        return render_template('user-feed-no-posts.html', username=username)
    return render_template('user-feed.html', posts=posts)
