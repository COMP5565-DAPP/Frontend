import json
from django.http import JsonResponse
from . import functions
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password,check_password
import pymongo

@csrf_exempt
def processable_Diamonds(request):
    result = functions.viewAllProcessableDiamonds()
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

@csrf_exempt
def carveable_Diamonds(request):
    result = functions.viewAllCarveableDiamonds()
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

@csrf_exempt
def collectable_Diamonds(request):
    result = functions.viewAllCollectibleDiamond()
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

@csrf_exempt
def designable_Diamonds(request, address):
    result = functions.viewAllDesignableDiamond(address)
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

@csrf_exempt
def purchasable_Diamonds(request):
    result = functions.viewAllPurchaseableDiamond()
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

@csrf_exempt
def owned_Diamonds(request, address):
    result = functions.viewOwnedDiamond(address)
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

@csrf_exempt
def mine_diamonds(request, diamondID, companyNum, address):
    functions.mineDiamond(diamondID, companyNum, address)
    result = functions.getDiamond(address)
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

# old mine version:
# def mine_diamonds(request, diamondID, companyNum,address):
#     functions.mineDiamond(diamondID, companyNum,address)
#     return JsonResponse({"status": "success", "message": "Mined  successfully"})

@csrf_exempt
def process_diamonds(request, diamondID, companyNum, address):
    functions.processDiamond(diamondID, companyNum, address)
    result = functions.getDiamond(address)
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = functions.getCompany(username)

        if user and check_password(password, user['password']):  # 假设密码字段是 'password'
            return JsonResponse({"status": "success!!!", 
                                 "username": user.get('username'),
                                 "role": user.get('role'),
                                 "address":user.get('address')}) 
        else:
            return JsonResponse({"status": "error", "message": "Invalid credentials"}, status=401)

    return JsonResponse({"status": "error", "message": "Only POST method allowed"}, status=405)


# old login version:
# def register(request, companyName, password, address, companyNum, companyType):
#     functions.insertCompany(companyName, password, address, companyNum, companyType)
#     result = functions.getCompany()
#     json_result = json.dumps(result)
#     return JsonResponse(json_result, safe=False)

@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        companyName = data.get('companyName')
        
        if not companyName:
            return JsonResponse({"status": "error", "message": "Company name is required"}, status=400)

        password = data.get('password')
        address = data.get('address')
        userName = data.get('userName')
        companyNum = data.get('companyNum')
        companyType = data.get('companyType')

        hashed_password = make_password(password)

        if functions.insertCompany(userName,companyName, hashed_password, address, companyNum, companyType):
            return JsonResponse({"status": "success", "message": "Company registered successfully"})