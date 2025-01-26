# PCB Defect Detection System

This repository contains a complete solution for detecting defects on printed circuit boards (PCBs). The system consists of a frontend built with React, Vite, and Tailwind CSS, and a backend powered by Flask and Python. A YOLOv8-based custom model, trained on a PCB defects dataset, is integrated into the backend for defect detection.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Frontend Overview](#frontend-overview)
- [Backend Overview](#backend-overview)
- [Model Details](#model-details)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Frontend**
  - User-friendly interface for uploading PCB images.
  - Real-time defect detection results.
  - Built with React, Vite, and styled with Tailwind CSS.

- **Backend**
  - Handles image uploads and communicates with the YOLOv8 model.
  - Built using Flask for seamless integration.
  - Efficient and scalable architecture.

- **Model Integration**
  - YOLOv8 custom model trained on a Kaggle PCB defects dataset.
  - High accuracy in detecting various PCB defects.

## Technologies Used

### Frontend
- React
- Vite
- Tailwind CSS

### Backend
- Flask
- Python

### Machine Learning
- YOLOv8
- Kaggle dataset for PCB defects

## Setup Instructions

### Prerequisites
- Node.js and npm (for the frontend)
- Python 3.x and pip (for the backend)

### Clone the Repository
```bash
git clone https://github.com/yourusername/pcb-defect-detection.git
cd pcb-defect-detection
```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```
3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Flask server:
   ```bash
   flask run
   ```

### Model Setup
1. Ensure the YOLOv8 custom model weights are saved in the `backend/models` directory.
2. The model will automatically load when the backend is started.

## Frontend Overview
The frontend provides a simple interface for users to upload images of PCBs and view the defect detection results. It is built with React, optimized using Vite, and styled using Tailwind CSS.

## Backend Overview
The backend is built with Flask and handles image processing and communication with the YOLOv8 model. It serves the defect detection results back to the frontend.

## Model Details
- **Dataset**: The model was trained using a PCB defects dataset sourced from Kaggle.
- **Architecture**: YOLOv8, known for its speed and accuracy in object detection tasks.
- **Training**: Custom training was performed to fine-tune the model for detecting specific PCB defects.

## Usage
1. Start both the frontend and backend servers.
2. Open the frontend in your browser (typically at `http://localhost:5173`).
3. Upload an image of a PCB through the interface.
4. View the detection results, including defect types and locations.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork this repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---
Feel free to reach out with any questions or suggestions. Happy coding!

