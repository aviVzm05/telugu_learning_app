# తెలుగు నేర్చుకుందాం — Telugu Learning App
### Interactive Telugu Learning for Students · 8వ తరగతి విద్యార్థులకు

---

## 🌟 Features
- 📚 **Multiple Modules** — Choose between **Short Paragraphs** and **Vemana Satakam** (Poetry).
- 📖 **20 Interactive Lessons** — Carefully selected content for progressive learning.
- 🔊 **Text-to-Speech** — High-quality Telugu audio for paragraphs, poems, and individual words.
- 📝 **Smart Word Meanings** — Hover over any Telugu word to see its meaning and transliteration.
- 🔤 **Pronunciation Guide** — Roman transliteration available for every lesson.
- 💡 **Bilingual Explanations** — Deep-dive meanings (Bhavam) for poems in both Telugu and English.
- ✅ **Progress Tracking** — Save and track your learning progress with persistent storage.
- 📊 **Module Statistics** — View completion percentages for each module.
- 🔐 **CORS Support** — RESTful API with cross-origin resource sharing enabled.
- 📝 **Comprehensive Logging** — Application and error logging with rotating file handlers.
- 🎨 **Modern Aesthetic UI** — Clean, responsive design optimized for desktop learning.

---

## 🚀 How to Run

### Step 1: Install Dependencies
Ensure you have Python 3.8+ installed, then install required packages:
```bash
pip install -r requirements.txt
```

### Step 2: Configure Environment (Optional)
Create a `.env` file in the project root for custom configuration:
```env
FLASK_ENV=development
DEBUG=True
PORT=5050
TTS_VOICE=te-IN
TTS_RATE=180
TTS_VOLUME=0.9
LOG_LEVEL=INFO
```

All variables have sensible defaults, so this step is optional.

### Step 3: Start the Application
Run the main Flask application from the project root:
```bash
python app.py
```

### Step 4: Access the App
Open your web browser and navigate to:
```
http://localhost:5050
```

---

## 🛠️ Project Structure
The project has been refactored for better maintainability and scalability:
- `app.py`: Main Flask server with API endpoints, error handling, and logging.
- `config.py`: Environment-based configuration management.
- `utils.py`: Utility functions for progress tracking, validation, and data operations.
- `lessons.py`: Central manager for all lesson modules.
- `templates.py`: Contains the interactive HTML/CSS/JS frontend.
- `progress_data/`: Directory storing user progress files (JSON-based).
- `telugu_lessons/`: Directory containing lesson data.
  - `short_paras.py`: 10 lessons featuring descriptive paragraphs.
  - `vemana_poems.py`: 10 classic Vemana Satakam poems with detailed explanations.

---

## � Modules Included

### 1. చిన్న పేరాలు · Short Paragraphs
Focuses on reading comprehension with topics like:
- **Our School** (మన పాఠశాల)
- **India** (భారతదేశం)
- **Nature's Beauty** (ప్రకృతి అందాలు)
- ...and more (10 lessons total).

### 2. వేమన శతకం · Vemana Satakam
Classic ethical poetry (Aataveladi) by Yogi Vemana, featuring:
- **Salt and Camphor** (ఉప్పు కప్పురంబు)
- **Quality over Quantity** (గంగిగోవు పాలు)
- **Practice Makes Perfect** (అనగననగ రాగ మతిశయిల్లుచునుండు)
- Detailed **Telugu & English explanations** for every poem.

---

## 🔌 API Endpoints

The application provides a RESTful API for managing lessons and progress. CORS is enabled for all API endpoints.

### Module Endpoints

**GET `/api/modules`**
- Returns all available learning modules with lesson counts and progress
- Response: JSON array of modules with progress statistics

**GET `/api/lessons/<module_id>`**
- Returns all lessons in a specific module with completion status
- Example: `/api/lessons/short_paras`
- Response: JSON array of lessons with metadata

**GET `/api/lesson/<module_id>/<lesson_id>`**
- Returns detailed content for a specific lesson
- Example: `/api/lesson/short_paras/1`
- Response: JSON object with full lesson details

### Progress Endpoints

**GET `/api/progress/<module_id>/<lesson_id>`**
- Retrieves completion status for a lesson
- Returns: `{"completed": boolean, "completed_at": timestamp}`

**POST `/api/progress/<module_id>/<lesson_id>`**
- Marks a lesson as completed
- Returns: Success status with completion timestamp

**GET `/api/progress/<module_id>`**
- Retrieves module-level progress statistics
- Returns: `{"total": number, "completed": number, "percentage": number}`

---

## ⚙️ Configuration

The application supports environment-based configuration through a `.env` file or environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `FLASK_ENV` | `development` | Environment mode (development/production/testing) |
| `DEBUG` | `False` | Enable Flask debug mode |
| `PORT` | `5050` | Server port |
| `LOG_LEVEL` | `INFO` | Logging level (DEBUG/INFO/WARNING/ERROR) |
| `TTS_VOICE` | `te-IN` | Text-to-speech language/voice code |
| `TTS_RATE` | `180` | Speech rate in words per minute |
| `TTS_VOLUME` | `0.9` | Audio volume (0.0-1.0) |
| `SESSION_TYPE` | `filesystem` | Session storage type |
| `SESSION_PERMANENT` | `False` | Make sessions permanent |
| `PERMANENT_SESSION_LIFETIME` | `3600` | Session lifetime in seconds |

### Creating a .env File
Create a `.env` file in the project root to override defaults:
```env
FLASK_ENV=development
DEBUG=True
PORT=5050
LOG_LEVEL=DEBUG
TTS_VOICE=te-IN
TTS_RATE=180
TTS_VOLUME=0.9
```

---

## 📊 Progress Tracking

The application automatically saves user progress to JSON files in the `progress_data/` directory. Each completed lesson is tracked with:
- `completed`: Boolean flag
- `completed_at`: ISO 8601 timestamp
- `module_id`: Module identifier
- `lesson_id`: Lesson identifier

Progress persists across browser sessions and is displayed in the UI with visual progress bars.

---

## 📝 Logging

The application includes comprehensive logging:
- **Development Mode**: Console and file logging at INFO level
- **Production Mode**: File logging at WARNING level
- **Log File**: `app.log` with rotating file handler (10MB max per file, 5 backup files)
- **Format**: `%(asctime)s - %(name)s - %(levelname)s - %(message)s`

All API requests, errors, and important events are logged for debugging and monitoring.

---

## 🎙️ Browser & Audio Notes
- **Best Experience:** Use **Google Chrome** or **Microsoft Edge**.
- **Voice Support:** The app uses the system's native TTS. For the best experience, ensure a Telugu (`te-IN`) voice is installed on your OS.
- **Fallback:** If a Telugu voice is unavailable, the app will gracefully handle audio using available system voices.

---

## 🤝 Contributing
To add new content, create a new module in the `telugu_lessons/` directory and register it in `lessons.py`.

---

## 📦 Dependencies
- **flask** (>=2.3.0): Web framework
- **flask-cors** (>=4.0.0): Cross-origin resource sharing
- **python-dotenv** (>=1.0.0): Environment variable management
- **werkzeug** (>=2.3.0): WSGI utilities and error handling

---

## 🐛 Troubleshooting

**Port Already in Use**
- Change the `PORT` environment variable or kill the process using port 5050

**Telugu Voice Not Playing**
- Ensure your system has Telugu language pack installed
- Check `TTS_VOICE` configuration in `.env`
- Verify browser audio permissions

**Progress Not Saving**
- Check write permissions in the `progress_data/` directory
- Review `app.log` for detailed error messages

