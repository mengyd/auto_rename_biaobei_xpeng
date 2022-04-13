import os, json

def loadRelation(relation_path):
    f = open(relation_path,'r', encoding='UTF-8')
    dict_relation = json.load(f)
    return dict_relation

def loadConfig(choice = 'relation'):
    workpath = os.path.abspath(os.path.join(os.getcwd(), ""))
    relation = loadRelation(workpath+'/mobile_data_relation.json')
    if choice == 'relation':
        return relation
    return relation
