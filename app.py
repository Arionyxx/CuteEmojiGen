import streamlit as st
import emoji_generator as eg
import utils
import random
import db_utils

# Set page configuration
st.set_page_config(
    page_title="Kaomoji Generator",
    page_icon="(づ｡◕‿‿◕｡)づ",
    layout="wide"
)

# Initialize session state for generated emojis if not exists
if 'generated_emojis' not in st.session_state:
    st.session_state.generated_emojis = []

# Initialize session state for current category
if 'current_category' not in st.session_state:
    st.session_state.current_category = "random"

# Function to load kaomoji history from database
def load_history_from_db():
    """Load emoji history from database"""
    history_entries = db_utils.get_all_kaomoji()
    # Return list of kaomoji text
    return [entry.text for entry in history_entries]

# Function to copy emoji to database
def copy_emoji(emoji_to_copy):
    # Save to database
    category = st.session_state.current_category
    save_success = db_utils.save_kaomoji(emoji_to_copy, category)
    return save_success

# Function to generate new emojis
def generate_emojis(emoji_type, count=10):
    # Store the current category for database storage
    st.session_state.current_category = emoji_type
    # Get emojis from generator
    st.session_state.generated_emojis = eg.generate_emojis(emoji_type, count)
    return st.session_state.generated_emojis

# App title and description
st.title("✨ Kaomoji Text Face Generator ✨")
st.markdown("Generate and copy your favorite text-based emoticons (kaomoji) like (*≧ω≦) and (｡♥‿♥｡)ﾉ♡!")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Generate Kaomoji")
    
    # Kaomoji type selection with more descriptive labels
    emoji_type = st.selectbox(
        "Select Kaomoji Mood:",
        ["cute", "cuddly", "sleepy", "fluffy", "flutter", "shy", 
         "happy", "sad", "excited", "angry", "surprised", "love", "random"],
        format_func=lambda x: x.capitalize() + " mood" if x != "random" else "Random mood"
    )
    
    # Number of kaomoji to generate (maximum 10)
    num_emojis = st.slider("Number of Kaomoji:", 1, 10, 5)
    
    # Generate button
    if st.button("Generate Kaomoji ʕ•ᴥ•ʔ"):
        with st.spinner("Generating kaomoji (⊃｡•́‿•̀｡)⊃ ..."):
            generate_emojis(emoji_type, num_emojis)
    
    # Display generated kaomoji
    if st.session_state.generated_emojis:
        st.subheader("Generated Kaomoji")
        emoji_cols = st.columns(min(5, num_emojis))
        
        for i, emoji_item in enumerate(st.session_state.generated_emojis):
            col_index = i % len(emoji_cols)
            with emoji_cols[col_index]:
                # Make font size larger for better visibility
                st.markdown(f"<h2 style='text-align: center; font-size: 24px;'>{emoji_item}</h2>", unsafe_allow_html=True)
                if st.button(f"Copy ♡", key=f"copy_{i}"):
                    copy_success = copy_emoji(emoji_item)
                    if copy_success:
                        st.success("Copied to history! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
                        st.balloons()

with col2:
    st.subheader("Kaomoji History (⌒‿⌒)")
    
    # Search in history
    search_term = st.text_input("Search history:", "")
    
    # Get history from database
    if search_term:
        # Search in database using search term
        history_entries = db_utils.search_kaomoji(search_term)
    else:
        # Get all entries from database
        history_entries = db_utils.get_all_kaomoji()
    
    # Display kaomoji history from database
    if history_entries:
        for i, entry in enumerate(history_entries):
            emoji_item = entry.text
            category = entry.category
            created_at = entry.created_at.strftime("%Y-%m-%d %H:%M")
            
            col_a, col_b = st.columns([1, 4])
            with col_a:
                st.markdown(f"<h3 style='text-align: center; font-size: 18px;'>{emoji_item}</h3>", unsafe_allow_html=True)
            with col_b:
                st.text(f"{category.capitalize()} kaomoji")
                st.text(f"Saved: {created_at}")
                if st.button(f"Copy ✿", key=f"history_{i}"):
                    # Just display the copied info, don't re-add to db
                    st.info(f"Copied: {emoji_item} (づ｡◕‿‿◕｡)づ")
        
        # Clear history button
        if st.button("Clear History (•̀ᴗ•́)و"):
            if db_utils.clear_history():
                st.success("History cleared! ヾ(⌐■_■)ノ♪")
                st.rerun()
            else:
                st.error("Failed to clear history (┬┬﹏┬┬)")
    else:
        st.info("Your kaomoji history will appear here (´｡• ᵕ •｡`)")

# Footer
st.markdown("---")
st.markdown("Made with (づ ◕‿◕ )づ ♡ using Streamlit")
