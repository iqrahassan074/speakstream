import streamlit as st
from gtts import gTTS
from io import BytesIO

st.markdown("""
    <style>
    /* Background gradient */
    .reportview-container {
        background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
        color: #3a0ca3;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Title styling */
    .title {
        color: #ff4d6d;
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 2px 2px 5px #00000033;
    }

    /* Text area styling */
    textarea {
        background-color: #fff0f6 !important;
        border: 2px solid #ff4d6d !important;
        border-radius: 12px !important;
        color: #3a0ca3 !important;
        font-size: 1.2rem !important;
        padding: 12px !important;
        box-shadow: 3px 3px 10px #ffa1c1cc !important;
    }

    /* Button styling */
    div.stButton > button {
        background: linear-gradient(45deg, #ff4d6d, #f9cb28);
        color: white;
        font-size: 1.3rem;
        font-weight: 700;
        padding: 12px 30px;
        border-radius: 15px;
        box-shadow: 3px 3px 12px #ff4d6dcc;
        transition: background 0.3s ease;
    }

    div.stButton > button:hover {
        background: linear-gradient(45deg, #f9cb28, #ff4d6d);
        cursor: pointer;
    }

    /* Warning text */
    .stWarning {
        font-weight: 600;
        color: #b00020;
        font-size: 1.2rem;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown('🎤 SpeakStream - AI-powered Text-to-Speech', unsafe_allow_html=True)

def main():
    text = st.text_area("📝 Enter text here:")

    if st.button("🗣️ Speak Now!"):
        if text.strip() == "":
            st.warning("⚠️ Please enter some text to convert to speech.")
        else:
            tts = gTTS(text=text, lang='en')
            mp3_fp = BytesIO()
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            st.success("✅ Here's your speech! Listen below 🎧")
            st.audio(mp3_fp.read(), format="audio/mp3")

if __name__ == "__main__":
    main()
