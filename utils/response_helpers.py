# response_helpers.py


def success_response(data=None):
    # Placeholder for generating a success API response
    return {"success": True, "data": data}


def error_response(message, status_code=400):
    # Placeholder for generating an error API response
    return {"success": False, "error": message}, status_code
