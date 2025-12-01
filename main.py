from flask import Flask, render_template_string, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

# HTML template with embedded CSS
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>QR Code Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            color: #555;
            font-weight: bold;
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 12px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #45a049;
        }
        .qr-result {
            margin-top: 30px;
            text-align: center;
        }
        .qr-result img {
            max-width: 100%;
            border: 2px solid #ddd;
            border-radius: 5px;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>QR Code Generator</h1>
        <form method="POST" action="/generate">
            <div class="form-group">
                <label for="text_input">Enter text or URL:</label>
                <input type="text" id="text_input" name="text_input" 
                       placeholder="Enter text, URL, or any information..." required>
            </div>
            <button type="submit">Generate QR Code</button>
        </form>
        
        {% if show_qr %}
        <div class="qr-result">
            <h3>Your QR Code:</h3>
            <img src="/qr_image" alt="Generated QR Code">
            <p style="color: #666; margin-top: 10px;">
                <small>QR Code for: {{ user_text }}</small>
            </p>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

# Store the last generated QR code in memory
last_qr_code = None

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, show_qr=False)

@app.route('/generate', methods=['POST'])
def generate():
    global last_qr_code
    
    # Get the text from the form
    text_input = request.form.get('text_input', '')
    
    if text_input:
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text_input)
        qr.make(fit=True)
        
        # Create an image from the QR Code
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save to BytesIO object
        last_qr_code = BytesIO()
        img.save(last_qr_code, 'PNG')
        last_qr_code.seek(0)
        
        return render_template_string(HTML_TEMPLATE, show_qr=True, user_text=text_input)
    
    return render_template_string(HTML_TEMPLATE, show_qr=False)

@app.route('/qr_image')
def qr_image():
    global last_qr_code
    if last_qr_code:
        last_qr_code.seek(0)
        return send_file(last_qr_code, mimetype='image/png')
    return "No QR code generated", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
