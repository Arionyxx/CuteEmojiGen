import streamlit as st

def show_success_message(message, duration=3):
    """Show a success message that automatically disappears"""
    placeholder = st.empty()
    placeholder.success(message)
    # In actual implementation, we would use JavaScript to remove the message after duration
    # But since we're not using custom JS, we'll rely on the next rerun to clear it

def get_emoji_background_color(emoji_type):
    """Get background color based on emoji type"""
    colors = {
        "cute": "#FFD1DC",  # Light pink
        "cuddly": "#FFB6C1",  # Pink
        "sleepy": "#E6E6FA",  # Lavender
        "fluffy": "#FFF0F5",  # Lavender blush
        "flutter": "#E0FFFF",  # Light cyan
        "shy": "#FFDAB9",  # Peach puff
        "happy": "#FFFACD",  # Lemon chiffon
        "sad": "#E6E6FA",  # Lavender
        "excited": "#FFD700",  # Gold
        "angry": "#FF6347",  # Tomato
        "surprised": "#98FB98",  # Pale green
        "love": "#FFC0CB",  # Pink
        "random": "#FFFFFF"  # White
    }
    return colors.get(emoji_type, "#F5F5F5")  # Default to whitesmoke

def format_emoji_display(emoji, size="large"):
    """Format the emoji display with appropriate size"""
    sizes = {
        "small": "30px",
        "medium": "50px",
        "large": "70px",
        "extra-large": "100px"
    }
    font_size = sizes.get(size, "50px")
    return f"<span style='font-size: {font_size};'>{emoji}</span>"

def search_emojis(emoji_list, search_term):
    """Search emojis based on search term"""
    if not search_term:
        return emoji_list
    
    search_term = search_term.lower()
    return [e for e in emoji_list if search_term in e.lower()]
