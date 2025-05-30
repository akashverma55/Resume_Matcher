from flask import Flask, request, render_template
import os
import PyPDF2 as PDF
import docx2txt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.config['Upload_FOLDER'] = 'uploads/'

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PDF.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text(page)
        return text

def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.txt'):
        return extract_text_from_txt(file_path)
    else:
        return "Unsupported file format"
@app.route('/')
def match():
    return render_template('index.html') 

@app.route('/matcher', methods=['POST'])
def matcher():
    if request.method == 'POST':
        job_description = request.form.get['job_description']
        resume_files = request.form.getlist['resumes']

        resumes = []

        for file in resume_files:
            filename = os.path.join(app.config['Upload_FOLDER'], file.filename)
            file.save(filename)
            resumes.append(extract_text(filename))

        if not job_description or not resume:
            return render_template('index.html', message="Please provide both job description and resume files.")
        
        vectorizer = TfidfVectorizer().fit_transform([job_description]+ resumes)

if __name__ == '__main__':
    app.run(debug=True)

