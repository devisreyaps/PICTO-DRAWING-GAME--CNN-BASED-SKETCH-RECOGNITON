# PICTO-DRAWING-GAME--CNN-BASED-SKETCH-RECOGNITON
An interactive drawing game where kids learn to draw with AI feedback!
# 🎨 PICTO - AI Drawing Game with CNN Sketch Recognition

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3-brightgreen.svg?style=for-the-badge&logo=flask&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-AI%20Model-orange.svg?style=for-the-badge&logo=pytorch&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)
![For Kids](https://img.shields.io/badge/For-Kids%20(5+)-pink.svg?style=for-the-badge)

**An interactive AI-powered drawing game where kids learn to draw with positive reinforcement**  
*Like Duolingo for drawing - Only encouragement, no scolding!*

[Demo Video](https://youtu.be/your-demo) • [Report Bug](https://github.com/devisreyaps/PICTO-DRAWING-GAME/issues) • [Request Feature](https://github.com/devisreyaps/PICTO-DRAWING-GAME/issues)

<img src="assets/demo.gif" width="600" alt="Picto Game Demo">

</div>

## 📋 Table of Contents
- [✨ Features](#-features)
- [🎮 Live Demo](#-live-demo)
- [🚀 Quick Start](#-quick-start)
- [🏗️ Architecture](#%EF%B8%8F-architecture)
- [🛠️ Tech Stack](#%EF%B8%8F-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🧠 AI Model Details](#-ai-model-details)
- [📊 Dataset](#-dataset)
- [🔧 API Endpoints](#-api-endpoints)
- [🤝 Contributing](#-contributing)
- [📝 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

## ✨ Features

### 🎯 **Core Features**
- **🤖 Real-time AI Recognition**: CNN model with 84.6% accuracy recognizes drawings instantly
- **📈 Progressive Learning**: 12 categories (apple, cat, house, sheep, tree, airplane, bird, dog, fish, pizza, rabbit, umbrella)
- **⭐ Reward System**: Earn stars based on drawing accuracy (Duolingo-style)
- **👶 Kid-Friendly Design**: Only positive reinforcement - no negative feedback
- **🎨 Interactive Canvas**: Smooth drawing experience with touch support
- **📊 Visual Progress**: Real-time feedback and progress tracking

### 💡 **Unique Selling Points**
- **Positive Psychology**: Designed to build confidence in young learners
- **Instant Feedback**: AI provides immediate, encouraging responses
- **Educational Value**: Develops fine motor skills and creativity
- **Accessible**: Works on desktop, tablet, and mobile browsers
- **No Ads**: Clean, distraction-free learning environment

## 🎮 Live Demo

#### **Step 1: Clone the Repository**
```bash
# Copy and paste this command:
gh repo clone devisreyaps/PICTO-DRAWING-GAME--CNN-BASED-SKETCH-RECOGNITON

# OR if you don't have GitHub CLI:
git clone https://github.com/devisreyaps/PICTO-DRAWING-GAME--CNN-BASED-SKETCH-RECOGNITON.git

# Navigate into the project:
cd PICTO-DRAWING-GAME--CNN-BASED-SKETCH-RECOGNITON

# Install required Python packages:
pip install -r requirements.txt

# Terminal 1 - Start backend:
streamlit run pictai_api.py

# Terminal 2 - Open frontend:
# Double-click htmll.html
