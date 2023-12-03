import web3.eth
from web3 import Web3
from enum import Enum
from eth_account.messages import encode_defunct

client = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
contract_address = '0xd8bcAdA0DcAF175F44A49322744C7915B02d85fA'

contract_abi = [
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "diamondId",
                "type": "uint256"
            },
            {
                "indexed": True,
                "internalType": "int256",
                "name": "uniqueId",
                "type": "int256"
            },
            {
                "indexed": False,
                "internalType": "enum DiamondTrackingContract.DiamondStatus",
                "name": "status",
                "type": "uint8"
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "currentOwner",
                "type": "address"
            }
        ],
        "name": "DiamondUpdated",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "Pro_Mine_diamondId",
                "type": "uint256"
            }
        ],
        "name": "carveDiamond",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "diamondId",
                "type": "uint256"
            }
        ],
        "name": "collectDiamond",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "diamondId",
                "type": "uint256"
            }
        ],
        "name": "designDiamond",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "diamonds",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "identification",
                "type": "uint256"
            },
            {
                "internalType": "int256",
                "name": "unique_id",
                "type": "int256"
            },
            {
                "internalType": "enum DiamondTrackingContract.DiamondStatus",
                "name": "status",
                "type": "uint8"
            },
            {
                "internalType": "address",
                "name": "currentOwner",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "engraved_quantity",
        "outputs": [
            {
                "internalType": "int256",
                "name": "",
                "type": "int256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "diamondId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "companyNum",
                "type": "uint256"
            }
        ],
        "name": "mineDiamond",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "Mine_diamondId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "companyNum",
                "type": "uint256"
            }
        ],
        "name": "processDiamond",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "diamondId",
                "type": "uint256"
            }
        ],
        "name": "purchaseDiamond",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "diamondId",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferDiamond",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "validDiamondIds",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "viewAllDiamonds",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "identification",
                        "type": "uint256"
                    },
                    {
                        "internalType": "int256",
                        "name": "unique_id",
                        "type": "int256"
                    },
                    {
                        "internalType": "enum DiamondTrackingContract.DiamondStatus",
                        "name": "status",
                        "type": "uint8"
                    },
                    {
                        "internalType": "address",
                        "name": "currentOwner",
                        "type": "address"
                    }
                ],
                "internalType": "struct DiamondTrackingContract.Diamond[]",
                "name": "",
                "type": "tuple[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]


class CompanyTypes(Enum):
    Mining = 0,
    Process = 1,
    Carve = 2,
    CollectAndJewelry = 3,
    Customer = 4


class DiamondStatus(Enum):
    Mined = 0,
    Processed = 1,
    Carved = 2,
    Collected = 3,
    Jewelry = 4,
    Sold = 5


import pymongo

def sign(privateKey, unique_id):
    unique_id = str(unique_id).encode('ascii')
    encode_message = encode_defunct(unique_id)

    signed_message = web3.eth.Eth.account.sign_message(encode_message, private_key=privateKey)
    print(signed_message.signature)
    return signed_message.signature


def verify(expectedAddress, signature, unique_ID):
    unique_ID = str(unique_ID).encode('ascii')
    encode_message = encode_defunct(unique_ID)

    signer = web3.eth.Eth.account.recover_message(encode_message, signature=signature)
    print(signer)
    if expectedAddress == signer:
        return True
    else:
        return False


# MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
# localDB = MongoDB_client['local']
# diamondSet = localDB['diamond']
# companySet = localDB['company']


def viewAllProcessableDiamonds():
    MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
    localDB = MongoDB_client['local']
    diamondSet = localDB['diamond']
    result = list(diamondSet.find({"diamondStatus": 0}, {'_id': 0}))
    # for result in result:
    #     print(result)
    MongoDB_client.close()
    return result


def viewAllCarveableDiamonds():
    MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
    localDB = MongoDB_client['local']
    diamondSet = localDB['diamond']
    findResult = list(diamondSet.find({'diamondStatus': 1}, {'_id': 0}))
    MongoDB_client.close()
    return findResult


def viewAllCollectibleDiamond():
    MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
    localDB = MongoDB_client['local']
    diamondSet = localDB['diamond']
    findResult = list(diamondSet.find({'diamondStatus': 2}, {'_id': 0}))
    MongoDB_client.close()
    return findResult


def viewAllDesignableDiamond(address):
    MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
    localDB = MongoDB_client['local']
    diamondSet = localDB['diamond']
    result = list(diamondSet.find({'diamondStatus': 3, 'currentOwner': address}, {'_id': 0}))
    for i in result:
        print(i)
    MongoDB_client.close()
    return result


def viewAllPurchaseableDiamond():
    MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
    localDB = MongoDB_client['local']
    diamondSet = localDB['diamond']
    result = list(diamondSet.find({'diamondStatus': 4}, {'_id': 0}))
    # for i in result:
    #     print(i)
    MongoDB_client.close()
    return result


def viewOwnedDiamond(address):
    MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
    localDB = MongoDB_client['local']
    diamondSet = localDB['diamond']
    result = list(diamondSet.find({'diamondStatus': 5, 'currentOwner': address}, {'_id': 0}))
    MongoDB_client.close()
    return result

