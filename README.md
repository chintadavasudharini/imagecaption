# 🚀 PixCaption AI

### Lightweight AI-Powered Image Captioning System using BLIP

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge\&logo=streamlit)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=for-the-badge)
![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-orange?style=for-the-badge\&logo=pytorch)
![AI](https://img.shields.io/badge/AI-Image%20Captioning-green?style=for-the-badge)

---

## 📌 Overview

PixCaption AI is a lightweight Image Captioning Application that automatically generates meaningful captions from uploaded images using the BLIP (Bootstrapping Language-Image Pretraining) model developed by Salesforce.

The application combines Computer Vision and Natural Language Processing to understand image content and generate human-like descriptions in real time.

Designed for CPU-friendly environments, the project can be deployed easily on free cloud platforms such as Render without requiring expensive GPU resources.
<img width="1920" height="920" alt="image" src="https://github.com/user-attachments/assets/452cdee5-7c3f-433b-b86f-3491cc6826c3" />
<img width="1920" height="919" alt="image" src="https://github.com/user-attachments/assets/366267a3-c67e-4bde-a4d6-ef1613fdb373" />


---

## 🎯 Problem Statement

Understanding visual content and converting it into meaningful natural language descriptions is a challenging AI problem.

Traditional image captioning systems often require:

* Large GPU resources
* Heavy models
* High deployment costs

PixCaption AI solves this by providing:

✅ Lightweight Architecture

✅ Fast Inference

✅ CPU-Based Deployment

✅ User-Friendly Interface

✅ Low Operational Cost

---

## ✨ Features

### Core Features

* Upload JPG and PNG Images
* AI-Powered Caption Generation
* Real-Time Processing
* Lightweight BLIP Model
* Clean Streamlit Interface
* Cloud Deployment Ready

### Technical Features

* Transformer-Based Caption Generation
* Vision-Language Model Integration
* Efficient Image Processing
* Cached Model Loading
* Low Memory Consumption
* CPU Optimized Inference

---

## 🏗️ System Architecture

```text
User Uploads Image
        │
        ▼
  Streamlit Frontend
        │
        ▼
 Image Preprocessing
        │
        ▼
BLIP Vision Encoder
        │
        ▼
Transformer Decoder
        │
        ▼
Caption Generation
        │
        ▼
 Display Result
```

---

## 🧠 AI Model

### BLIP (Bootstrapping Language-Image Pretraining)

Model Used:

```python
Salesforce/blip-image-captioning-base
```

BLIP is a Vision-Language Transformer Model that combines:

* Computer Vision
* Natural Language Processing
* Transformer Architecture

to generate context-aware image descriptions.

### Why BLIP-base?

| Feature         | Benefit |
| --------------- | ------- |
| Lightweight     | ~200MB  |
| CPU Friendly    | Yes     |
| Fast Inference  | Yes     |
| High Accuracy   | Yes     |
| Easy Deployment | Yes     |

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & Machine Learning

* Hugging Face Transformers
* PyTorch

### Image Processing

* Pillow (PIL)

### Version Control

* Git
* GitHub

### Deployment

* Render

---

## 📂 Project Structure

```text
PixCaption-AI/
│
├── app.py
├── requirements.txt
├── render.yaml
├── README.md
│
├── assets/
│
└── screenshots/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/chintadavasudharini/PixCaption-AI.git
cd PixCaption-AI
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## ☁️ Deployment on Render

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

---

## 📈 Future Enhancements

### Version 2

* Caption History
* Download Caption Feature
* Multi-Language Captions
* Voice Narration
* OCR Text Recognition
* Object Detection

### Version 3

* BLIP-2 Integration
* Vision-Language Chatbot
* Image-to-Story Generation
* Advanced Scene Understanding

---

## 🎓 Learning Outcomes

This project helped in understanding:

* Computer Vision
* Deep Learning
* Transformer Architecture
* Vision-Language Models
* Hugging Face Ecosystem
* Model Deployment
* Streamlit Development
* Cloud Deployment
* MLOps Fundamentals

---

## 📸 Application Screenshot

Add your application screenshot here:

```text
screenshots/homepage.png
```

---

## 🤝 Contributions

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author & Contact Information

### Chintada Vasudharini

Python Full Stack Developer | AWS | AI-ML

📍 KL University | B.Tech Computer Science Engineering

- **GitHub:** [@chintadavasudharini](https://github.com/chintadavasudharini)
- **LinkedIn:** [Chintada Vasudharini](https://www.linkedin.com/in/chintada-vasudharini-nov21/)
- **Email:** [chintadavasudharini@gmail.com](mailto:chintadavasudharini@gmail.com)
- **Personal Portfolio:** [Visit Here](https://portfolio-lime-tau-36.vercel.app/)


---

⭐ If you found this project useful, consider giving it a star on GitHub!
