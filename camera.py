import pygame
import pygame.camera
import tensorflow as tf
from keras.models import Sequential , load_model
from keras.layers import Dense
from keras.metrics import MeanAbsoluteError
import numpy as np
from PIL import Image
import streamlit as st
from streamlit_webrtc import webrtc_streamer
st.title("Age and Gender prediction project.")
import streamlit as st
from PIL import Image
import streamlit as st
from pygrabber.dshow_graph import FilterGraph
import pythoncom
pythoncom.CoInitialize()


def list_cameras():
    devices = FilterGraph().get_input_devices()
    available_cameras = {}
    for device_index, device_name in enumerate(devices):
        available_cameras[device_index] = device_name
    return available_cameras

img_file_buffer = st.camera_input("Capture an image")
gender_dict = {0:"Male",1:"Female"}
print(list_cameras())

if img_file_buffer is not None:
    
    imge = Image.open(img_file_buffer)   
    model = load_model("model.keras", custom_objects={"mae": MeanAbsoluteError()})
    imge = imge.resize((128, 128))   
    imge = imge.convert('L')
    imge_arr = np.array(imge) / 255.0
    imge_input = np.expand_dims(imge_arr,axis = 0)
    predictions = model.predict(imge_input)
    pred_gender = gender_dict[round(predictions[0][0][0])]
    pred_age = predictions[1][0]
    st.write(pred_gender)
    st.write(pred_age) 
   







