import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler

from flask import Flask, jsonify, render_template_string, request
from flask_cors import CORS

from config import ConfigClass
from lessons import MODULES
from templates import HTML_PAGE
from utils import (
    get_lesson_progress,
    get_module_progress,
    mark_lesson_complete,
    validate_lesson_id,
    validate_module_id,
)

app = Flask(__name__)
app.config.from_object(ConfigClass)

# Enable CORS for API access
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configure logging
if not app.debug and not app.testing:
    if not app.logger.handlers:
        file_handler = RotatingFileHandler(
            'app.log',
            maxBytes=10_000_000,
            backupCount=5
        )
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        ))
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/api/modules')
def get_modules():
    """Get all available learning modules"""
    try:
        summary = []
        for mid, mdata in MODULES.items():
            total_lessons = len(mdata.get("lessons", []))
            progress = get_module_progress(mid, total_lessons)

            summary.append({
                "id": mid,
                "title": mdata["title"],
                "title_te": mdata["title_te"],
                "lesson_count": total_lessons,
                "progress": progress
            })

        app.logger.info(f"Fetched {len(summary)} modules")
        return jsonify(summary), 200

    except Exception as e:
        app.logger.error(f"Error fetching modules: {str(e)}")
        return jsonify({"error": "Failed to fetch modules"}), 500

@app.route('/api/lessons/<module_id>')
def get_lessons(module_id):
    """Get all lessons in a module"""
    try:
        if not validate_module_id(module_id, MODULES):
            app.logger.warning(f"Module not found: {module_id}")
            return jsonify({"error": "Module not found"}), 404

        lessons = MODULES[module_id]["lessons"]
        summary = []

        for lesson in lessons:
            progress = get_lesson_progress(module_id, lesson["id"])
            summary.append({
                "id": lesson["id"],
                "title": lesson["title"],
                "title_meaning": lesson.get("title_meaning", ""),
                "level": lesson.get("level", ""),
                "level_en": lesson.get("level_en", ""),
                "completed": progress.get("completed", False)
            })

        app.logger.info(f"Fetched {len(summary)} lessons from module: {module_id}")
        return jsonify(summary), 200

    except Exception as e:
        app.logger.error(f"Error fetching lessons for module {module_id}: {str(e)}")
        return jsonify({"error": "Failed to fetch lessons"}), 500

@app.route('/api/lesson/<module_id>/<int:lesson_id>')
def get_lesson(module_id, lesson_id):
    """Get a specific lesson"""
    try:
        if not validate_module_id(module_id, MODULES):
            app.logger.warning(f"Module not found: {module_id}")
            return jsonify({"error": "Module not found"}), 404

        if not validate_lesson_id(lesson_id):
            app.logger.warning(f"Invalid lesson ID: {lesson_id}")
            return jsonify({"error": "Invalid lesson ID"}), 400

        lessons = MODULES[module_id]["lessons"]
        for lesson in lessons:
            if lesson["id"] == lesson_id:
                progress = get_lesson_progress(module_id, lesson_id)
                lesson_data = dict(lesson)
                lesson_data["completed"] = progress.get("completed", False)

                app.logger.info(f"Fetched lesson {lesson_id} from module {module_id}")
                return jsonify(lesson_data), 200

        app.logger.warning(f"Lesson {lesson_id} not found in module {module_id}")
        return jsonify({"error": "Lesson not found"}), 404

    except Exception as e:
        app.logger.error(f"Error fetching lesson {lesson_id} from module {module_id}: {str(e)}")
        return jsonify({"error": "Failed to fetch lesson"}), 500


@app.route('/api/progress/<module_id>/<int:lesson_id>', methods=['GET', 'POST'])
def manage_progress(module_id, lesson_id):
    """Get or update lesson progress"""
    try:
        if not validate_module_id(module_id, MODULES):
            app.logger.warning(f"Module not found for progress: {module_id}")
            return jsonify({"error": "Module not found"}), 404

        if not validate_lesson_id(lesson_id):
            app.logger.warning(f"Invalid lesson ID for progress: {lesson_id}")
            return jsonify({"error": "Invalid lesson ID"}), 400

        if request.method == 'POST':
            success = mark_lesson_complete(module_id, lesson_id)
            if success:
                app.logger.info(f"Marked lesson {lesson_id} complete in module {module_id}")
                return jsonify({
                    "status": "success",
                    "message": "Lesson marked as complete",
                    "completed_at": datetime.now().isoformat()
                }), 200
            else:
                app.logger.error(f"Failed to mark lesson {lesson_id} complete in module {module_id}")
                return jsonify({"error": "Failed to save progress"}), 500

        # GET request
        progress = get_lesson_progress(module_id, lesson_id)
        return jsonify(progress), 200

    except Exception as e:
        app.logger.error(f"Error managing progress for lesson {lesson_id} in module {module_id}: {str(e)}")
        return jsonify({"error": "Failed to manage progress"}), 500


@app.route('/api/progress/<module_id>')
def get_module_progress_api(module_id):
    """Get progress for entire module"""
    try:
        if not validate_module_id(module_id, MODULES):
            app.logger.warning(f"Module not found for progress stats: {module_id}")
            return jsonify({"error": "Module not found"}), 404

        total_lessons = len(MODULES[module_id].get("lessons", []))
        progress = get_module_progress(module_id, total_lessons)

        app.logger.info(f"Fetched progress stats for module {module_id}")
        return jsonify(progress), 200

    except Exception as e:
        app.logger.error(f"Error fetching module progress for {module_id}: {str(e)}")
        return jsonify({"error": "Failed to fetch module progress"}), 500


@app.errorhandler(400)
def bad_request(e):
    """Handle bad request errors"""
    app.logger.warning(f"Bad request: {str(e)}")
    return jsonify({"error": "Bad request", "details": str(e)}), 400


@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    app.logger.warning(f"404 Not Found: {request.path}")
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors"""
    app.logger.error(f"500 Internal Error: {str(e)}")
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    port = app.config.get('PORT', 5050)
    debug = app.config.get('DEBUG', False)
    app.logger.info(f"Starting Flask app on port {port} (debug={debug})")
    app.run(debug=debug, port=port,host='0.0.0.0')
