# 🏋️ REAL-TIME AI GYM COACH

### Your Form. Analyzed. Corrected. In Real Time.

An AI-powered personal fitness trainer that uses **Computer Vision, MediaPipe, and Large Language Models (LLMs)** to analyze exercise movements and provide real-time form correction.

The system tracks body movements through a webcam or smartphone camera, counts exercise repetitions, detects incorrect posture, and provides voice-based coaching feedback.

No expensive fitness equipment required — just your camera and an internet connection.

<p align="center">
  <a href="https://ai-realtime-gymcoaching.netlify.app/">
    🌐 <b>LIVE DEMO</b>
  </a>
  &nbsp; | &nbsp;
  <a href="https://github.com/jadhavaakash41074-dev/AI-Gym-Trainer">
    💻 <b>GITHUB REPOSITORY</b>
  </a>
</p>

---

## 🚀 Project Highlights

| Feature | Description |
|---|---|
| ⚡ Response Time | Approximately 100 ms average latency (project-reported) |
| 🏋️ Exercises | 5+ supported exercises |
| 🎯 Form Accuracy | Up to 95% (project-reported) |
| 📷 Camera | Webcam or smartphone camera |
| 🧠 AI Coaching | Groq-powered feedback |
| 🔊 Voice Feedback | Text-to-Speech using gTTS |

---

## 📌 Key Features

- 🎯 **Real-Time Pose Detection:** MediaPipe detects and tracks body landmarks using a live camera feed.
- 🔢 **Automatic Rep Counter:** Counts exercise repetitions based on body movement and joint angles.
- ✅ **AI Form Correction:** Identifies incorrect exercise posture and provides corrective feedback.
- 🔊 **Voice Coaching:** Generates coaching feedback using Groq and converts it into speech using gTTS.
- 📹 **Live Video Streaming:** Uses WebRTC for real-time video communication.
- 📊 **Workout Monitoring:** Displays exercise repetitions, posture status, and workout progress.
- 📱 **Cross-Device Support:** Accessible through compatible browsers on smartphones and computers.

---

## 🌐 Live Demo

👉 https://ai-realtime-gymcoaching.netlify.app/

Experience AI-powered workout monitoring and real-time exercise feedback.

---

## 🛠️ Tech Stack

| Component | Technology | Version |
|---|---|---|
| Programming Language | Python | 3.x |
| App Framework | Streamlit | 1.54.0 |
| Live Video Streaming | streamlit-webrtc | 0.64.5 |
| Pose Detection | MediaPipe | 0.10.14 |
| Image Processing | OpenCV (Headless) | 4.10.0.84 |
| Data Handling | Pandas | 2.2.3 |
| AI Coaching | Groq SDK | ≥0.12.0 |
| Text-to-Speech | gTTS | 2.5.3 |
| Environment Management | python-dotenv | 1.2.2 |
| Landing Page Hosting | Netlify | — |

### Additional Technologies

- HTML5
- CSS3
- JavaScript
- Git
- GitHub

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/jadhavaakash41074-dev/AI-Gym-Trainer.git
```

### 2. Navigate to the Project Directory

```bash
cd AI-Gym-Trainer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 6. Install System Dependencies (Linux)

If OpenCV shows a GLib or shared-library error, install:

```bash
sudo apt-get update
sudo apt-get install -y libgl1 libglib2.0-0
```

### 7. Configure Groq API Key

Create a `.env` file in the root directory.

```env
GROQ_API_KEY=your_groq_api_key_here
```

**Important:** Never upload your actual API key to GitHub.

For Streamlit Cloud, configure the same secret in the application's Secrets settings.

### 8. Run the Application

```bash
streamlit run main.py
```

Open your browser and visit:

```text
http://localhost:8501
```

---

## 🧠 How It Works

**Step 1: Camera Input**

The application accesses the user's webcam or smartphone camera through the browser.

**Step 2: Live Video Streaming**

WebRTC streams the camera feed to the application.

**Step 3: Pose Detection**

MediaPipe identifies important body landmarks such as shoulders, elbows, hips, knees, and ankles.

**Step 4: Movement Analysis**

The system calculates joint angles and analyzes body movements to identify exercise repetitions.

**Step 5: Form Correction**

Exercise-specific rules and thresholds help identify incorrect posture and movement patterns.

**Step 6: AI Voice Coaching**

Groq generates coaching feedback, while gTTS converts the text into spoken instructions.

**Step 7: Workout Dashboard**

The application displays repetition counts, exercise status, and feedback in real time.

---

## 🏃 Supported Exercises

The following are the currently documented exercise examples:

1. Squats
2. Push-ups
3. Bicep Curls
4. Lunges
5. Shoulder Press

*Note: Confirm the actual supported exercises against the implementation.*

---

## 📊 Application Workflow

```text
       User
        |
        ▼
   Camera Input
        |
        ▼
   WebRTC Streaming
        |
        ▼
  MediaPipe Pose Detection
        |
        ▼
   Body Landmark Tracking
        |
        ▼
    Joint Angle Analysis
        |
        ▼
   Exercise Recognition
        |
        ▼
   Rep Counting & Form Check
        |
        ▼
     Groq AI Coaching
        |
        ▼
      gTTS Voice Feedback
        |
        ▼
    Streamlit Dashboard
```

---

## 🔒 Security

- API keys are stored in environment variables.
- `.env` files are excluded through `.gitignore`.
- `.streamlit/secrets.toml` should never be committed.
- An `.env.example` file can be shared without exposing actual credentials.
- Never publish private API keys or sensitive configuration files.

### Example `.env.example`

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 📸 Screenshots

Add application screenshots and GIF demonstrations in the `static/` folder.

```markdown
![AI Gym Coach Dashboard](static/dashboard.png)

![Real-Time Pose Detection](static/pose-detection.png)
```

---

## 🚀 Deployment

The project uses two deployment platforms:

| Platform | Purpose |
|---|---|
| Netlify | Landing page hosting |
| Streamlit Community Cloud | Streamlit application hosting |

### Deployment Steps

1. Push the project repository to GitHub.
2. Deploy the landing page through Netlify.
3. Deploy the Streamlit application through Streamlit Community Cloud.
4. Configure the required Python dependencies.
5. Add the `GROQ_API_KEY` through Streamlit Secrets.
6. Test camera permissions, video streaming, and AI feedback.

---

## 🔮 Future Enhancements

- Support for more gym exercises.
- Personalized workout recommendations.
- Workout history and progress tracking.
- User profiles and fitness goals.
- Improved posture analysis.
- Exercise difficulty classification.
- More detailed AI-generated coaching.
- Mobile-friendly workout dashboard.
- Performance analytics and workout reports.

---

## 📄 License

This project is intended to be distributed under the **MIT License**.

See the `LICENSE` file for complete license information.

---

## ⭐ Show Your Support

If you find this project useful or interesting, please consider giving it a ⭐ on GitHub.

---

<p align="center">
  <b>🏋️ Train Smarter. Move Better. Improve Your Form with AI!</b>
</p>
