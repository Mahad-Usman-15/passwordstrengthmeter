import streamlit as st
import string

# Page configuration
st.set_page_config(page_title="Password Strength Meter", layout="centered")

# Title and description
st.title("🔒 Password Strength Meter")
st.markdown("Check how strong your password is based on common security criteria.")

# Initialize score
if 'score' not in st.session_state:
    st.session_state.score = 0

# Special characters set
specialcharacters = set(string.punctuation)

# Password input with placeholder
password = st.text_input(
    "Enter your password:", 
    placeholder="Type your password here..."
)

def PasswordStrengthMeter():
    # Reset score for each check
    st.session_state.score = 0
    
    # Check password length
    if len(password) >= 8:
        st.session_state.score += 1
        st.success("✓ Minimum 8 characters")
    else:
        st.error("✗ Must be at least 8 characters long")
    
    # Check uppercase letters
    if any(char.isupper() for char in password):
        st.session_state.score += 1
        st.success("✓ Contains uppercase letter")
    else:
        st.error("✗ Must contain at least one uppercase letter")  
    
    # Check lowercase letters
    if any(char.islower() for char in password):
        st.session_state.score += 1
        st.success("✓ Contains lowercase letter")
    else:
        st.error("✗ Must contain at least one lowercase letter") 
    
    # Check numbers
    if any(char.isdigit() for char in password):
        st.session_state.score += 1
        st.success("✓ Contains number")
    else:
        st.error("✗ Must contain at least one number") 
    
    # Check special characters
    if any(char in specialcharacters for char in password):
        st.session_state.score += 1
        st.success("✓ Contains special character")
    else:
        st.error("✗ Must contain at least one special character")
    
    # Display results
    st.divider()
    st.subheader(f"Score: {st.session_state.score}/5")
    
    # Strength assessment with colored boxes
    if st.session_state.score == 5:
        st.success("💪 Strong Password->Meets all criteria", icon="✅")
        st.success("✓ You can use this password anywhere")
    elif st.session_state.score == 3 or st.session_state.score == 4 :
        st.info("👍 Moderate Password->Good but missing some security features", icon="ℹ️")      
    elif st.session_state.score <= 2:
        st.error("❌ Weak Password->Short,missing key elements", icon="🚨")
        st.error("You shoud use numbers,special characters upper and lowercase letters")

# Only run the meter if password is entered
if password:
    PasswordStrengthMeter()