# 🩺 ESMDA: Expert System for Medical Diagnostic Assistance

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io/)


An interactive, production-grade clinical decision support system designed to assist in the rule-based diagnosis and treatment recommendation for common acute conditions (Cold, Flu, Bronchitis, Strep Throat, Sinusitis, Allergies, and Gastroenteritis). 

This system is built using **Python's `experta` framework** to model rule-based expert systems and is deployed as a user-friendly **Streamlit** web application.

---

## 🚀 Live Space
Access the deployed interactive web application here:
👉 **[Expert System For Medical Diagnostic Assistance on Hugging Face](https://huggingface.co/spaces/gmi-univ/Expert-System-for-Medical-Diagnostic-Assistance
)**

---

## 📚 Theoretical Foundation & Source of Truth

The system design, knowledge management, and logical rules implemented in this repository are thoroughly mapped and validated against the academic framework presented in:
* 📄 **[Knowledge Management in ESMDA: Expert System for Medical Diagnostic Assistance](https://www.researchgate.net/publication/256090216_Knowledge_Management_in_ESMDA_Expert_System_for_Medical_Diagnostic_Assistance)**

---

## ⚙️ Core Architecture

This application employs two separate, sequential reasoning engines to isolate diagnostic reasoning from medication prescription guidelines:

### 1. Diagnosis Engine (`DiagnosticMedical`)
Utilizes a Forward Chaining inference engine to match user-reported symptoms against rule definitions for **7 major target conditions**:
* Strep throat bacterial infection
* Flu (influenza)
* Acute Bronchitis
* Allergies
* Gastroenteritis
* Sinusitis
* Cold

### 2. Medication Recommendation Engine (`MedicationRecommendation`)
Recommends drug names, dosage protocols, and clinical warnings depending on:
* **Patient Demographics**: Dynamically scales drug dosages for pediatric patients using a weight-based scaling factor ($\text{Weight} \times \text{Base Dosage}$), while offering standard adult dosages for patients aged 18+.
* **Patient History / Contraindications**: Evaluates answers to safety questions (e.g., penicillin allergies, kidney complications, chronic illnesses) to automatically substitute or filter out high-risk medication groups.

---

## 📦 Installation & Local Setup

### Prerequisites
Make sure you have Python installed (Python 3.8 to 3.10 is recommended for `experta` compatibility).

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/ESMDA-expert-system.git](https://github.com/your-username/ESMDA-expert-system.git)
   cd ESMDA-expert-system


##   ⚠️ Disclaimer
This expert system is designed for educational and clinical research demonstration purposes based on medical reference guidelines. It does not substitute professional medical advice, clinical diagnosis, or physical examination by a qualified healthcare professional.
