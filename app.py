from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Folder where uploaded images will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check if the upload folder exists, if not, create it
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return 'No selected file'

        # Save the file to the upload folder
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        
        return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
