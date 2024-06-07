import requests
import json
from flask import Flask, jsonify

app = Flask(__name__)

def get_original_ip():
    try:
        response = requests.get('https://api.ipify.org')
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        return "Error: " + str(e)

def get_ip_plan_a():
    try:
        response = requests.get('http://ip.42.pl/raw')
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        return "Error: " + str(e)

def get_ip_plan_b():
    try:
        response = requests.get('https://ipapi.co/ip/')
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        return "Error: " + str(e)

def get_ip_plan_c():
    try:
        response = requests.get('https://api.ipdata.co/ip')
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        return "Error: " + str(e)

@app.route('/get_ip', methods=['GET'])
def get_ip():
    original_ip = get_original_ip()
    plan_a_ip = get_ip_plan_a()
    plan_b_ip = get_ip_plan_b()
    plan_c_ip = get_ip_plan_c()
    return jsonify({'original_ip': original_ip, 'plan_a_ip': plan_a_ip, 'plan_b_ip': plan_b_ip, 'plan_c_ip': plan_c_ip})

if __name__ == '__main__':
    app.run(debug=True)
