from flask import Blueprint, request, jsonify

cmmt = Blueprint('cmmt', __name__)


@cmmt.route('/comments', methods=['GET'])
def get_msg():
    return jsonify({
        'msg': 'Hello World!'
    })
