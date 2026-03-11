# app/streamlit_app.py

import streamlit as st
import sys
from pathlib import Path

# =========================
# Allow import from src
# =========================
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR / "src"))

from predict import predict_price, get_locations


# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Bangalore House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# =========================
# Custom Styling (Fancy UI)
# =========================
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
.big-font {
    font-size:28px !important;
    font-weight:700;
}
.card {
    background-color:white;
    padding:25px;
    border-radius:12px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)


# =========================
# Header
# =========================
st.markdown(
    "<p class='big-font'>🏠 Bangalore House Price Prediction</p>",
    unsafe_allow_html=True
)

st.caption(
    "Predict real estate prices using a Machine Learning Random Forest Model"
)

st.divider()

# =========================
# Load Locations
# =========================
locations = get_locations()

# =========================
# Layout Columns
# =========================
col1, col2 = st.columns([2, 1])

# -------- LEFT SIDE INPUTS --------
with col1:

    st.markdown("### Property Details")

    location = st.selectbox("📍 Location", locations)

    c1, c2, c3 = st.columns(3)

    with c1:
        sqft = st.number_input(
            "📐 Square Feet",
            min_value=300,
            max_value=10000,
            value=1200
        )

    with c2:
        bath = st.number_input(
            "🛁 Bathrooms",
            min_value=1,
            max_value=10,
            value=2
        )

    with c3:
        bhk = st.number_input(
            "🛏 BHK",
            min_value=1,
            max_value=10,
            value=2
        )

    predict_btn = st.button(
        "🚀 Predict Price",
        use_container_width=True
    )

# -------- RIGHT SIDE INFO CARD --------
with col2:
    st.markdown(
        """
        <div class="card">
        <h4>📊 Model Info</h4>
        <ul>
        <li><b>Algorithm:</b> Random Forest</li>
        <li><b>City:</b> Bangalore</li>
        <li><b>Features:</b> Location, Sqft, Bath, BHK</li>
        <li><b>Task:</b> Regression</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# Prediction Section
# =========================
st.divider()

if predict_btn:

    with st.spinner("Predicting price... 🔍"):
        price = predict_price(location, sqft, bath, bhk)

    st.markdown("### 💰 Prediction Result")

    r1, r2, r3 = st.columns(3)

    r2.metric(
        label="Estimated Price",
        value=f"₹ {price:.2f} Lakhs"
    )

    st.success("Prediction completed successfully!")

# =========================
# Footer
# =========================
st.divider()

st.caption(
"""
Built using **Python, Scikit-learn, Random Forest & Streamlit**

Built by **Joyesh**
"""
)