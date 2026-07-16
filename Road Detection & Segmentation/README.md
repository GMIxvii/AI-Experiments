# 🛰️ Satellite Road Segmentation using U-Net & ResNet-UNet

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![HuggingFace Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-yellow.svg)](https://huggingface.co/spaces/GMI-AI/Road-segmentation-app)

An end-to-end deep learning project for semantic road extraction from high-resolution aerial and satellite imagery. This repository contains data acquisition scripts, preprocessing pipelines, and PyTorch implementations comparing a classic **U-Net** against a transfer-learning-capable **ResNet-UNet** on the challenging **Massachusetts Roads Dataset**.

---

## 🚀 Live Demo
Test the final trained models in real-time with your own aerial images on Hugging Face Spaces:
👉 **[Road Segmentation App on Hugging Face](https://huggingface.co/spaces/GMI-AI/Road-segmentation-app)**

---

## 📊 Dataset Reference
The pipeline utilizes the popular **Massachusetts Roads Dataset** (originally collected by Volodymyr Mnih):
* 📁 **[Processed Dataset (Google Drive)](https://drive.google.com/drive/folders/1hwKrTEqsiUz0UtWEPhRdrbCCQ_rjdRFq?usp=drive_link)** — Ready-to-use directory including splits for training, validation, and testing.
* 🌐 **[Original Source Webpage](https://www.cs.toronto.edu/~vmnih/data/)**

The dataset consists of $1500 \times 1500$ pixel satellite images paired with binary road masks where roadways are labeled as the positive class.

---

## 🏗️ Models Implemented
We explore and compare two high-performing fully convolutional network architectures implemented in **PyTorch**:

1. **U-Net (Baseline)**: A classic symmetric encoder-decoder network utilizing skip connections to preserve high-resolution spatial details essential for identifying narrow roadways.
2. **ResNet-UNet (Transfer Learning)**: Evaluates a U-Net layout leveraging a pre-trained ResNet backbone as the contracting path (encoder). This replaces standard convolutional blocks with residual learning structures to facilitate better gradient flow and feature extraction.

---

