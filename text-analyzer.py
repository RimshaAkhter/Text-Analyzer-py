import streamlit as st

# Create a form to prevent the default Streamlit text area behavior
with st.form(key="text_analysis_form"):
    # User input with no extra hints
    text = st.text_area ("Enter a paragraph:", help="")  

    # Search and replace inputs inside the form
    st.header("🔍 Search and Replace")
    search_word = st.text_input("Search for:")
    replace_word = st.text_input("Replace with:")

    # Uppercase and lowercase conversion inside the form
    st.header("🔠 Text Case Conversion")
    case_option = st.selectbox("Select an option:", ["Uppercase", "Lowercase"])

    # Apply button inside the form
    submit_button = st.form_submit_button("Apply")

# Validate input and process when Apply is clicked
if submit_button:
    if not text.strip():
        st.error("❌ Please enter a paragraph before applying changes.")
    else:
        # Text analysis section
        st.header("📊 Text Analysis")

        # Word and character count
        words = text.split()
        num_words = len(words)
        num_chars = len(text)

        st.markdown(f"**📝 Word Count:** `{num_words}`")
        st.markdown(f"**🔢 Character Count:** `{num_chars}`")

        # Vowel count
        vowels = "aeiouAEIOU"
        num_vowels = sum(1 for char in text if char in vowels)
        st.markdown(f"**🔤 Vowel Count:** `{num_vowels}`")

        # Perform search and replace
        if search_word and replace_word:
            modified_text = text.replace(search_word, replace_word)
            st.header("✏️ Modified Paragraph")
            st.code(modified_text, language="text")

        # Apply uppercase/lowercase transformation
        if case_option == "Uppercase":
            st.header("🔡 Uppercased Text")
            st.code(text.upper(), language="text")
        elif case_option == "Lowercase":
            st.header("🔡 Lowercased Text")
            st.code(text.lower(), language="text")


