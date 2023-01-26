from peewee import CharField, DateTimeField, ForeignKeyField, IntegerField, Model, SqliteDatabase, TextField

db = SqliteDatabase('filostack.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = IntegerField(unique=True, primary_key=True)
    username = CharField(unique=True)
    password = CharField()
    email = CharField(unique=True)
    created_at = DateTimeField()


class Post(BaseModel):
    post_id = IntegerField(unique=True, primary_key=True)
    user = ForeignKeyField(User, backref='posts')
    title = CharField()
    body = TextField()
    like_count = IntegerField(default=0)


class Comment(BaseModel):
    user = ForeignKeyField(User, backref='comments')
    post = ForeignKeyField(Post, backref='comments')
    body = TextField()


db.create_tables([User, Post, Comment])
