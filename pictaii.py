import streamlit as st
import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
import numpy as np
import os
from streamlit_drawable_canvas import st_canvas

# 🔥 YOUR TRAINED MODEL CLASS
class QuickDrawCNN(nn.Module):
    def __init__(self, num_classes=12):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.dropout = nn.Dropout(0.3)
        
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 64 * 7 * 7)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

# Load model
@st.cache_resource
def load_model():
    model = QuickDrawCNN(12)
    model.load_state_dict(torch.load('quickdraw_proper.pt', map_location='cpu'))
    model.eval()
    return model

model = load_model()
categories = ['apple','cat','house','sheep','tree','airplane','bird','dog','fish','pizza','rabbit','umbrella']

st.title("🎨 AI Drawing Game")
st.write("👉 Draw → 🎯 AI guesses! (84.6% accurate)")

# Create canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0.3)",  # Transparent fill
    stroke_width=20,
    stroke_color="black",
    background_color="white",
    height=280,
    width=280,
    drawing_mode="freedraw",
    point_display_radius=0,
    key="canvas",
)

# AI Prediction Button
if st.button("🎯 AI Check Drawing!", type="primary"):
    if canvas_result.image_data is not None:
        # Convert canvas to PIL Image
        img = Image.fromarray(canvas_result.image_data.squeeze())
        
        # Save temporarily
        img.save("progress/kid_drawing.png")
        
        # 🔥 PROCESS (EXACTLY like Colab)
        kid_img = Image.open("progress/kid_drawing.png").convert('L').resize((28,28))
        kid_array = np.array(kid_img).astype(np.float32) / 255.0
        
        # CRITICAL: INVERT COLORS
        kid_array = 1.0 - kid_array  
        kid_tensor = torch.tensor(kid_array).unsqueeze(0).unsqueeze(0).float()
        
        # Predict
        with torch.no_grad():
            outputs = model(kid_tensor)
            probs = F.softmax(outputs, dim=1)
            top_class_idx = torch.argmax(probs).item()
            confidence = torch.max(probs).item() * 100
        
        # 🎮 KID-FRIENDLY RESULTS
        st.success(f"🎯 **{categories[top_class_idx].upper()}** ({confidence:.0f}% match!)")
        
        col1, col2, col3 = st.columns(3)
        top3 = torch.topk(probs, 3)
        with col1: 
            st.metric("🥇 1st", f"{categories[top3.indices[0][0]]}\n{top3.values[0][0]*100:.0f}%")
        with col2: 
            st.metric("🥈 2nd", f"{categories[top3.indices[0][1]]}\n{top3.values[0][1]*100:.0f}%")
        with col3: 
            st.metric("🥉 3rd", f"{categories[top3.indices[0][2]]}\n{top3.values[0][2]*100:.0f}%")
        
        # Show drawing
        st.image(canvas_result.image_data, caption="Your drawing", width=250)

# Instructions
with st.expander("📖 How to use"):
    st.write("""
    1. **Draw** cat, apple, house, sheep, etc.
    2. **Click** "🎯 AI Check Drawing!"
    3. **See** AI prediction + confidence!
    """)
    
