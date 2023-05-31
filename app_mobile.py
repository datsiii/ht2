import base64

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def handle_request():
    return "Successful Connection"


@app.route('/api/recognize', methods=['GET', 'POST'])
def get_file():
    base64_img = request.form["sample"]
    base64_img_bytes = base64_img.encode('utf-8')
    with open('decoded_image.jpeg', 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)

    '''
    base64_bytes = base64_message.encode('ascii')
    message_bytes = b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    #text = request.form["sample"]
    #print(text)
    '''
    return "received"


app.run(host="0.0.0.0", port=5000, debug=True)
