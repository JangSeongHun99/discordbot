from pymongo import MongoClient
import os

def get_database():
    client = MongoClient("mongodb+srv://seonghun:Wkd990921!@seonghun.hlvm3d7.mongodb.net/?retryWrites=true&w=majority")
    return client['seonghun']


def get_collection(name):
    db = get_database()
    coll = db.get_collection(name)
    return coll

def insertDB(collName, data):
    coll = get_collection(collName)
    try:
        coll.insert_one(data)
        print('추가 완료')
        return True
    except:
        print('추가 오류')
        return False

def deleteDB(collName, userId):
    coll = get_collection(collName)
    try:
        coll.delete_one({'userID': userId})
        print('삭제 완료')
        return True
    except:
        print('삭제 오류')
        return False

def findDB(collName, userId):
    coll = get_collection(collName)
    try:
        db = coll.find_one({'userID': userId})
        print('검색 완료')
        return db
    except:
        print('검색 실패')
        return False

def sortDB(collName, fieldname):
    coll = get_collection(collName)
    try:
        data = coll.find({},{"money","userID"}).limit(10).sort(fieldname, -1)
        print('정렬 완료')
        return data
    except:
        print('정렬 실패')
        return False

def updateDB(collName, userId, field_name, new_value):
    coll = get_collection(collName)
    try:
        coll.update_one({'userID':userId},{'$set':{field_name: new_value}})
        print('수정 완료')
    except:
        print('수정 실패')
        return False