# old version:
# def insertCompany(companyName, password, address, companyNum, companyType):
#     MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
#     localDB = MongoDB_client['local']
#     companySet = localDB['company']
#     insertData = {'companyName': companyName, 'password': password, 'address': address, "companyNum": companyNum,
#                   'companyType': companyType}
#     companySet.insert_one(insertData)
#     MongoDB_client.close()

def insertCompany(companyName, password, address, companyNum, companyType):
    with pymongo.MongoClient("mongodb://localhost:27017/local") as MongoDB_client:
        localDB = MongoDB_client['local']
        userSet = localDB['users']

        #check if the user already exists
        if userSet.find_one({'userName': companyName}):
            return False

        insertData = {
            'companyName': companyName, 
            'password': password, 
            'address': address, 
            "companyNum": companyNum,
            'companyType': companyType
        }
        userSet.insert_one(insertData)
        return True

# old version:
# def getCompany():
#     MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
#     localDB = MongoDB_client['local']
#     companySet = localDB['company']
#     result = list(companySet.find({}, {'_id':0}))
#     MongoDB_client.close()
#     return result

def getCompany(username):
    MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
    localDB = MongoDB_client['local']
    companySet = localDB['users']
    # 假设用户名字段是 'username'
    user = companySet.find_one({"username": username}, {'_id': 0})
    MongoDB_client.close()
    return user


def getDiamond(address):
    MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
    localDB = MongoDB_client['local']
    diamondSet = localDB['diamond']
    result = list(diamondSet.find({'currentOwner': address}, {'_id': 0}))
    MongoDB_client.close()
    return result



Instance = client.eth.contract(address=contract_address, abi=contract_abi)
currentUniqueID = 10001
uniqueID_Signature = []


def mineDiamond(diamondID, companyNum, address):
    web3.eth.Eth.default_account = address
    Instance.functions.mineDiamond(diamondID, companyNum).transact({'from': address, 'gas': 4000000})
    insertData = {'identification': diamondID + 100 * companyNum, 'diamondStatus': 0, 'currentOwner': address,
                  'unique_id': -1}
    MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
    localDB = MongoDB_client['local']
    diamondSet = localDB['diamond']
    diamondSet.insert_one(insertData)
    MongoDB_client.close()

# result = Instance.functions.viewAllDiamonds().call()
# print(result)
#mineDiamond(5, 2, '0x080375f44520893207235aB47fe462518D7019e9')

def processDiamond(mined_diamondID, companyNum, address):
    web3.eth.Eth.default_account = address
    Instance.functions.processDiamond(mined_diamondID, companyNum).transact({'from': address, 'gas': 4000000, 'value': Web3.to_wei(0.5, 'ether')})
    MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
    localDB = MongoDB_client['local']
    diamondSet = localDB['diamond']
    diamondSet.update_one({'identification':mined_diamondID}, {'$set': {'diamondStatus': 1, 'identification':mined_diamondID+1000*companyNum, 'currentOwner': address}})
    MongoDB_client.close()
#processDiamond(205, 1, '0x080375f44520893207235aB47fe462518D7019e9')

def carveDiamond(pro_mine_diamondID, address):
    global currentUniqueID
    web3.eth.Eth.default_account = address
    Instance.functions.carveDiamond(pro_mine_diamondID).transact({'from': address, 'gas': 4000000, 'value': Web3.to_wei(0.5, 'ether')})
    MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
    localDB = MongoDB_client['local']
    diamondSet = localDB['diamond']
    diamondSet.update_one({'identification': pro_mine_diamondID}, {'$set': {'diamondStatus': 2, 'unique_id': currentUniqueID, 'currentOwner': address}})
    currentUniqueID += 1
    MongoDB_client.close()

#carveDiamond(1205, '0x6C7f647FcF988e0e7599E30580703244A0afBB1e')

def collectDiamond(diamondID, address):
    web3.eth.Eth.default_account = address
    Instance.functions.collectDiamond(diamondID).transact({'from': address, 'gas':4000000, 'value':Web3.to_wei(0.5, 'ether')})
    MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
    localDB = MongoDB_client['local']
    diamondSet = localDB['diamond']
    diamondSet.update_one({'identification': diamondID}, {'$set': {'diamondStatus': 3, 'identification': diamondID, 'currentOwner': address}})
    MongoDB_client.close()

#collectDiamond(1205, '0x86E59a7010F6124AF2fE5dA487143db97C42298A')

def designDiamond(diamondID, address, uniqueID, privateKey):
    web3.eth.Eth.default_account = address
    Instance.functions.designDiamond(diamondID).transact({'from': address, 'gas': 4000000})
    signature = sign(privateKey, uniqueID)
    uniqueID_Signature[uniqueID-10000] = signature


def transferDiamond(diamondID, newOwner, address):
    web3.eth.Eth.default_account = address
    Instance.functions.transferDiamond(diamondID, newOwner).transact({'from': address, 'gas': 4000000})
    MongoDB_client = pymongo.MongoClient("mongodb://localhost:27017/local")
    localDB = MongoDB_client['local']
    diamondSet = localDB['diamond']
    diamondSet.update_one({'identification': diamondID}, {"$set": {'currentOwner': newOwner}})
    MongoDB_client.close()

# result = viewAllPurchaseableDiamond()
# print(result)