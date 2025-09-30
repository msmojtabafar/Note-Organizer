
# 📝 Note Organizer

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Flask-black?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-FF5733?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Transformers-DAA520?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Docker-0db7ed?style=for-the-badge&logo=docker&logoColor=white" />
</div>

---

## 🚀 Overview

Note Organizer is a smart web application built with **Flask** that helps you manage, categorize, and summarize your notes automatically.  
It supports **English and Persian**, and can generate short summaries for long texts using **transformers**.

---

## 🌟 Features

- Add, edit, and delete notes with ease.  
- Automatic note summarization using AI.  
- Supports **Persian and English** text.  
- Categorize notes into predefined categories (Work, Study, Personal, Health, Finance, etc.).  
- Search and filter notes by content or category.  
- Responsive and clean interface with editable tasks.  
- Fully containerized with **Docker** for easy deployment.  

---

## 🛠️ Technologies Used

- **Python 3.13**  
- **Flask** for web framework  
- **SQLAlchemy** for database management (SQLite)  
- **Hugging Face Transformers** for text summarization and translation  
- **Docker** for containerization  
- **Bootstrap** (or Tailwind) for frontend styling  

---

## 📂 Project Structure

```
Note Organizer/
├── app.py              # Main Flask application
├── database.db         # SQLite database
├── templates/          # HTML templates (index.html, edit.html)
├── static/             # CSS, JS, images
├── requirements.txt    # Python dependencies
└── Dockerfile          # Docker configuration
```

---

## ⚡ Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/msmojtabafar/Note-Organizer.git
cd Note-Organizer
```

### 2. Install dependencies
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### 3. Run the app
```bash
python app.py
```

Open your browser and go to: `http://localhost:5000`

---

### 4. Docker Deployment (Optional)
```bash
docker build -t note-organizer .
docker run -p 5000:5000 note-organizer
```

---

## 📝 Usage

1. Add a new note with content and select a category.  
2. The AI will automatically summarize your note (supports Persian & English).  
3. Edit or delete notes anytime.  
4. Use search bar and category filters to quickly find your notes.  

---
