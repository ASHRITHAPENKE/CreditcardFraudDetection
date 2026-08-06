# 💳 A Scalable Model for Credit Card Fraud Detection Using Human-Centric Features

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Framework-black?style=for-the-badge&logo=flask)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-orange?style=for-the-badge&logo=scikitlearn)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-Academic-red?style=for-the-badge)

</div>

---

# 📖 Project Overview

The rapid growth of digital payment systems, online banking, and e-commerce platforms has significantly increased the volume of credit card transactions worldwide. While these advancements have improved convenience and accessibility, they have also created opportunities for increasingly sophisticated fraud attacks.

Traditional fraud detection systems primarily rely on static rules and predefined thresholds, making them ineffective against evolving fraud patterns and often resulting in high false-positive rates. To address these challenges, this project presents an intelligent and scalable Credit Card Fraud Detection System powered by Machine Learning and Human-Centric Behavioral Analysis.

Unlike conventional approaches that focus only on transaction-level attributes, the proposed system incorporates behavioral features such as spending habits, transaction frequency, transaction velocity, device usage patterns, and anomaly detection signals. These behavioral insights enable the system to distinguish legitimate user behavior from suspicious activities with greater accuracy.

The project also provides an interactive Flask-based web application that allows users to submit transaction details, obtain real-time fraud predictions, and visualize the contribution of important features influencing each prediction.

---

# 🎯 Objectives

The primary objectives of this project are:

- Develop an intelligent fraud detection model capable of accurately classifying fraudulent and legitimate transactions.

- Improve prediction accuracy by integrating behavioral features with traditional transaction attributes.

- Reduce false positive rates to minimize inconvenience caused by incorrectly blocked legitimate transactions.

- Build a scalable architecture suitable for handling high-volume financial transaction environments.

- Provide an interactive web application for real-time fraud prediction.

- Visualize feature importance to improve transparency and explainability of machine learning predictions.

- Design a modular system that can be easily extended with future machine learning algorithms and deployment platforms.

---

# ✨ Key Features

| Feature | Description |
|----------|-------------|
| Real-Time Fraud Detection | Instantly predicts whether a transaction is legitimate or fraudulent. |
| Human-Centric Behavioral Analysis | Uses customer behavioral patterns along with transaction data for better prediction. |
| Interactive Dashboard | Modern Flask web interface with responsive design. |
| Machine Learning Prediction | Utilizes trained machine learning models for classification. |
| Feature Importance Analysis | Displays the most influential features contributing to predictions. |
| Data Preprocessing | Handles normalization, missing values, and feature engineering. |
| Modular Architecture | Easy to maintain and extend with new algorithms. |
| Scalable Design | Suitable for integration into large-scale financial environments. |
| Responsive User Interface | Works across different screen sizes and devices. |
| Visualization Support | Provides graphical analysis of prediction results. |

---

# 🛠 Technology Stack

## Programming Languages

| Technology | Purpose |
|------------|---------|
| Python | Backend development, machine learning implementation, data processing |
| HTML5 | Structure of the web interface |
| CSS3 | Styling and responsive user interface |
| JavaScript | Interactive frontend functionality |

---

## Backend Technologies

| Technology | Purpose |
|------------|---------|
| Flask | Web framework used to build the application and serve prediction requests |
| Jinja2 | Dynamic HTML template rendering |

---

## Machine Learning Technologies

| Technology | Purpose |
|------------|---------|
| Scikit-Learn | Model training, evaluation, preprocessing utilities |
| XGBoost | Supervised fraud classification model |
| Isolation Forest | Behavioral anomaly detection |
| Joblib | Saving and loading trained machine learning models |

---

## Data Processing Libraries

| Library | Purpose |
|----------|---------|
| Pandas | Data loading, preprocessing, manipulation |
| NumPy | Numerical computations |
| SciPy | Scientific computations |
| Imbalanced-Learn | Handling imbalanced datasets |

---

## Visualization Libraries

| Library | Purpose |
|----------|---------|
| Matplotlib | Graph plotting and feature visualization |
| Seaborn | Statistical visualization and performance charts |

---

## Development Tools

| Tool | Purpose |
|------|---------|
| Visual Studio Code | Development environment |
| Git | Version control |
| GitHub | Repository hosting and collaboration |

---

# 💻 Software Requirements

| Component | Specification |
|-----------|---------------|
| Operating System | Windows 10/11, Linux, macOS |
| Programming Language | Python 3.10 or above |
| Backend Framework | Flask |
| Frontend | HTML5, CSS3, JavaScript |
| Machine Learning Framework | Scikit-Learn |
| Data Processing | Pandas, NumPy |
| Model Serialization | Joblib |
| Visualization | Matplotlib, Seaborn |
| IDE | Visual Studio Code |
| Version Control | Git |

