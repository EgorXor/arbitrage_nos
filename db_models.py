admin@bithub-bot:~/Bot/app$ cat db_models.py
from peewee import *
import datetime
from config import *

db = PostgresqlDatabase(DB_NAME, user=DB_USER, password=DB_PASSWORD)


class BaseModel(Model):

    class Meta:
        database = db


class Users(BaseModel):
    uid = PrimaryKeyField()
    f_name = CharField()
    state = CharField()
    prev = CharField(null=True)
    admin = BooleanField(default=False)
    date_reg = DateTimeField(default=datetime.datetime.now())


class Subscribers(BaseModel):
    id = PrimaryKeyField()
    uid = ForeignKeyField(Users, related_name='sub', unique=True)
    group = CharField()
    date = DateTimeField(null=True)
    perm = BooleanField(default=False)


class Referrals(BaseModel):
    uid = PrimaryKeyField()
    referral = ForeignKeyField(Users, related_name='ref')
    added = BooleanField(default=True)


class Profit(BaseModel):
    uid = ForeignKeyField(Users, related_name='profit', primary_key=True)
    count = FloatField(default=0)


class Wiki(BaseModel):
    name = CharField(primary_key=True)
    description = TextField()
    link = CharField()


class Culc(BaseModel):
    id = PrimaryKeyField()
    count = IntegerField(default=1)

admin@bithub-bot:~/Bot/app$