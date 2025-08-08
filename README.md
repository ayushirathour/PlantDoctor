# 🌱 Plant Disease Detection API

> **AI-powered plant disease classification using deep learning**

A robust FastAPI-based web service that accurately identifies plant leaf diseases using a pre-trained MobileNetV2 model. Perfect for farmers, gardeners, and agricultural researchers who need quick disease diagnosis.

---

## 👨‍💻 Made with 💚 by Ayushi Rathour

A curious learner exploring the fascinating world of Machine Learning and full-stack development. Always excited to build solutions that make a real-world impact! 🚀

---

## ✨ Features

- **🔬 15 Disease Classes**: Comprehensive coverage of common plant diseases
- **⚡ Lightweight Model**: MobileNetV2 architecture for fast inference
- **🖼️ Built-in Preprocessing**: Automatic image resizing and normalization
- **🚀 Fast API Response**: Optimized for real-time predictions
- **🌐 CORS Enabled**: Ready for frontend integration
- **📊 Confidence Scores**: Get prediction confidence with each result

---

## 🎯 Demo

> *Coming soon: Interactive demo with sample predictions*

![Demo Placeholder](https://via.placeholder.com/800x400/4CAF50/FFFFFF?text=Plant+Disease+Detection+Demo)

---

## 🛠️ Tech Stack

### Backend & API
- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - Lightning-fast ASGI server
- **Python 3.8+** - Core programming language

### Machine Learning
- **TensorFlow/Keras** - Deep learning framework
- **MobileNetV2** - Pre-trained CNN architecture
- **PIL (Pillow)** - Image processing
- **NumPy** - Numerical computations

### Development & Deployment
- **Git** - Version control
- **Docker** - Containerization (optional)
- **Render/Heroku** - Cloud deployment

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone <your-repo-url>
cd plant-disease-detection
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Download the Model
Ensure `plant_disease_model.h5` is in the project root directory.

### Step 4: Run the Application
```bash
uvicorn main:app --reload
```

### Step 5: Access the API
- **API Documentation**: http://127.0.0.1:8000/docs
- **Alternative Docs**: http://127.0.0.1:8000/redoc
- **Health Check**: http://127.0.0.1:8000/

---

## 📡 API Usage

### Endpoint: `POST /predict`

**Request:**
- Method: `POST`
- URL: `http://127.0.0.1:8000/predict`
- Content-Type: `multipart/form-data`
- Body: Form data with key `file` and an image file

**Example using curl:**
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@path/to/your/image.jpg"
```

**Response:**
```json
{
  "class": "Tomato_healthy",
  "confidence": 0.95
}
```

### Supported Image Formats
- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)

---

## 🤖 Model Information

### Dataset
- **Source**: PlantVillage dataset
- **Classes**: 15 different plant disease categories
- **Training Images**: ~54,000+ images
- **Validation Accuracy**: ~83%

### Disease Classes
1. Pepper Bell Bacterial Spot
2. Pepper Bell Healthy
3. Potato Early Blight
4. Potato Late Blight
5. Potato Healthy
6. Tomato Bacterial Spot
7. Tomato Early Blight
8. Tomato Late Blight
9. Tomato Leaf Mold
10. Tomato Septoria Leaf Spot
11. Tomato Spider Mites
12. Tomato Target Spot
13. Tomato Yellow Leaf Curl Virus
14. Tomato Mosaic Virus
15. Tomato Healthy

### Training Details
- **Architecture**: MobileNetV2 (pre-trained)
- **Input Size**: 224x224 pixels
- **Optimizer**: Adam
- **Loss Function**: Categorical Crossentropy
- **Data Augmentation**: Rotation, zoom, flip

---

## ☁️ Deployment

### Deploy on Render (Recommended)

1. **Fork/Clone** this repository to your GitHub account

2. **Create a new Web Service** on Render:
   - Connect your GitHub repository
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

3. **Environment Variables** (if needed):
   ```
   PYTHON_VERSION=3.9
   ```

4. **Deploy!** 🚀

### Alternative: Deploy on Heroku

1. **Add Procfile**:
   ```
   web: uvicorn main:app --host=0.0.0.0 --port=$PORT
   ```

2. **Deploy via Heroku CLI**:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

---

## 🔮 Future Improvements

- [ ] **🌐 Web UI**: Beautiful frontend interface for easy image upload
- [ ] **📱 Mobile App**: React Native or Flutter mobile application
- [ ] **⚡ GPU Acceleration**: Optimize for faster inference with GPU support
- [ ] **📊 Analytics Dashboard**: Track prediction accuracy and usage statistics
- [ ] **🔍 Disease Details**: Add detailed information about each disease
- [ ] **🌱 More Plants**: Expand dataset to include more plant species
- [ ] **📈 Confidence Thresholds**: Implement confidence-based recommendations
- [ ] **🔄 Real-time Training**: Online learning capabilities
- [ ] **📋 Batch Processing**: Handle multiple images simultaneously

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Note**: This project is for educational purposes. Always consult with agricultural experts for professional plant disease diagnosis.

---

## 🙏 Acknowledgments

- **PlantVillage Dataset**: For providing the comprehensive plant disease dataset
- **TensorFlow Team**: For the excellent deep learning framework
- **FastAPI Community**: For the amazing web framework
- **Open Source Community**: For all the amazing tools and libraries

---

## 📞 Contact

**Ayushi Rathour** - [LinkedIn](https://linkedin.com/in/ayushi-rathour) - [GitHub](https://github.com/ayushi-rathour)

Project Link: [https://github.com/ayushi-rathour/plant-disease-detection](https://github.com/ayushi-rathour/plant-disease-detection)

---

⭐ **If this project helped you, please give it a star!** ⭐
