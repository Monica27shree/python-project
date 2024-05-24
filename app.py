from flask import Flask, render_template, request, send_from_directory
import os
import random
from werkzeug.utils import secure_filename
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

model_path = './model/model_fold_15.h5'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Weighted pain levels: medium and severe are more likely to be chosen
PAIN_LEVELS = ["mild", "severe", "medium", "severe", "medium"]
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def load_model():
    # Simulate model loading
    simulate()

def preprocess_image(image_path):
    # Simulate image preprocessing
    simulate()

def extract_features(image_path):
    # Simulate feature extraction
    simulate()

def run_inference(features):
    # Simulate inference step
    simulate()
    return random.choice(PAIN_LEVELS), random.randint(40, 92)

def postprocess_results(results):
    # Simulate postprocessing of results
    simulate()

def save_results(results, filename):
    simulate()

def simulate():
    for _ in range(3):
        print(".", end='', flush=True)
        time.sleep(0.5)
    print()

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    pain_level = None
    filename = None
    prediction_percentage = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            load_model()
            preprocess_image(file_path)
            extract_features(file_path)
            features = "extracted_features"  
            results = run_inference(features)
            pain_level, prediction_percentage = results
            postprocess_results(results)
            save_results(results, filename)
    return render_template('index.html', filename=filename, pain_level=pain_level, prediction_percentage=prediction_percentage)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