---

# 🖥 Hardware Requirements

| Hardware | Minimum Requirement | Recommended |
|----------|---------------------|-------------|
| Processor | Intel Core i5 / AMD Ryzen 5 | Intel Core i7 / AMD Ryzen 7 |
| RAM | 8 GB | 16 GB or Higher |
| Storage | 50 GB Free Space | 256 GB SSD |
| GPU | Integrated Graphics | NVIDIA GPU (Optional) |
| Internet | 10 Mbps | 50 Mbps Broadband |

---

# 📂 Project Directory Structure

```text
Credit-Card-Fraud-Detection/
│
├── core/
│   ├── prediction.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   └── utility.py
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── processed_data.csv
│
├── models/
│   ├── fraud_model.pkl
│   ├── scaler.pkl
│   └── encoder.pkl
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── assets/
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   └── analysis.html
│
├── app.py
├── train_main.py
├── generate_analysis.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 📁 Folder Description

## 📦 core/

The **core** directory contains the primary logic responsible for preprocessing transaction data, extracting behavioral features, loading machine learning models, and generating fraud predictions. These modules separate business logic from the application layer, improving maintainability and code organization.

---

## 📦 data/

The **data** directory stores the datasets used during training, validation, and testing. It may also contain processed datasets generated after feature engineering and preprocessing operations.

---

## 📦 models/

The **models** folder contains serialized machine learning models along with supporting files such as feature scalers and encoders. These files are loaded by the Flask application to perform real-time fraud prediction without retraining the model every time.

---

## 📦 static/

The **static** directory contains all frontend resources including CSS stylesheets, JavaScript files, icons, images, animations, and other assets required by the web application.

---

## 📦 templates/

The **templates** folder contains HTML pages rendered dynamically by Flask using the Jinja2 templating engine. These pages provide the user interface for transaction input, fraud prediction, dashboards, and analysis results.

---

## 📄 app.py

The main entry point of the application. It initializes the Flask server, loads trained models, handles user requests, performs prediction, and renders the appropriate HTML templates.
## 📄 train_main.py

The `train_main.py` file is responsible for training the machine learning model. It loads the dataset, performs preprocessing, applies feature engineering techniques, trains the fraud detection model, evaluates its performance using multiple metrics, and finally saves the trained model for deployment.

### Responsibilities

- Load the training dataset.
- Perform data cleaning.
- Handle missing values.
- Encode categorical variables.
- Normalize numerical features.
- Split dataset into training and testing sets.
- Train Machine Learning models.
- Evaluate performance.
- Save trained models.

---

## 📄 generate_analysis.py

This module generates detailed analytical reports after prediction. It identifies the most influential features responsible for the classification and provides visual explanations through graphs and charts.

### Responsibilities

- Feature importance visualization
- Prediction explanation
- Graph generation
- Analytical reporting
- Transaction contribution analysis

---

# 🏛 System Architecture

The Credit Card Fraud Detection System follows a layered architecture to ensure modularity, scalability, and maintainability.

```
                     ┌──────────────────────┐
                     │      End User        │
                     └──────────┬───────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │   Flask Web Interface  │
                    └──────────┬─────────────┘
                               │
                               ▼
                  ┌──────────────────────────┐
                  │ Transaction Input Module │
                  └──────────┬───────────────┘
                             │
                             ▼
               ┌──────────────────────────────┐
               │ Data Preprocessing Module    │
               └──────────┬───────────────────┘
                          │
                          ▼
          ┌────────────────────────────────────┐
          │ Behavioral Feature Engineering     │
          └─────────────┬──────────────────────┘
                        │
                        ▼
         ┌──────────────────────────────────────┐
         │ Machine Learning Prediction Engine   │
         └─────────────┬────────────────────────┘
                       │
                       ▼
          ┌──────────────────────────────────┐
          │ Fraud Risk Classification Module │
          └─────────────┬────────────────────┘
                        │
                        ▼
         ┌─────────────────────────────────────┐
         │ Feature Importance & Analysis Module│
         └─────────────┬───────────────────────┘
                       │
                       ▼
               ┌─────────────────────┐
               │ Result Dashboard    │
               └─────────────────────┘
