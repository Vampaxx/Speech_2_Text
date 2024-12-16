import os
import time
import threading
from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify, send_from_directory,render_template
from Speech_2_Text.pipeline.stage_02_converting_text import DataProcessingPipeline

app = Flask(__name__)


UPLOAD_FOLDER           = 'static\\uploads'
TRANSCRIPTION_FOLDER    = 'static\\transcriptions'
ALLOWED_EXTENSIONS      = {'wav', 'mp3'}
app.config['UPLOAD_FOLDER']         = UPLOAD_FOLDER
app.config['TRANSCRIPTION_FOLDER']  = TRANSCRIPTION_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER,exist_ok=True)
if not os.path.exists(TRANSCRIPTION_FOLDER):
    os.makedirs(TRANSCRIPTION_FOLDER, exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/save_file', methods=['POST'])
def save_file():
    if 'audioFile' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['audioFile']
    if file:
        file_path   = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        return jsonify({"message": f"File saved at {file_path}"}), 200

    return jsonify({"error": "File save failed"}), 500

@app.route('/process_audio', methods=['POST'])
def process_audio():
    file_path = request.json.get('filePath')
    print(file_path)
    
    if not file_path:
        return jsonify({"error": "No file path provided"}), 400
    
    # Create an instance of DataProcessing
    obj     = DataProcessingPipeline()
    print(obj.main())


    return jsonify({"message": "Audio processed and transcription saved"}), 200




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
