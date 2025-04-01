
import streamlit as st
import requests

# Function to get word details from Free Dictionary API
def get_word_details(word):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to get word pronunciation (from the response)
def get_word_pronunciation(word_details):
    if 'phonetic' in word_details[0]:
        return word_details[0]['phonetic']
    return "No pronunciation available"

# Function to get word synonyms (from the response)
def get_word_synonyms(word_details):
    synonyms = []
    for meaning in word_details[0]['meanings']:
        if 'synonyms' in meaning:
            synonyms.extend(meaning['synonyms'])
    return synonyms

# Streamlit UI Design
st.set_page_config(page_title="Dictionary App", page_icon="📖", layout="wide")

# Custom Styling using Markdown (CSS)
st.markdown("""
    <style>
        body {
            background: radial-gradient(circle, rgba(25, 25, 112, 1) 0%, rgba(0, 0, 0, 1) 100%);
            font-family: 'Poppins', sans-serif;
            color: white;
            overflow: hidden;
            animation: gradient 10s ease infinite;
        }

        @keyframes gradient {
            0% {
                background: radial-gradient(circle, rgba(25, 25, 112, 1) 0%, rgba(0, 0, 0, 1) 100%);
            }
            50% {
                background: radial-gradient(circle, rgba(238, 130, 238, 1) 0%, rgba(0, 0, 0, 1) 100%);
            }
            100% {
                background: radial-gradient(circle, rgba(25, 25, 112, 1) 0%, rgba(0, 0, 0, 1) 100%);
            }
        }

        .title {
            font-size: 60px;
            font-weight: 800;
            color: #ADD8E6;  /* Lighter Blue Color */
            text-align: center;
            text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.4);
            margin-top: 50px;
            letter-spacing: 5px;
            font-family: 'Orbitron', sans-serif;
        }

        .input-container {
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0px 15px 30px rgba(0, 0, 0, 0.3);
            width: 70%;
            margin: 40px auto;
            text-align: center;
        }

        .input-container input {
            border-radius: 10px;
            padding: 15px;
            width: 70%;
            font-size: 20px;
            border: 2px solid #ff69b4;
            outline: none;
            transition: 0.3s;
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
        }

        .input-container input:focus {
            border-color: #32cd32;
            background-color: rgba(50, 205, 50, 0.2);
        }

        .result-container {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0px 15px 30px rgba(0, 0, 0, 0.3);
            width: 70%;
            margin: 20px auto;
            text-align: center;
        }

        /* Styling for the meaning section */
        .meaning-container {
            background-color: rgba(255, 255, 0, 0.2);  /* Soft yellowish background */
            padding: 20px;
            border-radius: 15px;
            color: #ffcc00;  /* Yellow color for text */
            font-size: 20px;
            margin-top: 20px;
        }

        /* Styling for the synonyms section */
        .synonyms-container {
            background-color: rgba(255, 99, 71, 0.2);  /* Soft tomato red background */
            padding: 20px;
            border-radius: 15px;
            color: #ff6347;  /* Tomato red for synonyms */
            font-size: 20px;
            margin-top: 20px;
        }

        /* Colorful Styling for Meaning Header */
        .meaning-header {
            font-size: 30px;
            color: #ff1493;  /* Deep pink for meaning header */
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.4);
        }

        /* Colorful Styling for Synonyms Header */
        .synonyms-header {
            font-size: 30px;
            color: #ff6347;  /* Tomato red for synonyms header */
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.4);
        }

        .button {
            background-color: #ff69b4;
            color: white;
            padding: 12px 24px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            margin-top: 20px;
            width: 60%;
            margin-left: auto;
            margin-right: auto;
            display: block;
            font-size: 18px;
            transition: 0.3s;
        }

        .button:hover {
            background-color: #32cd32;
        }

        .footer {
            text-align: center;
            color: white;
            margin-top: 50px;
            font-size: 18px;
            font-weight: 500;
        }

        .footer a {
            color: #32cd32;
            text-decoration: none;
        }

        .footer a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">✨ Dictionary App ✨</div>', unsafe_allow_html=True)

# Input for word
st.markdown('<div class="input-container">', unsafe_allow_html=True)
word = st.text_input("Enter a word:", key="word", max_chars=50)
st.markdown('</div>', unsafe_allow_html=True)

# Check if word is entered
if word:
    word_details = get_word_details(word)
    if word_details:
        # Display Result Container
        st.markdown('<div class="result-container">', unsafe_allow_html=True)

        # Display Meaning in Colorful Section
        st.markdown('<div class="meaning-container">', unsafe_allow_html=True)
        st.markdown('<div class="meaning-header">Meaning:</div>', unsafe_allow_html=True)  # Colorful header for Meaning
        for meaning in word_details[0]['meanings']:
            if 'definitions' in meaning:
                for definition in meaning['definitions']:
                    st.write(f"- {definition['definition']}")
        st.markdown('</div>', unsafe_allow_html=True)

        # Display Pronunciation
        pronunciation = get_word_pronunciation(word_details)
        if pronunciation != "No pronunciation available":
            st.subheader("Pronunciation:")
            st.write(f"**{pronunciation}**")

        # Display Synonyms in Colorful Section
        synonyms = get_word_synonyms(word_details)
        if synonyms:
            st.markdown('<div class="synonyms-container">', unsafe_allow_html=True)
            st.markdown('<div class="synonyms-header">Synonyms:</div>', unsafe_allow_html=True)  # Colorful header for Synonyms
            st.write(", ".join(synonyms))
            st.markdown('</div>', unsafe_allow_html=True)

        # Save as Favorite Button
        if st.button('💾 Save as Favorite', key="save_favorite", help="Save this word to favorites"):
            with open("favorites.txt", "a") as file:
                file.write(f"{word}\n")
            st.success(f"'{word}' has been saved as a favorite! 💾")

        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-container">', unsafe_allow_html=True)
        st.write(f"Sorry, no details found for '{word}'. 😔")
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.write("Please enter a word to get its meaning, pronunciation, and synonyms. ✨")

# Footer with a message
st.markdown('<div class="footer">Made with ❤️ by <a href="https://yourwebsite.com" target="_blank">Kiran</a></div>', unsafe_allow_html=True)












