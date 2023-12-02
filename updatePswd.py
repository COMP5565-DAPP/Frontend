import os
import django
from django.contrib.auth.hashers import make_password
import pymongo

# for update passwords in mongodb

# 设置 Django 环境
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "COMP5565_DAPP.settings")
django.setup()

def update_passwords():
    MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
    localDB = MongoDB_client['local']
    companySet = localDB['users']

    for user in companySet.find():
        hashed_pwd = make_password(user['password'])
        companySet.update_one({"_id": user['_id']}, {"$set": {"password": hashed_pwd}})

    MongoDB_client.close()

# 运行脚本
update_passwords()
