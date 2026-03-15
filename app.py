from flask import Flask, render_template_string, jsonify
import json
from lessons import LESSONS
from templates import HTML_PAGE

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/api/lessons')
def get_lessons():
    summary = [{"id": l["id"], "title": l["title"], "title_meaning": l["title_meaning"],
                 "level": l["level"], "level_en": l["level_en"]} for l in LESSONS]
    return jsonify(summary)

@app.route('/api/lesson/<int:lesson_id>')
def get_lesson(lesson_id):
    for lesson in LESSONS:
        if lesson["id"] == lesson_id:
            return jsonify(lesson)
    return jsonify({"error": "Lesson not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5050)
