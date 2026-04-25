import streamlit as st
from extract_text import extract_text_from_pdf
from extract_images import extract_images
from llm_pipeline import generate_ddr
from report_generator import create_pdf
from utils import create_folder
import os


st.title("AI DDR Generator")

sample_file = st.file_uploader("Upload Sample Inspection Report", type="pdf")
thermal_file = st.file_uploader("Upload Thermal Report", type="pdf")


if sample_file and thermal_file:

    create_folder("inputs")
    create_folder("outputs")
    create_folder("extracted_images/sample")
    create_folder("extracted_images/thermal")

    sample_path = os.path.join("inputs", "sample_report.pdf")
    thermal_path = os.path.join("inputs", "thermal_report.pdf")

    with open(sample_path, "wb") as f:
        f.write(sample_file.read())

    with open(thermal_path, "wb") as f:
        f.write(thermal_file.read())

    if st.button("Generate DDR"):

        with st.spinner("Processing..."):

            sample_text = extract_text_from_pdf(sample_path)
            thermal_text = extract_text_from_pdf(thermal_path)

            sample_imgs = extract_images(sample_path, "extracted_images/sample")
            thermal_imgs = extract_images(thermal_path, "extracted_images/thermal")

            ddr_report = generate_ddr(sample_text, thermal_text)

            output = create_pdf(ddr_report, sample_imgs, thermal_imgs)

        st.success("DDR Generated Successfully")

        with open(output, "rb") as f:
            st.download_button(
                "Download DDR Report",
                f,
                file_name="DDR_Report_Final.pdf"
            )