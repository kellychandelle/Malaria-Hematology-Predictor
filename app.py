import pickle
import pandas as pd
import gradio as gr

# ── Load saved model ─────────────────────────────────
with open("malaria_model.pkl", "rb") as f:
    saved = pickle.load(f)

model   = saved["model"]
scaler  = saved["scaler"]
columns = saved["columns"]


# ── Prediction Function ──────────────────────────────
def predict(
    age,
    hb,
    wbc,
    neutrophils,
    lymphocytes,
    eosinophils,
    htc,
    mch,
    mchc,
    rdw,
    platelet,
    sex
):

    # Encode sex
    sex_male = 1 if sex == "Male" else 0

    # Create dataframe in EXACT training order
    X = pd.DataFrame([[
        age,
        hb,
        wbc,
        neutrophils,
        lymphocytes,
        eosinophils,
        htc,
        mch,
        mchc,
        rdw,
        platelet,
        sex_male
    ]], columns=columns)

    # Scale data
    X_scaled = scaler.transform(X)

    # Predict
    pred  = model.predict(X_scaled)[0]
    proba = model.predict_proba(X_scaled)[0]

    conf = round(float(proba[pred]) * 100, 1)

    if pred == 1:
        return f" MALARIA POSITIVE — {conf}% confidence"
    else:
        return f" MALARIA NEGATIVE — {conf}% confidence"


# ── Gradio UI ────────────────────────────────────────
with gr.Blocks(title="Malaria Prediction App") as demo:

    gr.Markdown("# Malaria Prediction Using Hematological Indicators")

    gr.Markdown(
        "Enter hematological parameters to predict malaria positivity."
    )

    with gr.Row():
        age = gr.Number(label="Age")
        hb  = gr.Number(label="Hemoglobin (Hb%)")
        wbc = gr.Number(label="Total WBC Count")

    with gr.Row():
        neutrophils = gr.Number(label="Neutrophils")
        lymphocytes = gr.Number(label="Lymphocytes")
        eosinophils = gr.Number(label="Total Circulating Eosinophils")

    with gr.Row():
        htc  = gr.Number(label="HTC/PCV (%)")
        mch  = gr.Number(label="MCH (pg)")
        mchc = gr.Number(label="MCHC (g/dl)")

    with gr.Row():
        rdw      = gr.Number(label="RDW-CV (%)")
        platelet = gr.Number(label="Platelet Count")
        sex      = gr.Dropdown(
            ["Male", "Female"],
            label="Sex"
        )

    btn = gr.Button("Predict", variant="primary")

    result = gr.Markdown()

    btn.click(
        fn=predict,
        inputs=[
            age,
            hb,
            wbc,
            neutrophils,
            lymphocytes,
            eosinophils,
            htc,
            mch,
            mchc,
            rdw,
            platelet,
            sex
        ],
        outputs=result
    )

    gr.Markdown(
        "<small>For educational purposes only. "
        "Always consult healthcare professionals.</small>"
    )

demo.launch()
