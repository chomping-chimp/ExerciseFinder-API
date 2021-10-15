from . import db_api
import json
db = db_api.DB()

'''
Function to get all Exercises from DB
'''
def get_all():
    query = "SELECT * FROM Fitness.Exercises"
    result = db.db_get(query)
    return result

'''
Function to return exercises based on filters
Params: filterList - List of Filters
'''
def filterGroups(filterList):
    splitList = filterList.split('%')
    if (len(splitList) == 1):
        filters = splitList[0]
        query = ("SELECT * FROM Fitness.AllExercises WHERE `Primary Muscle` = '{}'".format(filters))
    else:
        filters = tuple(splitList)
        query = ("SELECT * FROM Fitness.AllExercises WHERE `Primary Muscle` IN {}".format(filters))
    result = db.db_get(query)
    return result