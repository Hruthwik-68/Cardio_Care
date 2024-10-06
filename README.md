Heart Attack Prediction - Cardio Care
Overview
Heart Attack Prediction - Cardio Care is a revolutionary platform designed to reduce the heart attack death rate in India, currently at 33%, through early detection efforts. This platform offers a comprehensive solution for detecting potential heart issues using just a webcam and minimal user input. By leveraging advanced technologies such as Eulerian Video Magnification (EVM)  the platform measures vital parameters such as heart rate, HRV (Heart Rate Variability), blood pressure, oxygen saturation, stress levels, and more.

In addition to these physiological measurements, the platform also considers the user's mental and physical health through a self-assessment questionnaire. The system then generates a detailed report that predicts the probability of a heart attack and provides actionable insights. In critical cases, users can contact a doctor directly through the platform for immediate medical assistance.

Key Features :
1. Webcam-Based Vital Sign Measurement: Use your webcam to measure heart rate, HRV, blood pressure, oxygen saturation, breathing rate, and parasympathetic activity.
2. Stress Level Detection: Analyze stress levels through HRV and Electrodermal Activity (EDA) data using EVM technology.
3. Comprehensive Health Assessment: A self-assessment considering factors such as smoking, alcohol consumption, diabetes, and drowsiness contributes to the user’s overall health score.
4. Detailed Health Report: Generate a graphical and numerical report with vital signs, health scores, and a prediction of heart attack probability.
5. Doctor Connectivity: Easily connect with a doctor in critical cases for immediate medical attention.

Technology Stack :
Frontend: HTML, CSS, JavaScript
Backend: Flask (Python)
Machine Learning: Python (TensorFlow, scikit-learn)
Technologies: Eulerian Video Magnification (EVM), Machine Learning Algorithms

Installation
This project is divided into two main parts: Website and Machine Learning (ML). Both need to be set up and run separately.

Prerequisites
Python 3.10+
Flask
TensorFlow
scikit-learn
OpenCV
Other Python libraries 


1. Clone the Repository
git clone https://github.com/Hruthwik-68/Cardio_Care.git
cd Cardio_Care

Step 1: Setting Up the Website

cd website
Install the required dependencies:

Run the Flask application:

python app.py

The website will be hosted locally at http://127.0.0.1:5000/. You can access it in your browser.

Step 2: Setting Up the Machine Learning Service
Navigate to the ml folder:

cd ../ml
Install the required dependencies:

Run the Machine Learning service:

python app.py
The website will be hosted locally at http://127.0.0.1:3005/. You can access it in your browser.

This service will process the vital signs and health assessments collected from the website.
Usage :  
1. Access the Website: Open the local server URL http://127.0.0.1:5000/ in your browser.
2. Login or Register: Start by registering or logging in.
3. Perform a Scan: Use your webcam to capture vital parameters like heart rate, stress levels, blood pressure, and more.
4. Self-Assessment: Answer the simple health-related questions to generate a comprehensive report.
5. View Report: After the scan and self-assessment, the platform generates a detailed report with health scores and risk analysis.
6. Consult a Doctor: If the system detects a critical condition, you can connect with a doctor through the platform.

Contributing
Contributions are welcome! If you’d like to contribute, please submit a pull request or open an issue on the GitHub repository.

License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.


Contact
For more information or queries, please contact the project owner:

Hruthwik M
[LinkedIn](https://www.linkedin.com/in/hruthwik-m) | [GitHub](https://github.com/Hruthwik-68)

