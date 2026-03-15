# తెలుగు నేర్చుకుందాం — Telugu Learning App
### For Class 8 Students · 8వ తరగతి విద్యార్థులకు

---

## Features
- 📖 **4 Telugu lessons** with real passages from school-level texts
- 🔊 **Text-to-Speech** — reads any paragraph or word aloud in Telugu
- 📝 **Word meanings** — hover over any Telugu word to see its meaning
- 🔤 **Pronunciation guide** — Roman transliteration for every paragraph
- ✅ **Progress tracking** — mark paragraphs as completed
- 🎨 **Beautiful UI** — designed for engagement

---

## How to Run

### Step 1: Install Flask
```bash
pip install flask
```

### Step 2: Start the app
```bash
cd telugu_app
python app.py
```

### Step 3: Open in browser
```
http://localhost:5050
```

---

## How to Use

1. **Choose a lesson** from the left sidebar
2. **Read the Telugu text** — hover over highlighted words to see their meanings
3. **Click "వినండి (Listen)"** to hear the paragraph read aloud in Telugu
4. **Click any word chip** in the word list to hear just that word
5. **Click "Pronunciation Help"** to see how to pronounce the text in Roman script
6. **Click "చదివాను (Done)"** when you've finished a paragraph

---

## Browser Notes
- Works best in **Google Chrome** or **Microsoft Edge**
- Telugu TTS requires `te-IN` voice — available on Chrome on Android/Windows
- On systems without Telugu voice, it falls back to English pronunciation of the Roman script

---

## Lessons Included
| # | Title | Meaning | Level |
|---|-------|---------|-------|
| 1 | మన పాఠశాల | Our School | Easy |
| 2 | భారతదేశం | India | Medium |
| 3 | ప్రకృతి అందాలు | Beauty of Nature | Medium |
| 4 | మన శరీరం | Our Body | Easy |

---

## Adding More Lessons
Edit `app.py` and add entries to the `LESSONS` list following the existing format. Each paragraph needs:
- `telugu` — the Telugu text (max 2 lines)
- `transliteration` — Roman script pronunciation guide
- `translation` — English meaning
- `words` — list of key words with meanings
