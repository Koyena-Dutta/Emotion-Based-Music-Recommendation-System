🎵 Emotion-Based Spotify Music Recommender
📌 Project Overview

This project is a real-time Emotion-Based Music Recommendation System that uses facial emotion recognition to suggest Spotify playlists according to the user's mood. It captures live video through a webcam, analyzes facial expressions using DeepFace, detects the dominant emotion, and automatically opens a corresponding Spotify playlist in the browser.
The system first observes the user's face for a few seconds, stabilizes the detected emotion using smoothing logic, then selects a single final emotion and opens a playlist suited to that mood — preventing continuous switching every second.

💡 Features

🎥 Live webcam emotion detection
🧠 AI-powered facial emotion recognition (DeepFace)
🎶 Automatic Spotify playlist recommendation
⏳ Emotion stabilization to avoid rapid changes
✅ Works offline except for Spotify redirection
🔁 Smooth emotion averaging for accuracy

🛠 Technologies Used

Python
OpenCV
DeepFace
NumPy
Webbrowser module
Spotify Web Links

📂 Project Structure
emotion-music-recommender/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── assets/

⚙️ How It Works

Webcam captures your face in real-time.
DeepFace analyzes facial expressions.
System collects emotions for a few seconds.
Most frequent emotion is selected.
Spotify playlist opens based on final detected mood.

🚀 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/emotion-music-recommender.git
cd emotion-music-recommender

2️⃣ Create Virtual Environment
python -m venv venv


Activate it:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Project
python main.py


✔ Camera will open
✔ Show your emotion
✔ After analysis, Spotify playlist will auto-launch

Press Q to quit.

📋 Requirements

Make sure these are installed:
Python 3.8+
Webcam
Internet connection (for Spotify)

📦 Dependencies (requirements.txt)

Example:

opencv-python
deepface
tensorflow
numpy
Pillow

🔐 Important Notes

Do NOT upload your venv folder to GitHub.
Ensure camera permissions are enabled.
Spotify login may be required in browser.

📸 Output Example

Emotion Displayed: Happy
Result: Spotify Happy Playlist Opens 🎉


📄 License
This project is for academic and learning purposes and does require license to access it.
