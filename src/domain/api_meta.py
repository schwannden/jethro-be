WEB_DOMAIN_TAGS_METADATA = [
    {
        "name": "User",
        "description": "User domain, created by FastAPI User",
    },
    {
        "name": "Service",
        "description": "Sales Order (銷貨單) domain",
    },
]
RESTFUL_ERROR_RESPONSES = {
    400: {
        "content": {"text/plain": {}},
        "description": "Bad Request (check your request body, query parameter)",
    },
    401: {
        "content": {"text/plain": {}},
        "description": "Unauthorized (your account/request does not contain necessary credential)",
    },
    404: {
        "content": {"text/plain": {}},
        "description": "Not Found (requested resource does not exist)",
    },
    410: {
        "content": {"text/plain": {}},
        "description": "Gone (requested resource has been deleted)",
    },
    500: {
        "content": {"text/plain": {}},
        "description": "Internal Server Error (runtime server error)",
    },
}
