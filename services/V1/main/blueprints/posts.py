from flask import blueprints, jsonify, request
from models.model import Comment, Post, User
pst = blueprints.Blueprint('pst', __name__)


@pst.route('/posts', methods=['GET'])
def get_all_posts():
    return jsonify({
        'msg': 'Hello World!'
    })
