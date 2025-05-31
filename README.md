# 📝 Resume Matching System

A Flask-based web application that intelligently matches job descriptions with resumes using TF-IDF vectorization and cosine similarity.

---

## 🚀 Features

* ✅ Upload resumes in **PDF, DOCX, or TXT** formats
* ✅ Match resumes using **TF-IDF** and **cosine similarity**
* ✅ Automatically ranks the **top 3 most relevant resumes**
* ✅ Clean, responsive UI built with **Bootstrap**
* ✅ Instant, real-time results – no need to refresh

---

## 💠 Technologies Used

| Layer        | Tools/Packages Used                        |
| ------------ | ------------------------------------------ |
| Backend      | Flask (Python web framework)               |
| NLP          | `scikit-learn` (TF-IDF, Cosine Similarity) |
| File Parsing | `PyPDF2`, `docx2txt`                       |
| Frontend     | HTML5, CSS3, Bootstrap 4                   |
| Other        | Multi-file upload, basic error handling    |

---

## 📆 Project Structure

```
Resume_Matching/
├── main.py                 # Flask app logic
├── requirement.txt         # Python dependencies
├── README.md               # Project documentation
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   ├── style.css           # Custom styles
│   └── style1.css          # Additional styles
├── uploads/                # Uploaded resume files
├── Input_Resume/           # Sample resumes (if any)
└── .gitignore              # Ignore rules
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Resume_Matching
```

### 2. Install Dependencies

```bash
pip install -r requirement.txt
```

### 3. Run the Application

```bash
python main.py
```

---

## 🔍 How It Works

1. **Input**: User enters job description and uploads resumes
2. **Text Extraction**: Text is extracted from PDF, DOCX, or TXT
3. **Vectorization**: All text is vectorized using TF-IDF
4. **Similarity Scoring**: Cosine similarity is calculated between the job and each resume
5. **Ranking**: Top 3 resumes are ranked and displayed with scores

---

## 🧐 Algorithm Details

### 🔹 TF-IDF (Term Frequency–Inverse Document Frequency)

* Captures important words by analyzing term frequency across documents
* Converts unstructured text into numerical vectors

### 🔹 Cosine Similarity

* Measures angle between vector representations
* Score ranges from `0` (no match) to `1` (perfect match)

---

## 🧪 Sample Usage

1. **Start the app**:

   ```bash
   python main.py
   ```

2. **Upload job description and resumes**:

   * Type/paste the job description
   * Upload multiple resumes (PDF, DOCX, or TXT)

3. **View Results**:

   * See the **top 3 most relevant resumes**
   * Each includes a **similarity score**

---

## ✅ To-Do / Future Enhancements

* [ ] Support more file types (e.g., `.odt`, `.rtf`)
* [ ] Add resume parsing for structured fields
* [ ] NER-based skill extraction
* [ ] User accounts with login and dashboard
* [ ] Downloadable results (CSV/Excel)
* [ ] Job-matching explanation feature

---

## 🛠️ Dependencies

```text
flask
PyPDF2
docx2txt
scikit-learn
```

---

## 🐞 Known Issues

* Some PDF files may fail due to complex formatting
* Uploaded resumes are stored temporarily (clean-up recommended)
* Performance may vary with large files or many uploads

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch:

   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add YourFeatureName"
   ```
4. Push and open a Pull Request

---

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

* [Flask](https://flask.palletsprojects.com/)
* [scikit-learn](https://scikit-learn.org/)
* [Bootstrap](https://getbootstrap.com/)
