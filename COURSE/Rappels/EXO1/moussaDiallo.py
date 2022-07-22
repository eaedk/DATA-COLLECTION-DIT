import json
from typing import List


def readFile(filename: str):
    with open(filename, 'r') as file:
        data = file.read()
        file.close()
    return data


def deserialize(data: str):
    return json.loads(data)


def modifyPayload(data: List[dict]):
    def construct(item: dict):
        if item.get('name') != None:
            splitter = item \
                .get('name') \
                .split(' ')
            item['name'] = {
                'lastName': splitter[0].upper(),
                'firstName': splitter[-1].capitalize(),
            }
        return item
    return list(map(construct, data))


def modifyPayload2(data: List[dict]):
    def construct(item: dict):
        if item.get('list') != None:
            splitter = item \
                .get('list') \
                .split(', ')
            item['list'] = splitter
        return item
    return list(map(construct, data))


def modifyPayload3(data: List[dict]):
    def AddingPD(item: list[dict]):
        item["Personal_data"] = {}
        klist = ["name", "guid", "phone", "country"]
        for k in klist:
            if k == "name":
                if item.get('name') != None:
                    item["Personal_data"]['lastName'] = item["name"]["lastName"]
                    item["Personal_data"]['firstName'] = item["name"]["firstName"]
            else:
                item["Personal_data"][k] = item[k]
        return item
    return list(map(AddingPD, data))


def modifyPayload4(data: List[dict]):
    def AddingBankData(item: list[dict]):
        item["Bank_data"] = {}
        klist = ["pan", "pin", "cvv", "iban", "currency"]
        for k in klist:
            item["Bank_data"][k] = item[k]
        return item
    return list(map(AddingBankData, data))


def modifyPayload5(data: List[dict]):
    def AddingActivities(item: list[dict]):
        item["Activities"] = {}
        klist = ['list']
        for k in klist:
            item["Activities"] = item[k]
        return item
    return list(map(AddingActivities, data))


def modifyPayload6(data: List[dict]):
    def DropItem(item: list[dict]):
        klist = ["name", "guid", "phone", "country", "pan",
                 "pin", "cvv", "iban", "list", "currency"]
        for k in klist:
            del item[k]
        return item
    return list(map(DropItem, data))
