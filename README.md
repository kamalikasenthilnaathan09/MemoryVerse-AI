# 🧠 MemoryVerse AI
### Intelligent Digital Identity System

<p align="center">
  <img src="system-architecture.png" alt="MemoryVerse AI Architecture" width="900">
</p>

<p align="center">
  <b>An AI-inspired platform that helps students organize, manage, and access their academic and professional documents through a modern digital identity system.</b>
</p>

---

## 📖 Overview

MemoryVerse AI is a web-based Digital Identity System developed to simplify how students manage their academic and professional records.

Throughout their journey, students collect resumes, certificates, internship letters, project reports, and achievements. These documents often become scattered across folders, emails, and cloud storage, making them difficult to locate when needed.

MemoryVerse AI provides a centralized platform where users can securely manage their documents through an intuitive dashboard, making their digital portfolio organized and easily accessible.

---

# ✨ Key Features

### 🔐 User Authentication
- Secure Login & Registration
- Session Management
- User Profile

### 📂 Document Management
- Upload academic and professional documents
- Organize files in one place
- Manage uploaded documents

### 📊 Interactive Dashboard
- User-friendly dashboard
- Quick access to uploaded files
- Clean and responsive interface

### 🔍 Smart Search
- Search documents efficiently
- Organized document listing

### 🕸️ Knowledge Graph
- Visual representation of relationships between documents and categories

### 📅 Digital Timeline
- Displays academic and professional milestones chronologically

### 🤖 AI Assistant Interface
- Dedicated AI assistant page with a modern chat interface

### 📈 Analytics Dashboard
- Visual analytics for uploaded documents
- Interactive charts and statistics

### 👤 Profile Management
- Update personal information
- Manage account details

### ⚙️ Settings
- Application preferences
- Account management

### 📄 Resume Builder
- Dedicated resume builder interface

---

# 🏗️ System Architecture

The application follows a modular Flask architecture.

```
User
   │
   ▼
Frontend (HTML • CSS • JavaScript)
   │
   ▼
Flask Application
│
├── Authentication
├── Dashboard
├── Document Management
├── Profile
├── Analytics
├── AI Assistant
├── Knowledge Graph
└── Timeline
   │
   ▼
SQLite Database
```

---

# 🛠️ Technology Stack

## Frontend
- HTML5
- CSS3
- JavaScript

## Backend
- Python
- Flask

## Database
- SQLite

## Frameworks & Libraries
- Flask
- Jinja2
- SQLAlchemy

---

# 📂 Project Structure

```
MemoryVerse-AI
│
├── database/
├── models/
├── routes/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
├── screenshots/
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
├── Procfile
└── README.md
```

---

# 📸 Application Screenshots

## Landing Page

![Landing Page](screenshots/landing-page.png)

---

## Login

![Login](screenshots/login-page.png)

---

## Register

![Register](screenshots/register-page.png)

---

## Dashboard

![Dashboard](screenshots/dashboard.png)

---

## Documents

![Documents](screenshots/documents.png)

---

## Knowledge Graph

![Knowledge Graph](screenshots/knowledge-graph.png)

---

## Timeline

![Timeline](screenshots/timeline.png)

---

## Smart Search

![Smart Search](screenshots/smart-search.png)

---

## Analytics

![Analytics](screenshots/analytics.png)

---

## AI Assistant

![AI Assistant](screenshots/ai-assistant.png)

---

## Resume Builder

![Resume Builder](screenshots/resume-builder.png)

---

## Profile

![Profile](screenshots/profile-page.png)

---

## Settings

![Settings](screenshots/settings-page.png)

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/kamalikasenthilnaathan09/MemoryVerse-AI.git
```

## Navigate to Project

```bash
cd MemoryVerse-AI
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 🎯 Problem Statement

Students frequently struggle to manage and retrieve important academic and professional documents stored across multiple locations.

MemoryVerse AI addresses this challenge by providing a unified platform that centralizes document storage, improves organization, and enhances accessibility through a modern dashboard and intelligent user experience.

---

# 🚀 Future Enhancements

- OCR-based document text extraction
- AI-powered document categorization
- Semantic document search
- Knowledge graph automation
- Resume parsing
- Embedding-based retrieval
- RAG-powered AI Assistant
- Cloud storage integration
- Mobile application
- Voice-enabled search

---

# 🏆 Hackathon Information

**Project:** MemoryVerse AI – Intelligent Digital Identity System

Developed as a prototype for the **MemoryVerse AI '26 Hackathon**, focusing on creating a centralized platform for managing students' academic and professional digital identities.

---

# 👩‍💻 Developer

**Y. S. Kamalika**

**B.Tech – Artificial Intelligence & Data Science**

---

# 📄 License

This project is developed for educational and hackathon purposes.

---

<p align="center">
⭐ If you found this project interesting, consider giving it a star on GitHub!
</p>
