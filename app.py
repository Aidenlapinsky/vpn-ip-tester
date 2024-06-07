# app.py (Python Script)
import requests
import socket
import os
import ipaddress

app = Flask(__name__)

@app.route("/")
def index():
    original_ip = get_current_ip_plan_a()
    if original_ip is None:
        original_ip = get_current_ip_plan_b()
    if original_ip is None:
        original_ip = get_current_ip_plan_c()
    
    vpn_ip = test_vpn()
    if vpn_ip is None:
        vpn_ip = test_vpn_alternate()
    
    return render_template("index.html", original_ip=original_ip, vpn_ip=vpn_ip)

def get_current_ip_plan_a():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        data = response.json()
        return data['ip']
    except requests.exceptions.RequestException as e:
        return None

def get_current_ip_plan_b():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except socket.error as e:
        return None

def get_current_ip_plan_c():
    try:
        ip = os.popen("dig +short myip.opendns.com @resolver1.opendns.com").read().strip()
        return ip
    except Exception as e:
        return None

def test_vpn():
    try:
        vpn_ip = get_current_ip_plan_a()
        if vpn_ip != original_ip:
            return vpn_ip
        else:
            return "VPN is not working correctly!"
    except Exception as e:
        return None

def test_vpn_alternate():
    try:
        vpn_ip = get_current_ip_plan_b()
        if vpn_ip != original_ip:
            return vpn_ip
        else:
            return "VPN is not working correctly!"
    except Exception as e:
        return None

if __name__ == "__main__":
    app.run(debug=True)
