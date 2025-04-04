import requests
from utils import load_config

BASE_URL = "https://graph.facebook.com/v22.0"

def get_headers():
    token = load_config().get('access_token')
    return {'Authorization': f'Bearer {token}'}

def get_pages():
    res = requests.get(f"{BASE_URL}/me/accounts", headers=get_headers())
    return res.json().get('data', [])

def get_forms(page_id):
    res = requests.get(f"{BASE_URL}/{page_id}/leadgen_forms", headers=get_headers())
    return res.json().get('data', [])

def get_recent_leads(form_id, limit=3):
    res = requests.get(f"{BASE_URL}/{form_id}/leads", params={'limit': limit}, headers=get_headers())
    return res.json().get('data', [])