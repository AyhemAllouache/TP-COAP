from flask import Flask, render_template, request
from coapthon.client.helperclient import HelperClient


app = Flask(__name__)


COAP_SERVER_IP = '192.168.129.96'

@app.route('/')
def index():

    return render_template('index.html', state='OFF')

@app.route('/led_on', methods=['POST'])
def led_on():
    client = HelperClient(server=(COAP_SERVER_IP, 5683))
    response = client.post('/LED', 'Off')
    #response = send_coap_request('On')
    client.stop()
    return render_template('index.html', state='ON')

@app.route('/led_off', methods=['POST'])
def led_off():
    client = HelperClient(server=(COAP_SERVER_IP, 5683))
    response = client.post('/LED', 'On')
    return render_template('index.html', state='OFF')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)