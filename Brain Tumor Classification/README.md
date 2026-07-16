# 🧠 Brain Tumor MRI Classification with MRI-Specific Physics Augmentations

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![TensorFlow 2.x](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://tensorflow.org)
[![HuggingFace Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-yellow.svg)](https://huggingface.co/spaces/GMI-AI/brain-tumor-classifier)

An end-to-end medical deep learning project that classifies brain tumors from MRI scans into four distinct categories. This repository features a custom **MRI Physics-Aware Augmentation Engine** that simulates clinical scanner artifacts (k-space corruption, bias fields, ghosting, and motion) alongside state-of-the-art Transfer Learning architectures.

---

## 🚀 Live Demo
The final, optimized model is deployed as an interactive web application on Hugging Face Spaces:
👉 **[Brain Tumor Classifier on Hugging Face](https://huggingface.co/spaces/GMI-AI/brain-tumor-classifier)**

---

## 📊 Dataset & Class Distribution

The dataset comprises high-resolution axial brain MRI scans classified into **4 distinct categories**:
1. `glioma_tumor`
2. `meningioma_tumor`
3. `pituitary_tumor`
4. `no_tumor` (Healthy scans)

### Dataset Resources:
* 📁 **[Original Raw Dataset (Google Drive)](https://drive.google.com/drive/folders/12iSrp5lWf0thbYblGpbAL1NYGZPbMzFW?usp=drive_link)**
* 🧼 **[Manually Cleaned Dataset (Google Drive)](https://drive.google.com/drive/folders/1nN9kM1CtJhy4KOu7NKWLyO_VS-N1cv1n?usp=sharing)** — Cleaned manually by AI engineering students.
* 📈 **[Split & Augmented Dataset (Google Drive)](https://drive.google.com/drive/folders/1aeE_xQp1Vx4Qj6U4yIlVPYyJAvgeR03a?usp=sharing)** — Cleaned data balanced to a uniform **1,000 images per class** (4,000 images total) split into `70% Train / 15% Val / 15% Test`.

---

## ⚙️ Custom MRI Physics-Aware Augmentations
Standard geometric rotations or color jitters do not adequately capture real-world medical imaging variance. To build clinical-grade robustness, this project implements custom physical and hardware-level artifact simulators:

| Artifact Simulation | Physics & Implementation |
| :--- | :--- |
| **MRI Bias Field Inhomogeneity** | Simulates spatial RF field variations using a smooth, channel-wise quadratic 2D grid scale, creating realistic gradient illumination drops. |
| **k-space Line Corruption** | Performs a 2D Fast Fourier Transform (FFT) on the spatial image, zeroing out random frequency lines in k-space, and transforms back to recreate k-space acquisition dropout. |
| **Motion Artifacts** | Blends affine-shifted replicas with the original frame to represent micro-movements of patients inside the scanner bore. |
| **k-space Spike Noise** | Amplifies random frequencies in the frequency domain with high-amplitude spikes to simulate RF sensor spikes before inverse FFT. |
| **Phase Ghosting** | Implements a pixel roll along the phase-encoding direction, blending it at a fraction of the intensity to emulate periodic motion artifacts. |

Standard geometric transformations (rotations, elastic transforms, crops) and intensity-based augmentations (gamma, Gaussian noise, coarse dropout) are also provided via `albumentations`.
