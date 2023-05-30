from doki import mongo


def find_user(username):
    result = mongo.empdb.users.find_one({"username": username})
    return result

def reg_user(new_user):
    result = mongo.empdb.users.insert_one(new_user)
    return result

def delUser(usernamedb):
    result = mongo.empdb.users.delete_one({'username':usernamedb})
    return result

