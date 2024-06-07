from flask import Flask, render_template
import requests
import socket
import os

app = Flask(__name__)

@app.route("/")
def index():
    original_ip = get_current_ip()
    vpn_ip = test_vpn()
    return render_template("index.html", original_ip=original_ip, vpn_ip=vpn_ip)

def get_current_ip():
    response = requests.get('https://api.ipify.org?format=json')
    data = response.json()
    return data['ip']

def test_vpn():
    # Test VPN functionality and get new IP address
    vpn_ip = get_current_ip()
    if vpn_ip!= original_ip:
        return vpn_ip
    else:
        return "VPN is not working correctly!"

if __name__ == "__main__":
    app.run(debug=True)
