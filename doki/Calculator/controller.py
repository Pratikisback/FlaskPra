from doki import mongo


def regcal(a, b, mulval, subval, addval, divval):
    result = mongo.empdb.calculated.insert_one({"First_number": a, "second_number": b, "Mulval": mulval,"Subval": subval, "Addval": addval, "DivVal": divval })
    if result:
        return True
    else:
        return False
