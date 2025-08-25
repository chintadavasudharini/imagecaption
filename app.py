import streamlit as st
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

# ---------------------------
# Page Setup
# ---------------------------
st.set_page_config(page_title="PixCaption AI", page_icon="🖼️", layout="centered")

# Custom CSS for a clean look
st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #4a4aef;
    }
    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #555;
    }
    .stButton>button {
        background-color: #4a4aef;
        color: white;
        border-radius: 12px;
        font-weight: bold;
        padding: 10px 24px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #3030c0;
    }
    .caption-box {
        background: #f0f0ff;
        padding: 16px;
        border-radius: 12px;
        margin-top: 20px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: 500;
        color: #333;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">PixCaption AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Generate instant, smart captions for your images</div>', unsafe_allow_html=True)
st.write("")

# ---------------------------
# Load Model (cached)
# ---------------------------
@st.cache_resource(show_spinner=False)
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    model.eval()
    return processor, model

processor, model = load_model()

# ---------------------------
# Upload & Caption
# ---------------------------
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("✨ Generate Caption"):
        with st.spinner("Analyzing your image..."):
            inputs = processor(images=image, return_tensors="pt")
            out = model.generate(**inputs, max_length=30, num_beams=5)
            caption = processor.decode(out[0], skip_special_tokens=True).strip()

        st.markdown(f'<div class="caption-box">💡 {caption}</div>', unsafe_allow_html=True)

# ---------------------------
# Footer
# ---------------------------
st.write("")
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center; font-size: 0.9rem; color: #777;'>"
    "Powered by <b>BLIP-base</b> | Deployed in <b>Streamlit</b>"
    "</div>", 
    unsafe_allow_html=True
)
