# LensIQ: EV Predictor from EXIF Metadata 📷⚡

This is **Module 1 of the LensIQ Suite** — an ML-based tool that predicts a photo's Exposure Value (EV) using only EXIF metadata like shutter speed, aperture, and ISO.

---

## 📌 Features

- 📸 Parses image EXIF data (JPG, JPEG, PNG, etc.)
- 📈 Predicts Exposure Value using a trained LOG-Linear Regression model
- 📊 Visualizes predicted vs actual EV
- 🔍 Preprocessing and feature extraction for photography metadata
- 🗺 Scene Mapping for predicted EV value

---

## 🔧 Tech Stack

- Python
- pandas, numpy
- scikit-learn
- Pillow (PIL) for EXIF parsing
- matplotlib & seaborn for visualizations

---

## 🧠 Workflow

1. Add path to photo or folder of photos
2. EXIF data is extracted
3. Features like Aperture, ISO, and Shutter Speed are normalized
4. EV is predicted using a trained ML model
5. Mapping of scene for every EV
6. Visual analysis and charts