```

---

# ⚙ Project Workflow

The project follows a systematic workflow to ensure accurate fraud prediction.

### Step 1 — Data Collection

Historical credit card transaction records are collected and stored for training purposes.

↓

### Step 2 — Data Preprocessing

The collected dataset is cleaned by handling missing values, removing inconsistencies, encoding categorical attributes, and normalizing numerical values.

↓

### Step 3 — Behavioral Feature Engineering

Additional human-centric behavioral features are generated, including:

- Spending habits
- Transaction velocity
- Transaction frequency
- Time-based behavior
- Device consistency
- Historical deviations

↓

### Step 4 — Model Training

The processed dataset is used to train Machine Learning models capable of distinguishing legitimate transactions from fraudulent ones.

↓

### Step 5 — Model Evaluation

The trained model is evaluated using various performance metrics to ensure reliability.

↓

### Step 6 — Model Deployment

The best-performing model is serialized and integrated into the Flask web application.

↓

### Step 7 — Real-Time Prediction

Users submit transaction details through the web interface, and the model predicts whether the transaction is legitimate or fraudulent.

↓

### Step 8 — Feature Importance Analysis

The application explains why a transaction was classified by highlighting the most influential features.

---

# 🧠 Machine Learning Pipeline

```
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Data Preprocessing
   │
   ▼
Feature Engineering
   │
   ▼
Training Dataset
   │
   ▼
Machine Learning Model
   │
   ▼
Model Evaluation
   │
   ▼
Save Model (.pkl)
   │
   ▼
Flask Application
   │
   ▼
Prediction
   │
   ▼
Result Visualization
```

---

# 🚀 Installation Guide

## Step 1 — Clone Repository

```bash
git clone https://github.com/yourusername/credit-card-fraud-detection.git
```

---

## Step 2 — Move into Project

```bash
cd credit-card-fraud-detection
```

---

## Step 3 — Create Virtual Environment

Windows

```bash
python -m venv venv
```

Linux / macOS

```bash
python3 -m venv venv
```

---

## Step 4 — Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

---

## Step 5 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6 — Start Application

```bash
python app.py
```

---

Open Browser

```
http://127.0.0.1:5000
```

---

# ▶ Using the Application

1. Launch the Flask application.

2. Open the application in your browser.

3. Navigate to the Prediction Dashboard.

4. Enter transaction details.

5. Click **Predict Transaction**.

6. Wait for the Machine Learning model to process the request.

7. View the prediction result.

8. Analyze feature contribution graphs.

9. Interpret the fraud risk score.

---

# 🏋 Model Training

To retrain the model with updated datasets:

```bash
python train_main.py
```

The training script performs:

- Dataset loading
- Data preprocessing
- Feature engineering
- Model training
- Model evaluation
- Saving trained models

---

# 📊 Feature Analysis

Generate prediction analysis using:

```bash
python generate_analysis.py
```

This module produces:

- Feature importance plots
- Contribution charts
- Analytical reports
- Visual explanations

---

# 🔍 Prediction Process

The prediction pipeline consists of the following stages:

| Stage | Description |
|--------|-------------|
| Input | User enters transaction details |
| Validation | Input values are validated |
| Preprocessing | Data is normalized and transformed |
| Feature Engineering | Behavioral features are extracted |
| Prediction | Machine Learning model predicts transaction |
| Classification | Transaction marked as Legitimate or Fraud |
| Analysis | Important features are displayed |
| Output | Final prediction shown on dashboard |

---

# 📈 Model Evaluation Metrics

The performance of the fraud detection model is measured using the following metrics.

| Metric | Description |
|---------|-------------|
| Accuracy | Percentage of correctly classified transactions |
| Precision | Measures correctness of fraud predictions |
| Recall | Measures ability to detect fraud cases |
| F1 Score | Harmonic mean of Precision and Recall |
| ROC-AUC Score | Overall classification capability |
| Confusion Matrix | Visual representation of prediction performance |

---

# 📊 Output

The application provides:

- Fraud / Legitimate prediction
- Confidence level
- Transaction analysis
- Feature importance visualization
- Interactive dashboard
- Prediction explanation
# 📂 Dataset Information

The fraud detection model is trained using a structured credit card transaction dataset containing both legitimate and fraudulent transactions. The dataset includes transaction-level attributes and engineered behavioral features to improve prediction accuracy.

### Dataset Characteristics

| Property | Description |
|----------|-------------|
| Dataset Type | Structured Tabular Dataset |
| Domain | Financial Transactions |
| Classification | Binary Classification |
| Target Variable | Fraud / Legitimate |
| Input Features | Transactional & Behavioral Features |
| Output | Fraud Detection |

### Behavioral Features

The proposed system extends traditional fraud detection by incorporating behavioral features such as:

- Spending consistency
- Transaction frequency
- Transaction velocity
- Time-of-day spending pattern
- Merchant interaction history
- Geographic deviation
- Device usage consistency
- Behavioral anomaly score

These features help the model identify deviations from a user's normal spending behavior and improve fraud detection performance.

---

# 📊 Sample Prediction Flow

```text
User Transaction
        │
        ▼
