from flask import Flask, render_template_string, jsonify, request
import json
from lessons import MODULES
from templates import HTML_PAGE

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/api/modules')
def get_modules():
    summary = []
    for mid, mdata in MODULES.items():
        summary.append({
            "id": mid,
            "title": mdata["title"],
            "title_te": mdata["title_te"]
        })
    return jsonify(summary)

@app.route('/api/lessons/<module_id>')
def get_lessons(module_id):
    if module_id not in MODULES:
        return jsonify({"error": "Module not found"}), 404
    
    lessons = MODULES[module_id]["lessons"]
    summary = [{"id": l["id"], "title": l["title"], "title_meaning": l["title_meaning"],
                 "level": l["level"], "level_en": l["level_en"]} for l in lessons]
    return jsonify(summary)

@app.route('/api/lesson/<module_id>/<int:lesson_id>')
def get_lesson(module_id, lesson_id):
    if module_id not in MODULES:
        return jsonify({"error": "Module not found"}), 404
    
    lessons = MODULES[module_id]["lessons"]
    for lesson in lessons:
        if lesson["id"] == lesson_id:
            return jsonify(lesson)
    return jsonify({"error": "Lesson not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5050)
