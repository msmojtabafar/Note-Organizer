from flask import Flask, render_template, request, redirect, url_for
from models import db, Note
import nltk
from transformers import pipeline

nltk.download('punkt')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

summarizer = pipeline(
    "summarization",
    model="philschmid/bart-large-cnn-samsum",
    tokenizer="philschmid/bart-large-cnn-samsum"
)

CATEGORY_KEYWORDS = {
    "Work": [
        "project", "meeting", "deadline", "client", "task", "office", 
        "پروژه", "جلسه", "مشتری", "مهلت", "کار", "وظیفه"
    ],
    "Personal": [
        "home", "family", "shopping", "personal", "travel", "hobby", 
        "خانه", "خانواده", "خرید", "شخصی", "تفریح", "سفر", "سرگرمی"
    ],
    "Study": [
        "learn", "study", "exam", "course", "lecture", "research", 
        "یادگیری", "مطالعه", "امتحان", "درس", "کلاس", "تحقیق"
    ],
    "Health": [
        "doctor", "exercise", "medicine", "fitness", "diet", 
        "سلامت", "دکتر", "ورزش", "دارو", "تغذیه", "تناسب"
    ],
    "Finance": [
        "budget", "expense", "money", "investment", "finance", 
        "مالی", "هزینه", "درآمد", "سرمایه", "پس انداز"
    ],
    "Shopping": [
        "buy", "purchase", "order", "shopping", 
        "خرید", "سفارش", "محصول"
    ],
    "Entertainment": [
        "movie", "music", "game", "show", 
        "فیلم", "موسیقی", "بازی", "نمایش"
    ],
    "Travel": [
        "trip", "flight", "hotel", "tour", 
        "سفر", "هتل", "پرواز", "تور"
    ],
    "Others": []
}


def categorize_note(content):
    for category, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in content.lower():
                return category
    return "Other"

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    search = request.args.get("search", "")
    category_filter = request.args.get("category", "All")
    
    notes = Note.query
    if search:
        notes = notes.filter(Note.title.contains(search) | Note.content.contains(search))
    if category_filter != "All":
        notes = notes.filter_by(category=category_filter)
    notes = notes.all()
    
    return render_template("index.html", notes=notes, search=search, category_filter=category_filter, categories=["All"] + list(CATEGORY_KEYWORDS.keys()))

@app.route("/add", methods=["POST"])
def add_note():
    title = request.form["title"]
    content = request.form["content"]
    
    category = categorize_note(content)
    summary = content
    if len(content.split()) > 30:
        summary = summarizer(content, max_length=50, min_length=25, do_sample=False)[0]['summary_text']
    
    new_note = Note(title=title, content=summary, category=category)
    db.session.add(new_note)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/edit/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == "POST":
        note.title = request.form["title"]
        note.content = request.form["content"]
        note.category = categorize_note(note.content)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html", note=note)

if __name__ == "__main__":
    app.run(debug=True)