Input Validation
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Machine Learning Model
        │
        ▼
Prediction
        │
 ┌──────┴──────┐
 │             │
 ▼             ▼
Legitimate   Fraud
 │             │
 ▼             ▼
Feature Analysis
 │
 ▼
Dashboard Result
```

---

# 📸 Application Screenshots

## 🔐 Login Page

Displays a secure authentication interface for accessing the fraud detection dashboard.

> *(Add Screenshot Here)*

---

## 🏠 Home Dashboard

Provides an overview of the application, project information, and navigation options.

> *(Add Screenshot Here)*

---

## 💳 Fraud Prediction Interface

Allows users to enter transaction details and perform fraud prediction in real time.

> *(Add Screenshot Here)*

---

## 📈 Feature Importance Analysis

Displays the contribution of the top features influencing the prediction.

> *(Add Screenshot Here)*

---

## ✅ Legitimate Transaction Output

Shows the prediction result for a genuine transaction along with confidence and analysis.

> *(Add Screenshot Here)*

---

## ❌ Fraud Transaction Output

Displays fraudulent transaction detection with visual indicators and feature contribution.

> *(Add Screenshot Here)*

---

# 🌟 Advantages

| Advantage | Description |
|-----------|-------------|
| Higher Accuracy | Improves fraud detection through behavioral analytics. |
| Reduced False Positives | Minimizes incorrect fraud alerts. |
| Explainable Predictions | Displays feature importance for every prediction. |
| Modular Design | Easy to maintain and extend. |
| Scalable Architecture | Suitable for large transaction volumes. |
| Interactive Dashboard | User-friendly and responsive interface. |
| Real-Time Detection | Instant fraud prediction through Flask. |
| Secure Processing | Designed with scalable and secure architecture. |

---

# 🔮 Future Enhancements

The project can be extended with several advanced capabilities to further improve fraud detection performance and usability.

| Enhancement | Description |
|------------|-------------|
| Cloud Deployment | Deploy on AWS, Azure, or Google Cloud Platform. |
| Banking API Integration | Real-time integration with financial systems. |
| Live Transaction Monitoring | Continuous fraud detection for streaming transactions. |
| Email & SMS Alerts | Instant notifications for high-risk transactions. |
| Explainable AI | Integrate SHAP or LIME for advanced interpretability. |
| Deep Learning Models | Implement LSTM, Autoencoders, or Transformer models. |
| Mobile Application | Android and iOS application support. |
| Database Integration | MySQL, PostgreSQL, or MongoDB support. |
| User Authentication | Secure login with role-based access control. |
| REST API | Public API for external system integration. |

---

# 👥 Team Members

| Name | Roll Number |
|------|-------------|
| Penke Ashritha Satyasri | 22A31A43D3 |
| Guthula Sai Sahithi | 22A31A43C3 |
| Gokavarapu Pavan Naga Kumar | 22A31A43E7 |
| Mohammad Khasim Khan | 23A35A4330 |

---

# 👨‍🏫 Project Guide

| Details | Information |
|---------|-------------|
| Guide | Mrs. T. Tejasvi, M.Tech., (Ph.D.) |
| Designation | Assistant Professor |
| Department | Computer Science and Engineering (Artificial Intelligence) |
| Institution | Pragati Engineering College (Autonomous) |

---

# 🏫 Academic Information

| Field | Details |
|-------|---------|
| Project Title | A Scalable Model for Credit Card Fraud Detection Using Human-Centric Features |
| Degree | Bachelor of Technology |
| Department | Computer Science and Engineering (Artificial Intelligence) |
| Institution | Pragati Engineering College (Autonomous) |
| Academic Year | 2025 – 2026 |

---

# 🙏 Acknowledgement

We express our sincere gratitude to our project guide, **Mrs. T. Tejasvi**, for her invaluable guidance, encouragement, and continuous support throughout the development of this project.

We also extend our heartfelt thanks to the Head of the Department, faculty members, and the management of Pragati Engineering College for providing the necessary facilities and motivation to successfully complete this work.

Finally, we thank all team members for their dedication, collaboration, and valuable contributions throughout the project lifecycle.

---

# 📚 References

- Scikit-Learn Documentation
- Flask Documentation
- XGBoost Documentation
- Pandas Documentation
- NumPy Documentation
- Matplotlib Documentation
- Python Official Documentation

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve this project:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Submit a Pull Request.

---

# 📜 License

This project has been developed exclusively for academic and educational purposes as part of the Bachelor of Technology curriculum.

Copyright © 2026

---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

Your support encourages further improvements and future open-source contributions.

---

<div align="center">

## 💳 Thank You for Visiting This Repository

Developed with ❤️ using Python, Flask, and Machine Learning.

</div>
