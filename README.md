# 🔧 Predictive Maintenance using Real-Time Sensor Data (GCP)

This project demonstrates an end-to-end **machine learning pipeline** for **predictive maintenance** using real-time simulated sensor data. It uses **Google Cloud Platform (GCP)** services such as **Pub/Sub**, **Dataflow (Apache Beam)**, **BigQuery**, **Vertex AI**, and **Looker Studio**.

---

## 🚀 Objective

To predict potential machine failures based on live sensor data (temperature, vibration, pressure) and visualize the health of machines in real time.

---

## 🧰 Tech Stack

- **Google Cloud Pub/Sub** – Real-time message ingestion
- **Apache Beam + Dataflow** – Stream processing
- **BigQuery** – Data warehouse for storage and analytics
- **Vertex AI** – Model training and deployment
- **Cloud Storage** – Model and intermediate data storage
- **Looker Studio** – Visualization
- **Python** – Data simulation, ML modeling

---

## 📁 Project Structure

predictive-maintenance-ml/ ├── data_simulation/ │ └── simulate_data.py # Simulates sensor data to Pub/Sub │ ├── beam_pipelines/ │ ├── ingest_to_bq.py # Pub/Sub → BigQuery raw data │ └── predict_and_store.py # Pub/Sub → ML Endpoint → Predictions in BigQuery │ ├── notebooks/ │ └── train_model_vertexai.ipynb # Train model in Vertex AI Workbench │ ├── model/ │ └── model.pkl # Trained model file │ ├── dashboards/ │ └── looker_studio_dashboard.json # Dashboard definition (optional export) │ └── README.md

yaml
Copy
Edit

---

## 📌 Step-by-Step Guide

### 🔹 1. Environment Setup
- Create a GCP project
- Enable the following APIs:
  - Pub/Sub
  - Dataflow
  - BigQuery
  - Vertex AI
  - Cloud Storage

### 🔹 2. Simulate Sensor Data
Run `simulate_data.py` to generate messages like:

```json
{
  "timestamp": 1713104567,
  "machine_id": 2,
  "temperature": 82.4,
  "vibration": 3.15,
  "pressure": 6.7
}
These are published to a Pub/Sub topic (sensor-data-topic).

🔹 3. Stream Data to BigQuery
Use ingest_to_bq.py to:

Read from Pub/Sub

Parse JSON

Store raw sensor data in a BigQuery table: raw_sensor_data

🔹 4. Train ML Model
Open the notebook train_model_vertexai.ipynb

Load data from BigQuery

Train a model (e.g., Random Forest)

Export model as model.pkl to Cloud Storage

🔹 5. Deploy Model to Vertex AI
Upload the model using the following:

bash
Copy
Edit
gcloud ai models upload ...
gcloud ai endpoints create ...
gcloud ai endpoints deploy-model ...
Save the endpoint URL.

🔹 6. Real-Time Prediction
Run predict_and_store.py:

Read from Pub/Sub

Call deployed Vertex AI model

Store prediction result in BigQuery table: prediction_results

🔹 7. Visualization
Connect Looker Studio to your BigQuery tables and create:

Live prediction dashboards

Sensor trends

Failure heatmaps

🧠 Sample Model Inputs
timestamp	machine_id	temperature	vibration	pressure
1713104567	3	84.5	2.1	6.2
📊 Sample Prediction Output
timestamp	machine_id	failure_risk
1713104567	3	0.92
✅ Future Enhancements
Include more features (humidity, power cycles, etc.)

Retraining pipeline using Cloud Composer

Add anomaly detection

🧑‍💻 Author
Mayur Pallakki
Data Engineer & ML Enthusiast

📜 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

Let me know if you want:
- A downloadable `.md` file version
- Custom GitHub repo setup
- Docs in PDF or DOCX format

Happy building 🚀
