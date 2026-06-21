from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import io
import base64
import os

app = Flask(__name__)
CORS(app, origins=[
    'https://devisreyaps.github.io',
    'http://localhost:5000',
    'http://localhost:8000',
    'https://picto-game-devi.onrender.com'
])# Enable CORS for all routes

# YOUR MODEL CLASS (unchanged)
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

# Load model ONCE
print("🔥 Loading your 84.6% model...")
model = QuickDrawCNN(12)
model_path = os.path.join(os.path.dirname(__file__), 'quickdraw_proper.pt')
model.load_state_dict(torch.load(model_path, map_location='cpu'))
model.eval()
categories = ['apple','cat','house','sheep','tree','airplane','bird','dog','fish','pizza','rabbit','umbrella']
print("✅ Backend ready on http://localhost:5000")

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'model': 'QuickDrawCNN', 'categories': categories})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        if not data or 'image_base64' not in data:
            return jsonify({'error': 'No image data provided'}), 400
        
        # Extract base64 data (remove data:image/png;base64, prefix if present)
        img_data = data['image_base64']
        if ',' in img_data:
            img_data = img_data.split(',')[1]
        
        img_data = base64.b64decode(img_data)
        img = Image.open(io.BytesIO(img_data)).convert('L').resize((28, 28))
        
        # Convert to numpy array and normalize
        kid_array = np.array(img).astype(np.float32) / 255.0
        kid_array = 1.0 - kid_array  # Invert: white background to black
        
        # Convert to tensor
        kid_tensor = torch.tensor(kid_array).unsqueeze(0).unsqueeze(0).float()
        
        with torch.no_grad():
            outputs = model(kid_tensor)
            probs = F.softmax(outputs, dim=1)
            top_class_idx = torch.argmax(probs).item()
            confidence = torch.max(probs).item() * 100
            
            # Check target if provided
            target = data.get('target', '').lower()
            target_idx = categories.index(target) if target in categories else -1
            target_confidence = probs[0][target_idx].item() * 100 if target_idx >= 0 else 0
        
        print(f"🎯 Predicted: {categories[top_class_idx]} ({confidence:.1f}%)")
        
        response = {
            'prediction': categories[top_class_idx],
            'confidence': float(confidence),
            'all_predictions': [
                {'category': cat, 'probability': float(prob * 100)}
                for cat, prob in zip(categories, probs[0].tolist())
            ]
        }
        
        if target_idx >= 0:
            response['target_match'] = float(target_confidence)
            response['target'] = target
            response['is_correct'] = categories[top_class_idx] == target
        
        return jsonify(response)
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify({'categories': categories})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
