# 🔐 Password Strength & Crack Time Estimator

A Python-based console tool to analyze password strength and estimate how long it would take to crack it using brute-force techniques. Includes a secure password generator.

## 💡 Features

- ✅ Password strength checker (length, character types)
- ⏳ Crack time estimation (custom logic implemented)
- 🔁 Secure random password generator
- 🖥️ Console-based interface (CLI)
- ✨ Clean, beginner-friendly Python code

## 📸 Demo

🔐 Password Tool 🔐
1. Check password strength and crack time
2. Generate strong password
Choose an option (1 or 2): 1
Enter your password: qwerty
Your password is: Weak ❌
Estimated crack time: 0.00 seconds

🔐 Password Tool 🔐
1. Check password strength and crack time
2. Generate strong password
Choose an option (1 or 2): 2
Enter password length (min 8): 12
Your strong password: A!4rEpfZ9#dL

## ⚙️ How it works

- Password is analyzed by:
  - Length
  - Presence of lowercase, uppercase, digits, symbols
- Based on character variety and length, the tool calculates total brute-force combinations
- It estimates crack time assuming 1 billion guesses per second

## 🧠 What I learned

> This is my first cybersecurity-related project. I implemented the crack time estimation logic myself, and learned how brute-force attacks work in real life.

- Basics of information security
- Brute-force math
- Python logic and string handling
- Working with time and formatting outputs

## 📂 Files

- `password_tool.py` – main program
- `README.md` – this file

## 🛡 Disclaimer

This project is for educational purposes only.  
Do not use it for illegal or unethical activities.

## 📈 Future plans

- Add GUI version (Tkinter)
- Add HaveIBeenPwned API integration
- Turn into a web app with Flask
