
# Lightweight Image Captioning (BLIP-base)

A small, CPU-friendly image captioning app using **Salesforce/blip-image-captioning-base**.
Built with **Streamlit** + **Hugging Face Transformers**. Perfect for **Render free tier**.

##  Live Demo  
Check it out: [PixCaption AI Live App](https://chintadavasudharini-imagecaption.streamlit.app/)  


## Quick Start (Local)

```bash
git clone <your-repo-url>.git
cd image_caption_lightweight
python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL shown in terminal.

## Deploy to Render

1. Push this folder to a **public GitHub repo**.
2. Go to [Render](https://render.com) → New → Web Service → Connect your repo.
3. Render will read `render.yaml` automatically. If not, set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
4. Click **Create Web Service**.

> First cold start may take a bit due to model download (cached afterward).

## Why this model?

- `Salesforce/blip-image-captioning-base` is lightweight (~200MB) and performs well on CPU.
- Avoids multi‑GB checkpoints like BLIP‑2 OPT or LLaVA.

## Notes

- If you see Torch/Transformers warnings, it's safe to ignore on CPU.
- For faster startup on free tiers, you can prebuild the image or use a persistent disk.

## Optional Enhancements

- Add caption history in a sidebar.
- Add a "Download caption" button.
- Convert to **Gradio** if you prefer a single-file demo.

---

**License:** MIT
