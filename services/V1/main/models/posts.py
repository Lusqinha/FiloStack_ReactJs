from model import Comment, Post, User
from json import dumps


# CREATE
def create_post(user_id, title, content, date):
    post = Post(user_id=user_id, title=title, content=content, date=date)
    return post


# READ
def get_all_posts():
    posts = Post.select()
    return dumps([post.to_dict() for post in posts])


def get_post_by_id(id):
    post = Post.get(Post.id == id)
    return dumps(post.to_dict())


def get_post_by_user_id(id):
    posts = Post.select().where(Post.user_id == id)
    return dumps([post.to_dict() for post in posts])


def get_post_by_title(title):
    posts = Post.select().where(Post.title == title)
    return dumps([post.to_dict() for post in posts])


def get_post_by_content(content):
    posts = Post.select().where(Post.content == content)
    return dumps([post.to_dict() for post in posts])


def get_post_by_date(date):
    posts = Post.select().where(Post.date == date)
    return dumps([post.to_dict() for post in posts])


if __name__ == '__main__':
    print(get_all_posts())
