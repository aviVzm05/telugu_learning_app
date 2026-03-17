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
- ✅ **Progress Tracking** — Visual progress bars and "Mark as Done" functionality.
- 🎨 **Modern Aesthetic UI** — Clean, responsive design optimized for desktop learning.

---

## 🚀 How to Run

### Step 1: Install Dependencies
Ensure you have Python installed, then install Flask:
```bash
pip install flask
```

### Step 2: Start the Application
Run the main Flask application from the project root:
```bash
python app.py
```

### Step 3: Access the App
Open your web browser and navigate to:
```
http://localhost:5050
```

---

## 🛠️ Project Structure
The project has been refactored for better maintainability:
- `app.py`: Main Flask server and API endpoints.
- `lessons.py`: Central manager for all lesson modules.
- `templates.py`: Contains the interactive HTML/CSS/JS frontend.
- `telugu_lessons/`: Directory containing lesson data.
  - `short_paras.py`: 10 lessons featuring descriptive paragraphs.
  - `vemana_poems.py`: 10 classic Vemana Satakam poems with detailed explanations.

---

## 📖 Modules Included

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

## 🎙️ Browser & Audio Notes
- **Best Experience:** Use **Google Chrome** or **Microsoft Edge**.
- **Voice Support:** The app uses the system's native TTS. For the best experience, ensure a Telugu (`te-IN`) voice is installed on your OS.
- **Fallback:** If a Telugu voice is unavailable, the app will gracefully handle audio using available system voices.

---

## 🤝 Contributing
To add new content, create a new module in the `telugu_lessons/` directory and register it in `lessons.py`.
