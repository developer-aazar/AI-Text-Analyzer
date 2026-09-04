import streamlit as st
import requests as req

st.set_page_config(page_title="Text Analyzer AI")

st.title("Text Analyzer AI")

st.header("Welcome")

st.write("Enter your text and let AI correct the mistakes.")


if "messages" not in st.session_state:
    st.session_state.messages = []

if "mistakes" not in st.session_state:
    st.session_state.mistakes = {
        "grammar": [],
        "spelling": [],
        "punctuation": []
    }
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

input_box = st.chat_input("Enter Your Text Here....")

if input_box:
    st.session_state.messages.append({
        "role": "user",
        "content": input_box
    })

    with st.chat_message("user", avatar="🧑🏻"):
        st.write(input_box)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Analyzing..."):
            try:

                response = req.post(
                    "http://localhost:8000/correct",
                    json={"text": input_box}
                )

                if response.status_code == 200:

                    result = response.json()

                    corrected_text = result["corrected_text"]
                    st.session_state.mistakes = {
                        "grammar": result["grammar_mistakes"],
                        "spelling": result["spelling_mistakes"],
                        "punctuation": result["punctuation_mistakes"]
                    }

                    st.session_state.analysis_done = True
                    
                    st.write("Analysis Result")

                    st.write("Original Text:")
                    st.info(result["original_text"])

                    st.write("Corrected Text:")
                    st.success(corrected_text)

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": f"""
            **Analysis Result**

            **Original Text:**  
            {result["original_text"]}

            **Corrected Text:**  
            {corrected_text}
            """
                    })


                else:

                    st.error("Something went wrong with the backend.")


            except req.exceptions.ConnectionError:

                st.error(
                    "Could not connect to FastAPI. "
                    "Make sure your backend is running."
                )

st.sidebar.header("Project Feedback 😝")

feedback = st.sidebar.selectbox(
    "Please Write Feedback About Project:",
    ("Excellent", "Good", "Average", "Bad")
)

feedback_button = st.sidebar.button("Submit")

if feedback_button:
    st.sidebar.success("Thank You for Your Feedback! ❤️")

st.sidebar.divider()

if st.session_state.analysis_done:

    st.sidebar.header("Mistakes Found!!!")

    st.sidebar.subheader("Grammar Mistakes:")

    if st.session_state.mistakes["grammar"]:
        for mistake in st.session_state.mistakes["grammar"]:
            st.sidebar.write(f"Mistake: {mistake['mistake']}")
            st.sidebar.write(f"Correction: {mistake['correction']}")
    else:
        st.sidebar.write("No grammatical mistakes found.")

    st.sidebar.subheader("Spelling Mistakes:")

    if st.session_state.mistakes["spelling"]:
        for mistake in st.session_state.mistakes["spelling"]:
            st.sidebar.write(f"Mistake: {mistake['mistake']}")
            st.sidebar.write(f"Correction: {mistake['correction']}")
    else:
        st.sidebar.write("No spelling mistakes found.")

    st.sidebar.subheader("Punctuation Mistakes:")

    if st.session_state.mistakes["punctuation"]:
        for mistake in st.session_state.mistakes["punctuation"]:
            st.sidebar.write(f"Mistake: {mistake['mistake']}")
            st.sidebar.write(f"Correction: {mistake['correction']}")
    else:
        st.sidebar.write("No punctuation mistakes found.")