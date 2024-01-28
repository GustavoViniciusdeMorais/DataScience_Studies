from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

app = FastAPI()

@app.get("/check/")
async def check():
    return {"status": "success"}

@app.post("/files/")
async def file_size(file: Annotated[bytes, File()]):
    print('test')
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

@app.post("/classify/")
async def classify(file: UploadFile):
    response = {"filename": file.filename}
    try:
        # Load the trained model
        model_path = os.path.abspath('../notebooks/image_classifier_model.h5')
        model = load_model(model_path)
        
        # Load and preprocess the image to be predicted
        img = image.load_img(file.filename, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize the image
       
        # Make the prediction
        prediction = model.predict(img_array)
        
        # Get the class label with the highest probability
        class_index = np.argmax(prediction)
        class_labels = {0: 'carbon', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic'}
        predicted_class = class_labels[class_index]

        # Display the prediction
        response = {"result": predicted_class}
    except ValueError as ve:
        print(f"Error: {ve}. Please enter valid integers.")

    except ZeroDivisionError as zde:
        print(f"Error: {zde}. Division by zero is not allowed.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return response