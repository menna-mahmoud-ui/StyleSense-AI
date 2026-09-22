import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000"
)

st.set_page_config(
    page_title="StyleSense AI",
    page_icon="👗",
    layout="centered"
)

st.title("👗 StyleSense AI")
st.write(
    "AI-powered fashion recommendations using YOLO, RAG, and Gemini."
)

st.divider()

# Upload outfit image
uploaded_image = st.file_uploader(
    "Upload your outfit image",
    type=["jpg", "jpeg", "png"]
)

# Display uploaded image
if uploaded_image:
    st.image(
        uploaded_image,
        caption="Uploaded Outfit",
        use_container_width=True
    )

# User question
question = st.text_input(
    "Ask a fashion question",
    placeholder="هل اللبس ده مناسب للجامعة؟"
)

if st.button("Get Style Recommendation"):

    if uploaded_image is None:
        st.warning("Please upload an outfit image.")

    elif not question:
        st.warning("Please enter your question.")

    else:
        try:
            files = {
                "image": (
                    uploaded_image.name,
                    uploaded_image.getvalue(),
                    uploaded_image.type
                )
            }

            data = {
                "question": question
            }

            with st.spinner("Analyzing your outfit..."):

                response = requests.post(
                    f"{BACKEND_URL}/query/image",
                    files=files,
                    data=data,
                    timeout=120
                )

            if response.status_code == 200:

                result = response.json()

                st.success("Analysis completed!")

                # Recommendation
                st.subheader("✨ StyleSense Recommendation")
                st.write(result["answer"])

                # Detected items
                st.subheader("👗 Detected Items")

                for item in result.get("detected_items", []):
                    st.write(
                        f"- **{item['item']}** "
                        f"(confidence: {item['confidence']})"
                    )

                # RAG sources
                if result.get("sources"):
                    st.subheader("📚 Sources")

                    for source in result["sources"]:
                        st.write(f"- {source}")

            else:
                st.error(
                    f"Backend error: {response.status_code}"
                )
                st.code(response.text)

        except requests.exceptions.RequestException as e:
            st.error(
                f"Could not connect to the backend: {e}"
            )