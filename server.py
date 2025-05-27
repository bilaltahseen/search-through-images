from flask import Flask, render_template, request, jsonify, redirect, url_for
from agentic_parser import parse_image_and_add_to_chroma
import os
from chromadb_client import search_chroma

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Add zip to template context
@app.context_processor
def utility_processor():
    return dict(zip=zip)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return redirect(url_for('home'))
    
    file = request.files['image']
    if file.filename == '':
        return redirect(url_for('home'))
    
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        parse_image_and_add_to_chroma(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('home'))
    
    return redirect(url_for('home'))

@app.route('/search', methods=['POST'])
def search_images():
    query = request.form.get('query', '')
    # TODO: Implement actual image search logic
    results = search_chroma(query)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 