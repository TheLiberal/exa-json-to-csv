import json
import csv
import io
import streamlit as st

st.title("🎈 JSON to CSV Converter")

# JSON input
json_input = st.text_area("Enter your JSON data here:")

# Validate JSON and convert to CSV
if st.button("Convert to CSV"):
    try:
        # Parse JSON
        data = json.loads(json_input)

        # Check if 'results' key exists and is a list
        if 'results' not in data or not isinstance(data['results'], list):
            st.error(
                "Invalid JSON structure. Expected a 'results' key with a list value.")
        else:
            # Create CSV
            output = io.StringIO()
            writer = csv.DictWriter(
                output, fieldnames=data['results'][0].keys())
            writer.writeheader()
            writer.writerows(data['results'])

            # Offer CSV for download
            st.download_button(
                label="Download CSV",
                data=output.getvalue(),
                file_name="converted.csv",
                mime="text/csv"
            )
            st.success("JSON successfully converted to CSV!")
    except json.JSONDecodeError:
        st.error("Invalid JSON. Please check your input.")
