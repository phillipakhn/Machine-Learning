# Predicting Daily Transportation Mode and Mobility Patterns from Google Maps Timeline Data


## Overview

This project uses Google Maps Timeline data to predict daily mobility patterns and modes of transportation (e.g. walking, cycling, vehicle) using machine learning algorithms such as decision trees, random forests, XGBoost, and oversampling techniques to handle class imbalance.

The notebook extracts features like average speed, duration, and distance, and trains classifiers to identify transportation modes from user movement data.

---

## Dataset

The project uses data exported from Google Maps Timeline in JSON format.  
Make sure you include your own data in this structure:

```
Dataset/location-history.json
```

The data is parsed and transformed into a structured DataFrame for model training and evaluation.

---

## Recommended: Use a Virtual Environment (Optional)

Create a Python virtual environment to keep dependencies isolated:

```bash
python3 -m venv venv
source venv/bin/activate
```

To deactivate:

```bash
deactivate
```

---

## How to Run

### Step 1: Install required packages
```bash
pip3 install -r requirements.txt
```

### Step 2: Launch the notebook

```bash
jupyter notebook
```

Then open and run `notebook.ipynb`
