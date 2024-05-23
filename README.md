# Deep Learning Face Verification

## Overview

This project utilizes deep learning techniques to perform face verification, which involves determining whether two facial images belong to the same person or not. The model is trained on a dataset of facial images and learns to extract features that are discriminative for identifying individuals.

## Requirements

- Python 3
- TensorFlow
- Keras
- OpenCV
- NumPy

## Usage

1. Clone the repository:

```
git clone https://github.com/srijosh/Face-Verification-Deep-Learning-.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the " Facial Verification with a Siamese Network.ipynb " Jupyter Notebook file to train the model. Make sure you have enough images inside application_data/verification_images folder to test the verification

4. Once you have tested, Navigate to the `app` folder and paste the model trained h5 format file inside it

5. Run the faceid.py script inside the app folder. Ensure that you have enough images inside the app/application_data/verification_images folder for testing.

```
cd app
python faceid.py
```

## Demo:

<table width="100%"> 
<tr>
<td width="50%">
<img src="demos/1.png">
</td> 
<td width="50%">
<img src="demos/2.png">  
</td>
</table>
