from langchain.tools import tool
import requests

header = "token 626c7b10b45a3f6:d0a9f4a23e74485"

@tool
def items():
        """Return the list of available items/products."""
        url = "http://172.23.176.1:8080/api/resource/Item"
        header = "token 626c7b10b45a3f6:f03cf008ef463a8"
        response = requests.get(url, headers={"Authorization": header})

        return response.json()


@tool
def customers():
        """Return the list of available customers."""
        url = "http://172.23.176.1:8080/api/resource/Customer"
        header = "token 626c7b10b45a3f6:f03cf008ef463a8"
        response = requests.get(url, headers={"Authorization": header})

        return response.json()


@tool
def sales_orders():
        """Return the list of available sales orders."""
        url = "http://172.23.176.1:8080/api/resource/Sales Order"
        header = "token 626c7b10b45a3f6:f03cf008ef463a8"
        response = requests.get(url, headers={"Authorization": header})

        return response.json()

TOOLS = [items, customers, sales_orders]
