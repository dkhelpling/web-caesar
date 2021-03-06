from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form method="POST">
                <label for="base">Rotate by: 
                    <input name="rot" type="text" value="0" />
                    <textarea id="base" name="text">{0}
                    </textarea>
                    <input type="submit" />
                </label

        <!-- create your form here -->
        </body>
    </html
"""

@app.route('/')
def index():
    return form.format('')

@app.route('/', methods=['POST'])
def encrypt():
    l_rot = int(request.form['rot'])
    l_text = str(request.form['text'])

    encrypt_str = rotate_string(l_text, l_rot)
    return form.format(encrypt_str)






app.run()