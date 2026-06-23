from fastapi import APIRouter 
import requests



router = APIRouter(prefix="/tools", tags=["Tools"])



header = "token 626c7b10b45a3f6:d0a9f4a23e74485"
@router.get("/items")
def items():
        url = "http://172.26.192.1:8080/api/resource/Item"
        header = "token 626c7b10b45a3f6:f03cf008ef463a8"
        response = requests.get(url, headers={"Authorization": header})

        return response.json()



@router.get("/customers")
def customers():
        url = "http://172.26.192.1:8080/api/resource/Customer"
        header = "token 626c7b10b45a3f6:f03cf008ef463a8"
        response = requests.get(url, headers={"Authorization": header})

        return response.json()

@router.get("/sales/order")
def sales_orders():
        url = "http://172.26.192.1:8080/api/resource/Sales Order"
        header = "token 626c7b10b45a3f6:f03cf008ef463a8"
        response = requests.get(url, headers={"Authorization": header})

        return response.json()


