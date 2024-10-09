import requests
from flask_login import login_required, current_user
from __init__ import app, db

def trigger_patch():
    patch_api_url = "https://your-patch-management-api/trigger"
    response = requests.post(patch_api_url, json={"action": "patch"})
    return response.json()

@app.route('/trigger-patch', methods=['POST'])
@login_required
def trigger_patch_endpoint():
    if current_user.is_authenticated:
        if current_user.role != 'admin':
            return "Access Denied", 403
        result = trigger_patch()
        return result
