"""
Utility functions for Telugu Learning App
Handles progress tracking, file operations, and data validation
"""
import json
from datetime import datetime
from pathlib import Path

PROGRESS_DIR = Path("progress_data")
PROGRESS_DIR.mkdir(exist_ok=True)


def get_progress_file(module_id, lesson_id):
    """Get the path to a progress file"""
    return PROGRESS_DIR / f"{module_id}_{lesson_id}.json"


def mark_lesson_complete(module_id, lesson_id):
    """Mark a lesson as completed"""
    progress_file = get_progress_file(module_id, lesson_id)

    data = {
        "completed": True,
        "completed_at": datetime.now().isoformat(),
        "module_id": module_id,
        "lesson_id": lesson_id
    }

    try:
        with open(progress_file, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving progress: {e}")
        return False


def get_lesson_progress(module_id, lesson_id):
    """Get the progress status of a lesson"""
    progress_file = get_progress_file(module_id, lesson_id)

    if progress_file.exists():
        try:
            with open(progress_file) as f:
                return json.load(f)
        except Exception as e:
            print(f"Error reading progress: {e}")

    return {"completed": False}


def get_module_progress(module_id, total_lessons):
    """Calculate progress for a module"""
    completed = 0

    for lesson_id in range(1, total_lessons + 1):
        progress = get_lesson_progress(module_id, lesson_id)
        if progress.get("completed", False):
            completed += 1

    return {
        "total": total_lessons,
        "completed": completed,
        "percentage": int((completed / total_lessons * 100) if total_lessons > 0 else 0)
    }


def validate_module_id(module_id, valid_modules):
    """Validate module ID against available modules"""
    return module_id in valid_modules


def validate_lesson_id(lesson_id):
    """Validate lesson ID"""
    return isinstance(lesson_id, int) and lesson_id > 0


def clear_all_progress():
    """Clear all progress data (for testing/reset)"""
    try:
        for file in PROGRESS_DIR.glob("*.json"):
            file.unlink()
        return True
    except Exception as e:
        print(f"Error clearing progress: {e}")
        return False
