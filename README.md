# 🌍 Ubuntu Image Fetcher

> "I am because we are" – Ubuntu Philosophy  

This project is a **Python-based image downloader** inspired by Ubuntu’s principles of **community, respect, and sharing**.  
It fetches images from the web, saves them locally, and organizes them in a `Fetched_Images` directory.  

---

## 🚀 Features
- Fetches images from any valid URL
- Creates a `Fetched_Images/` directory if it doesn’t exist
- Validates **HTTP status codes** and **Content-Type**
- Prevents **duplicate downloads** using content hashing
- Allows **multiple URLs** at once
- Handles errors gracefully

---

## 📂 File Structure

Ubuntu_Requests/
│
├── ubuntu_fetcher.py # Main script
└── README.md # Documentation
---

## ▶️ Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Ubuntu_Requests.git
   cd Ubuntu_Requests

   python3 ubuntu_fetcher.py

   Example interaction:

Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter one or more image URLs (separated by spaces): https://example.com/ubuntu.jpg
✓ Successfully fetched: 3f2a8c1b_ubuntu.jpg
✓ Image saved to Fetched_Images/3f2a8c1b_ubuntu.jpg

Connection strengthened. Community enriched.
Requirements

Python 3.x

Libraries:

requests

Install dependencies with:

pip install requests

✨ Challenge Features

Multiple URLs supported

Content-Type checked (ensures only images are saved)

Duplicate prevention via hashing

Graceful error handling for network issues

"A person is a person through other persons." – Ubuntu Philosophy


---

### **📜 requirements.txt**


requests


---

👉 Steps for you:  

1. On your computer, create a folder `Ubuntu_Requests`  
2. Inside it, paste the **3 files** above (`ubuntu_fetcher.py`, `README.md`, `requirements.txt`)  
3. Push to GitHub with:  
```bash
git init
git add .
git commit -m "Ubuntu Image Fetcher Assignment"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Ubuntu_Requests.git
git push -u origin main
