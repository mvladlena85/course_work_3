from flask import Blueprint, jsonify

import utils
import logging

logging.basicConfig(level=logging.ERROR)

logger = logging.getLogger()
logger_handler = logging.FileHandler("api.log")
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger_handler.setFormatter(formatter)
logger.addHandler(logger_handler)

# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)


api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts')
def api_all_posts():
    logger.info(f"Запрос /api/posts")
    posts = utils.get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>')
def api_post(post_id: int):
    logger.info(f"Запрос /api/posts/{post_id}")
    post = utils.get_post_by_pk(post_id)
    return jsonify(post)
