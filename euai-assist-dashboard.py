import streamlit as st
from PIL import Image

# ----- Sidebar -----
st.sidebar.title("🧭 EU AI Compliance Assistant")
section = st.sidebar.radio("Go to", [
    "Overview", 
    "Risk Classification", 
    "Document Analyzer", 
    "Fairness Audit", 
    "Monitoring & Drift", 
    "Reports & Exports"
])

# ----- Header -----
st.title("🛡️ EU AI Act Compliance Dashboard")
st.caption("An AI-powered assistant to support your organization’s compliance with the EU AI Act")

# ----- Sections -----
if section == "Overview":
    st.subheader("Welcome 👋")
    st.markdown("""
    Use this assistant to:
    - Classify your AI system by risk
    - Analyze documentation for gaps
    - Run fairness audits
    - Monitor for drift
    - Generate audit reports
    """)

elif section == "Risk Classification":
    st.subheader("🧠 Risk Classification")
    use_case = st.text_area("Describe your AI use case")
    if st.button("Classify Risk"):
        # Simulate LLM classification
        st.success("Predicted Risk Category: High Risk (Biometric Identification)")
        st.markdown("📘 Refer to Annex III – High-Risk Use Cases")

elif section == "Document Analyzer":
    st.subheader("📄 Document Analyzer")
    uploaded_file = st.file_uploader("Upload AI system documentation", type=["pdf", "docx", "txt"])
    if uploaded_file:
        st.info("Running NLP compliance check...")
        # Simulated result
        st.warning("❌ Missing human oversight description")
        st.success("✅ Data governance section found")

elif section == "Fairness Audit":
    st.subheader("⚖️ Fairness Audit")
    st.markdown("Upload your dataset or model output for bias analysis.")
    data_file = st.file_uploader("Upload CSV", type="csv")
    if data_file:
        st.info("Running statistical parity analysis...")
        st.error("⚠️ Detected disparate impact between gender groups")
        st.bar_chart({"Male": 0.82, "Female": 0.65})

elif section == "Monitoring & Drift":
    st.subheader("📊 Model Monitoring")
    st.markdown("Visualize performance over time.")
    # Simulated metric display
    st.line_chart({"Accuracy": [0.90, 0.88, 0.85, 0.78]})
    st.warning("⚠️ Model drift detected in last 30 days")

elif section == "Reports & Exports":
    st.subheader("📋 Compliance Report")
    st.markdown("""
    - Risk: **High**
    - Documentation: **Partial**
    - Bias Found: **Yes**
    - Drift: **Detected**
    """)
    st.download_button("📁 Download PDF Report", data=b"Report content...", file_name="compliance_report.pdf")

