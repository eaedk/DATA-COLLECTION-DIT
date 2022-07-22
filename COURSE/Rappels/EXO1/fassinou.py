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
    def construct(item: dict):
        item['personal_data'] = {
            'guid': item['guid'],
            'lastName': item['name']['lastName'],
            'firstName': item['name']['firstName'],
            'phone': item['phone'],
            'country': item['country'],
        }
        return item
    return list(map(construct, data))


def modifyPayload4(data: List[dict]):
    def construct(item: dict):
        item['bank_data'] = {
            'pan': item.get('pan'),
            'pin': item.get('pin'),
            'cvv': item.get('cvv'),
            'iban': item.get('iban'),
            'currency': item.get('currency'),
        }
        return item
    return list(map(construct, data))


def modifyPayload5(data: List[dict]):
    def construct(item: dict):
        item['activities'] = item.get('list')
        return item
    return list(map(construct, data))


def modifyPayload6(data: List[dict]):
    def construct(item: dict):
        toDel = ["name", "country", "pan", "iban", "pin",
                 "cvv", "currency", "guid", "phone", "list"]
        for i in toDel:
            del item[i]
        return item
    return list(map(construct, data))


def writeFile(data: str):
    with open("newFile.json", "w") as outfile:
        json.dump(data, outfile)
    return "Ok"


if __name__ == '__main__':
    data = readFile('F:\DIT MASTER1 2022\DataCollection/file.json')
    data = deserialize(data)
    data = modifyPayload(data)
    data = modifyPayload2(data)

    data = modifyPayload3(data)
    data = modifyPayload4(data)
    data = modifyPayload5(data)
    data = modifyPayload6(data)
    print(data[:1])
