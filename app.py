from flask import Flask, request, jsonify
from gateway.auth import authenticate
from gateway.encrypt import encrypt_data, decrypt_data
from gateway.storage import upload_file, download_file

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    token = request.headers.get('Authorization')
    if not authenticate(token):
        return jsonify({'error': 'Unauthorized'}), 403
    file = request.files['file']
    encrypted = encrypt_data(file.read(), key='mysecretkey123')
    upload_file(file.filename, encrypted)
    return jsonify({'status': 'Uploaded'})

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    token = request.headers.get('Authorization')
    if not authenticate(token):
        return jsonify({'error': 'Unauthorized'}), 403
    encrypted = download_file(filename)
    decrypted = decrypt_data(encrypted, key='mysecretkey123')
    return decrypted

if __name__ == '__main__':
    app.run(debug=True)
