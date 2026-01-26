# PICTO-DRAWING-GAME--CNN-BASED-SKETCH-RECOGNITON
An interactive drawing game where kids learn to draw with AI feedback!

</div>

## ✨ Features

### 🎯 **Core Features**
- **🤖 Real-time AI Recognition**: CNN model with 84.6% accuracy recognizes drawings instantly
- **📈 Progressive Learning**: 12 categories (apple, cat, house, sheep, tree, airplane, bird, dog, fish, pizza, rabbit, umbrella)
- **⭐ Reward System**: Earn stars based on drawing accuracy (Duolingo-style)
- **👶 Kid-Friendly Design**: Only positive reinforcement - no negative feedback
- **🎨 Interactive Canvas**: Smooth drawing experience with touch support
- **📊 Visual Progress**: Real-time feedback and progress tracking
### 🤖 AI & Technical Features
CNN Model with 84.6% Accuracy: Trained on Google QuickDraw dataset

Fast Inference: <100ms response time for drawing recognition

Image Preprocessing: Automatic resizing, normalization, and augmentation

Confidence Scoring: Detailed breakdown of prediction probabilities

Multi-class Support: Can recognize and differentiate between all 12 categories
##  System Architecture Diagram

┌─────────────────┐     HTTP/JSON     ┌─────────────────┐     Inference     ┌─────────────────┐
│                 │                   │                 │                   │                 │
│  Frontend       │◄────────────────► │  Flask Backend  │◄────────────────► │  PyTorch CNN    │
│  (Browser)      │   Base64 Images   │  (Python)       │   Tensor Data     │  Model          │
│                 │                   │                 │                   │                 │
├─────────────────┤                   ├─────────────────┤                   ├─────────────────┤
│ • HTML5 Canvas  │                   │ • REST API      │                   │ • 84.6% Acc     │
│ • Vanilla JS    │                   │ • CORS Handling │                   │ • 12 Categories │
│ • CSS3 Animations│                  │ • Image Preproc │                   │ • 2.5MB Size    │
└─────────────────┘                   └─────────────────┘                   └─────────────────┘
🧠 AI Model Details
Model Performance
Metric	       Value	           Description
Accuracy	      84.6%	            On test dataset
Inference Time	< 100ms	          Per drawing
Model Size	    2.5 MB	          Disk space
Classes	        12	              Drawing categories


## Training Details
Dataset: Google QuickDraw (12 categories, 120K samples)

Train/Test Split: 80/20

Optimizer: Adam with learning rate 0.001

Loss Function: CrossEntropyLoss

Epochs: 50 with early stopping

Batch Size: 64


## 🎮 Live Demo
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
