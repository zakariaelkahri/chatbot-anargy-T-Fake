from langchain.tools import tool
import requests

from app.core.config import settings


def _frappe_get(resource: str) -> dict:
        # if not settings.FRAPPE_AUTH_TOKEN:
        #         return {"error": "FRAPPE_AUTH_TOKEN is not configured"}

        url = f"http://192.168.112.1:8080/api/resource/{resource}"
        response = requests.get(
                url,
                headers={"Authorization": "token 626c7b10b45a3f6:f03cf008ef463a8"},
                # timeout=10,
        )
        response.raise_for_status()
        return response.json()

@tool
def out_of_context() -> dict:

        """Use this tool when the user's question is out of context or unrelated to ERP functionality.
        This includes greetings, small talk, jokes, general questions, or anything that doesn't pertain to ERP items, customers, or sales orders.
        Call this tool to handle conversations that fall outside the scope of ERP data retrieval.
        """        
        return "I cannot answer that."



@tool
def customers() -> dict:
        """
        Fetch ERP customers. Use ONLY when the user explicitly asks about customers.
        query: describe what customer information is needed (e.g. 'list all customers', 'find customer John').
        DO NOT call for greetings, small talk, jokes, or anything unrelated to ERP customers.
        """
        return _frappe_get("Customer")

@tool
def items() -> dict:
        """
        Fetch ERP items/products. Use ONLY when the user explicitly asks about items or products.
        query: describe what item information is needed (e.g. 'list all items', 'find item SKU001').
        DO NOT call for greetings, small talk, jokes, or anything unrelated to ERP items.
        """
        return _frappe_get("Item")

@tool
def sales_orders() -> dict:
        """
        Fetch ERP sales orders. Use ONLY when the user explicitly asks about sales orders.
        query: describe what order information is needed (e.g. 'list sales orders', 'order SO-0001 status').
        DO NOT call for greetings, small talk, jokes, or anything unrelated to ERP sales orders.
        """
        return _frappe_get("Sales Order")





TOOLS = [items, customers, sales_orders,out_of_context]
