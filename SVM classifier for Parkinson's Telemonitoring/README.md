
# Parkinson's Telemonitoring & Diagnostic Platform

## 📌 Overview
This repository contains the core classification and diagnostic modules designed for Parkinson's disease telemonitoring. 

## **Note:** 
This is an extraction from a fully developed e-health platform, originally built as a submission for the ***National University Olympiad in Artificial Intelligence & Programming 2026***. 

## 🏗️ Patient Workflow
The platform guides the patient through a comprehensive, multi-step remote examination process before delivering results.

```mermaid
graph LR
    Start([Start]) --> Vocal[Patient performs vocal examination]
    Vocal --> Motor[Patient performs motor examination]
    Motor --> Choose{Choose motor<br>exercise}
    Choose --> Hand[Hand open/close exercise]
    Choose --> Arm[Arm extension exercise]
    Hand --> Quest[Complete diagnostic questionnaire]
    Arm --> Quest
    Quest --> Results[View results]
    Results --> Discuss[Discuss with virtual doctor]
    Discuss --> End([End])

```

## 🧠 Decision Engine Architecture

The final diagnostic decision is powered by a multi-modal AI approach, combining traditional machine learning, computer vision, expert systems, and LLM-based agents.

```mermaid
graph LR
    SVM[SVM classifier] --> FD{Final decision}
    CV[Mediapipe - computer vision inference] --> FD
    Expert[Experta - expert system] --> FD
    LLM[LLM-Based med Agent] --> FD
    
    FD --> Healthy([Healthy])
    FD --> Parkinson([Parkinson])

    style Healthy stroke:#4CAF50,stroke-width:3px
    style Parkinson stroke:#F44336,stroke-width:3px

```

## 📊 Dataset (SVM Module)

The SVM classifier relies on the **Parkinson's Telemonitoring Dataset**, provided by the UCI Machine Learning Repository. It consists of biomedical voice measurements from individuals with early-stage Parkinson's disease.

* **Source:** [Parkinson's Telemonitoring - UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/189/parkinsons+telemonitoring)

## 🛠️ Tech Stack & Methodology

The modeling pipeline is contained within `parkinsons_model.ipynb` and includes data preprocessing, feature selection, and classification using the following stack:

* **Language:** Python 3
* **Data Processing:** `pandas`, `numpy`
* **Machine Learning:** `scikit-learn` (SVC, LinearSVC, PCA, SelectKBest, RFE)
* **Computer Vision:** `mediapipe`
* **Expert System:** `experta`
* **Visualization:** `matplotlib`, `seaborn`

