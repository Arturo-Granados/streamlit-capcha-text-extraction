#Set-up
import streamlit as st
from tempfile import NamedTemporaryFile

from ml_model import *

#pip install protobuf==3.20
#Set title and subheader 
st.title('Capcha characters recognitions')

st.subheader('A simple app that shows a text extraction algorithm. You can choose a image to play.'
             + ' The application consists in an algorithm that extracts text from Capcha images and show the procces' )


image = st.file_uploader("Choose a image file to play")
temp_file = NamedTemporaryFile(delete=False)
if image:
    temp_file.write(image.getvalue())
    st.subheader('Original image')
    st.image(image)
    img = show_adap_threshold_img(temp_file.name)
    st.subheader('Image with adaptive threshold')
    st.image(img)
    img = closing_img(img)
    st.subheader('Image with closing operation')
    st.image(img)
    img = dilatation_img(img)
    st.subheader('Image with dilatation operation')
    st.image(img)
    img = smooting_img(img)
    st.subheader('Image with smooting operation')
    st.image(img)
    img = image_segmantation(img)
    st.subheader('Image segmentation')
    st.image(img)
    st.subheader(get_demo(temp_file.name))
