
import streamlit as st  # Streamlit library import for creating the web app
import random           # Random module for selecting random characters
import string           # String module to access predefined character sets

# Function to generate the password
def generate_password(length, use_digits, use_special_chars):
    characters = string.ascii_letters  # Start with all alphabet letters (uppercase + lowercase)
    if use_digits:
        characters += string.digits    # Add digits if checkbox is selected
    if use_special_chars:
        characters += string.punctuation  # Add special characters if checkbox is selected
    return ''.join(random.choice(characters) for _ in range(length))  # Return a random password

# Streamlit UI starts here
st.title("🔐 Password Strength Meter")  # Title at the top of the app

# Slider for password length input from user
length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

# Checkbox to include digits in password
use_digits = st.checkbox("Include Digits")

# Checkbox to include special characters in password
use_special_chars = st.checkbox("Include Special Characters")

# Button to trigger password generation
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special_chars)  # Call function with selected options
    st.success(f"Generated Password: `{password}`")  # Display the generated password with highlight

# Divider line
st.write("--------------------------------")  # Horizontal line for separation

# Footer message with heart in red and centered
st.markdown("""
<div style='text-align: center;'>
    <h4>Built with <span style='color: red;'>❤</span> by Atiya Shah</h4>
</div>
""", unsafe_allow_html=True)  # HTML enabled to style and color the heart
