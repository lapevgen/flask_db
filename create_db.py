from db import DB
from user_model import UserModel
from news_model import NewsModel


db = DB()
users_model = UserModel(db.get_connection())
users_model.init_table()
users_model.insert("test1", "111")
news_model = NewsModel(db.get_connection())
news_model.init_table()
