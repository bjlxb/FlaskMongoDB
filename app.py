from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/set_collections/<dbname>/<tablename>')
def set_collections(dbname, tablename):
    conn = MongoClient('127.0.0.1', 27017)
    # 连接mydb数据库，没有则自动创建
    db = conn.dbname
    # 使用test_set集合，没有则自动创建
    my_set = db.tablename
    print(my_set)
    return 'Hello World!'


@app.route('/get_database')
def get_database():
    myclient = MongoClient('127.0.0.1', 27017)
    dblist = myclient.list_database_names()

    print(dblist)
    # return '{}'.format(dblist)
    # return jsonify({'data': list(dblist)})
    return jsonify(dblist)


@app.route('/get_one_collection/one')
def get_one_collection(one):
    conn = MongoClient('127.0.0.1', 27017)
    # 连接mydb数据库，没有则自动创建
    db = conn.mydb
    # 使用test_set集合，没有则自动创建
    my_set = db.test_set
    one = my_set.find_one(one)

    return jsonify(one)


@app.route('/get_collections/')
def get_collections():
    conn = MongoClient('127.0.0.1', 27017)
    # 连接mydb数据库，没有则自动创建
    db = conn.mydb
    # 使用test_set集合，没有则自动创建
    my_set = db.test_set
    li = []
    # 查询全部
    for i in my_set.find():
        li.append(i)
        print(i)
    # 查询name=zhangsan的
    for i in my_set.find({"name": "zhangsan"}):
        print(i)
    return '{}'.format(li)


if __name__ == '__main__':
    app.run()
