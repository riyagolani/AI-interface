# AI Visionary - Streamlit Image Generation App

AI Visionary is a **Streamlit-based web app** that generates AI-powered images using **Hugging Face models**. Users can enter a text prompt and generate images dynamically. The app supports customization for different Hugging Face models.

Use this app here: https://ailabinterface.streamlit.app
---

## **🚀 Features**
- Generate AI-generated images from text prompts.
- Supports **Hugging Face Stable Diffusion models**.
- Download generated images.
- Simple and intuitive **Streamlit UI**.

---

## **🛠 Setup & Installation**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/riyagolani/AI-interface.git
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Configure API Key & Model Name**
- Open `app.py` and update the following variables with your Hugging Face API key and desired model name:
  ```python
  HF_API_KEY = "your_hugging_face_api_key"  # Insert your Hugging Face API Key
  MODEL_NAME = "stabilityai/stable-diffusion-xl-base-1.0"  # Insert desired model name
  ```

---

## **▶️ Running the App**
After setup, launch the Streamlit app with:
```sh
streamlit run app.py
```
- The app will start locally on **http://localhost:8501**.

---

## **⚙️ Customizing the Model**
To use different Hugging Face models:
1. **Update the `MODEL_NAME` variable** in `app.py`.
2. Example:  
   ```python
   MODEL_NAME = "runwayml/stable-diffusion-v1-5"
   ```
3. Restart the app.

---

## **🤝 Contributing**
Want to improve AI Visionary? Feel free to fork, modify, and submit a pull request!

---
