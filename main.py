from flask import Flask, request, render_template
import os
import PyPDF2 as PDF
import docx2txt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PDF.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or "" # Handle cases where extract_text might return None
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

@app.route('/matcher', methods=['POST','GET'])
def matcher():
    if request.method == 'POST':
        job_description = request.form.get('job_description')
        resume_files = request.files.getlist('resumes')

        resumes = []

        for file in resume_files:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            resumes.append(extract_text(filename))

        if not job_description and not resumes:
            return render_template('index.html', message="Please provide both job description and resume files.")
        
        # Calculate cosine similarity
        vectorizer = TfidfVectorizer().fit_transform([job_description]+ resumes)
        vectors = vectorizer.toarray()
        job_vectors = vectors[0]
        resume_vectors = vectors[1:]

        similarity = cosine_similarity([job_vectors], resume_vectors)[0]
        print("Similarity Scores:", similarity)
        print("--------------------------------------------------------------------")
        print("Job Vectors:", job_vectors)
        print("--------------------------------------------------------------------")
        print("Resume Vectors:", resume_vectors)

        top_indices = similarity.argsort()[-3:][::-1]  # Get indices of top 3 resumes
        top_resumes = [resume_files[i].filename for i in top_indices]
        similarity_scores = [round(similarity[i], 2) for i in top_indices]

        return render_template('index.html', message="Similarity scores calculated successfully.", top_resumes=top_resumes, similarity_scores=similarity_scores)
    
    return render_template('index.html', message="Invalid request method.")


if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)

