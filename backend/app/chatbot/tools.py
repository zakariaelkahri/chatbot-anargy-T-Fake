from langchain.tools import tool
import requests

from app.core.config import settings


def _frappe_get(resource: str) -> dict:
        if not settings.FRAPPE_AUTH_TOKEN:
                return {"error": "FRAPPE_AUTH_TOKEN is not configured"}

        url = f"{settings.FRAPPE_BASE_URL}/api/resource/{resource}"
        response = requests.get(
                url,
                headers={"Authorization": settings.FRAPPE_AUTH_TOKEN},
                timeout=10,
        )
        response.raise_for_status()
        return response.json()

@tool
def items(query: str) -> dict:
        """
        Fetch ERP items/products. Use ONLY when the user explicitly asks about items or products.
        query: describe what item information is needed (e.g. 'list all items', 'find item SKU001').
        DO NOT call for greetings, small talk, jokes, or anything unrelated to ERP items.
        """
        return _frappe_get("Item")


@tool
def customers(query: str) -> dict:
        """
        Fetch ERP customers. Use ONLY when the user explicitly asks about customers.
        query: describe what customer information is needed (e.g. 'list all customers', 'find customer John').
        DO NOT call for greetings, small talk, jokes, or anything unrelated to ERP customers.
        """
        return _frappe_get("Customer")


@tool
def sales_orders(query: str) -> dict:
        """
        Fetch ERP sales orders. Use ONLY when the user explicitly asks about sales orders.
        query: describe what order information is needed (e.g. 'list sales orders', 'order SO-0001 status').
        DO NOT call for greetings, small talk, jokes, or anything unrelated to ERP sales orders.
        """
        return _frappe_get("Sales Order")

TOOLS = [items, customers, sales_orders]
