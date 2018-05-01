from UI.models import User
import requests
from django.core import serializers

class UserHandler(object):
    # 取得資料庫中所有使用者
    @classmethod
    def get_all_user(self):
        users = User.objects.all()
        return users
    # 用 id 搜尋資料庫中的使用者
    @classmethod
    def get_user_by_id(self, user_id, json=True):
        user = User.objects.get(pk=user_id)
        if json:
            user = serializers.serialize('json', [user, ])
        return user
    # 透過 api 批次新增資料
    @classmethod
    def create_from_api(self):
        users = self.fetch_from_url()
        for user in users:
            name = user['name']
            username = user['username']
            email = user['email']
            self.create(name=name, username=username, email=email)
        return users
    # 透過 url 抓取資料
    @classmethod
    def fetch_from_url(self):
        url = 'http://jsonplaceholder.typicode.com/users'
        data = requests.get(url=url).json()
        return data

    # 新增使用者
    @classmethod
    def create(self, name, username, email='user@user.com'):
        if (self.check_data_exist(email=email)):
            user = User.objects.get(email=email)
        else:
            user = User(name=name, username=username, email=email)
            user.save()
        return user
    @classmethod
    def update(self, id, name, username, email):
        user = User.objects.get(pk=id)
        user.name = name
        user.username = username
        user.email = email
        user.save()
        return user
    # 檢查使用者是否存在
    @classmethod
    def check_data_exist(self, email):
        if (User.objects.filter(email=email).count() > 0):
            return True
        return False