from flask import Flask, render_template, request, session
from eddsa import generate_key_pair, sign_message, verify_signature
import binascii

app = Flask(__name__)
app.secret_key = 'super_secret_key'

def generate_or_get_keys():
    if 'private_key' not in session or 'public_key' not in session:
        private_key, public_key = generate_key_pair()
        session['private_key'] = private_key
        session['public_key'] = public_key
    else:
        private_key = session['private_key']
        public_key = session['public_key']
    return private_key, public_key

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    signature = None
    hex_signature = None
    verification_result = None

    if request.method == 'POST':
        message = request.form['message']
        private_key, public_key = generate_or_get_keys()
        original_signature = sign_message(private_key, message)
        hex_signature = binascii.hexlify(original_signature).decode()  # Convert signature to hex
        session['original_signature'] = original_signature  # Store the signature in the session as bytes

    if request.method == 'POST' and 'verify' in request.form:
        original_signature = session.get('original_signature')
        if message and original_signature:
            private_key, public_key = generate_or_get_keys()
            input_signature = binascii.unhexlify(request.form['signature'])  # Get user input signature
            verification_result = verify_signature(public_key, message, input_signature)

    return render_template('index.html', message=message, signature=hex_signature, verification_result=verification_result)

if __name__ == '__main__':
    app.run(debug=True)
