# Parkinson's Telemonitoring & Diagnostic Platform

## 📌 Overview
This repository contains the core classification and diagnostic modules designed for Parkinson's disease telemonitoring. 

**Note:** This is an extraction from a fully developed e-health platform, originally built as a submission for the **National University Olympiad in Artificial Intelligence & Programming**. 

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