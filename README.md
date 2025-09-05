🌍 Ubuntu-Inspired Image Fetcher

“I am because we are” – Ubuntu Philosophy

This project is a Python script that demonstrates how to fetch images from the internet in a way that reflects Ubuntu values of community, respect, sharing, and practicality.

The program asks the user for one or more image URLs, downloads them, and stores them in a folder called Fetched_Images.
It ensures that only valid images are saved, prevents duplicates, and handles errors gracefully without crashing.

✨ Program Highlights

Community → connects to global resources by fetching images from the web.

Respect → handles errors such as broken links or invalid URLs politely.

Sharing → organizes all images into one accessible directory.

Practicality → creates a real tool that can be reused whenever images need to be collected.

📌 Features Implemented

Creates a Fetched_Images folder automatically if it doesn’t exist.

Validates URLs and ensures that the file is really an image (checks Content-Type).

Generates filenames based on content to avoid overwriting or duplicates.

Allows multiple image URLs to be provided at once.

Catches and reports connection problems without stopping the program.

📂 Repository Structure
Ubuntu_Requests/
│
├── ubuntu_fetcher.py   # Main script for fetching images
├── requirements.txt    # Dependencies (requests library)
└── README.md           # Documentation

▶️ How to Use the Program

Clone the repository to your computer:

git clone https://github.com/YOUR-USERNAME/Ubuntu_Requests.git
cd Ubuntu_Requests


Install the required Python library:

pip install -r requirements.txt


Run the program:

python3 ubuntu_fetcher.py


Provide one or more image URLs when prompted:

Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter one or more image URLs (separated by spaces): https://example.com/wallpaper.jpg
✓ Successfully fetched: ab34d2c1_wallpaper.jpg
✓ Image saved to Fetched_Images/ab34d2c1_wallpaper.jpg

Connection strengthened. Community enriched.


Running the Script in Terminal


Fetched Images Stored in Folder


(You can replace these placeholders with your own screenshots after running the program.)

⚙️ Requirements

Python 3.x

Libraries:

requests

To install dependencies manually:

pip install requests

🌐 Extra Improvements (Challenge Tasks)

Support for downloading multiple images at once.

Duplicate detection using file hashing.

Validation of HTTP headers to confirm content type before saving.

Error messages that guide the user instead of breaking execution.

💡 Reflection

This assignment highlights how programming can be connected to philosophy. Just as Ubuntu teaches that a person is a person through other persons, this tool demonstrates that a program is useful through its interaction with resources created and shared by others.

✍️ Author: Ubuntu_Requests Assignment – Python Libraries
