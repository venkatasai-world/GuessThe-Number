# 🎯 Guess The Number Game

A fun and interactive web-based Number Guessing Game built using Flask. The computer randomly selects a number between 1 and 100, and the user must guess the correct number within limited chances.

The game includes difficulty levels and smart hint messages to help the player guess the number correctly.

Built using Python Flask for the backend and HTML, CSS, and JavaScript for the frontend.

---

## 🚀 Features

- Random number generation
- Difficulty levels:
  - Easy Mode
  - Hard Mode
- Limited guessing chances
- Hint system:
  - Very Close
  - Close
  - Too High
  - Too Low
- Interactive gameplay
- Responsive user interface
- Flask-powered backend

---

## 🛠️ Technologies Used

- Python
- Flask
- Flask-CORS
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```bash
GuessThe-Number/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── README.md
```

---

## ▶️ How the Game Works

1. The user selects a difficulty level:
   - Easy → 10 chances
   - Hard → 5 chances

2. The computer randomly generates a number between 1 and 100.

3. The player enters guesses.

4. The game provides hints after each guess:
   - Too High
   - Too Low
   - Very Close
   - Close

5. The player wins by guessing the correct number before running out of chances.

---

## 💻 Example Gameplay

```bash
Select Difficulty: Easy

Guess the number: 50
Result: Too Low

Guess the number: 75
Result: Very Close

Guess the number: 78
🎉 You Win!
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/venkatasai-world/GuessThe-Number.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd GuessThe-Number
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask Application

```bash
python app.py
```

---

## 📌 Requirements

Example `requirements.txt`

```txt
Flask
Flask-Cors
gunicorn
```

---

## 🌐 Render Deployment

This project is fully ready for deployment on Render using Gunicorn.

### Start Command

```bash
gunicorn app:app
```

---

## 🎯 Learning Objectives

This project helps beginners understand:

- Flask Basics
- Session Management
- Random Number Generation
- Frontend and Backend Integration
- JavaScript Fetch API
- Game Logic Development

---

## 🌟 Future Improvements

- Add leaderboard system
- Add multiplayer mode
- Add timer functionality
- Add sound effects and animations
- Improve mobile responsiveness

---

## 🔗 GitHub Repository

:contentReference[oaicite:0]{index=0}

---

## 👨‍💻 Author

Created by Venkata Sai
