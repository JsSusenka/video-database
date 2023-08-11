import os
from flask import Flask, request

uploads_folder = "uploads"

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Zdar cegře'


@app.route('/files')
def files():
    res = []

    for file_path in os.listdir(uploads_folder):
        if os.path.isfile(os.path.join(uploads_folder, file_path)):
            res.append(file_path)

    return res


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f"{uploads_folder}/{f.filename}")
        return 'file uploaded successfully'


if __name__ == "__main__":
    if not os.path.exists(uploads_folder):
        os.mkdir(uploads_folder)
    app.run(host="0.0.0.0", debug=True)
