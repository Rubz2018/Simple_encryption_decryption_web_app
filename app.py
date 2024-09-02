from flask import Flask, request, jsonify, render_template
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

app = Flask(__name__)

# Load RSA keys
def load_keys():
    with open("keys/private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)
    with open("keys/public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())
    return private_key, public_key

private_key, public_key = load_keys()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json['data'].encode('utf-8')
    encrypted = public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return jsonify({'encrypted_data': encrypted.hex()})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_data = bytes.fromhex(request.json['encrypted_data'])
    decrypted = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return jsonify({'decrypted_data': decrypted.decode('utf-8')})

if __name__ == '__main__':
    app.run(debug=True)
