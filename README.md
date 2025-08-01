# 🔒 Phishing URL Detection System

A machine learning-powered web application that analyzes URLs to detect potential phishing websites. Built with Flask and scikit-learn, this tool extracts 30 key features from URLs and uses a trained classifier to determine website safety.

[**View Live Demo**](https://web-production-e5644.up.railway.app//)

---
![Project Screenshot](https://github.com/Aditya-Sai-19/PHISHING-URL-DETECTION/blob/main/project-screenshot.jpg)
![Project Screenshot](https://raw.githubusercontent.com/Aditya-Sai-19/PHISHING-URL-DETECTION/main/project-screenshot-1.png)
---

## ✨ Features

- **Real-time URL Analysis** - Instant phishing detection for any website
- **30+ Security Features** - Comprehensive analysis including domain age, SSL certificates, redirects, and more
- **Interactive Web Interface** - Clean, responsive design with gradient styling
- **Safety Scoring** - Percentage-based safety assessment
- **One-Click Deployment** - Ready for Render, Heroku, or any cloud platform

## 🛠️ Tech Stack

- **Backend**: Python, Flask, scikit-learn
- **ML Model**: Gradient Boosting Classifier
- **Frontend**: HTML5, CSS3, Bootstrap, JavaScript
- **Deployment**: Gunicorn ready

## 🚀 Quick Start

```bash
git clone https://github.com/yourusername/phishing-url-detector.git
cd phishing-url-detector
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000` and start detecting phishing URLs!

## 🔍 How it Works

The system analyzes URLs based on:
- Domain characteristics (age, registration length, subdomains)
- URL structure (length, special characters, redirects)
- Website content (forms, links, scripts)
- Security features (HTTPS, certificates, ports)

## 📊 Model Performance

The trained model achieves high accuracy in detecting phishing attempts by analyzing patterns commonly found in malicious websites.

---

**⚠️ Disclaimer**: This tool is for educational and security awareness purposes. Always exercise caution when visiting unfamiliar websites.
