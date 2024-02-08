
import streamlit as st

# Function to mimic chatbot response
def get_chatbot_response(message):
    return f"Chatbot says: I received your message '{message}'. How can I assist you further?"

# Placeholder function for settings page content
def display_settings_page():
    st.header("Settings")
    st.write("This is a placeholder for settings. Customize as needed.")

# Main app logic
def main_chat_window():
    st.title('Chatbot UI')

    # Sidebar
    with st.sidebar:
        st.header('Chatbot Info')
        st.write('This is a simple chatbot UI built with Streamlit. You can interact with the chatbot in the chat window.')

        # Search input for previous conversations
        search_query = st.text_input("Search previous conversations", key="search_conversations")

        # Display list of previous conversations (filtered based on search query if any)
        st.write("Previous Conversations")
        if 'chat_history' in st.session_state:
            filtered_history = [conv for conv in st.session_state.chat_history if search_query.lower() in conv.lower()]
            for conv in filtered_history:
                st.write(conv)

        # Link to settings page
        if st.button("Go to Settings"):
            st.session_state.current_page = "settings"

    # Main chat interface
    if st.session_state.current_page == "main":
        col1, col2 = st.columns([3, 1])  # Adjust column ratios as needed
        
        with col1:
            # Text input for user message
            user_message = st.text_input("You: ", key="user_input", on_change=None)
        
        with col2:
            # File uploader next to the message input
            uploaded_file = st.file_uploader("", key="file_uploader", type=None)
        
        # Logic to handle message or file upload
        if st.button('Send') and (user_message or uploaded_file):
            if user_message:
                # Append user message to chat history
                st.session_state.chat_history.append(f"You: {user_message}")
                # Get chatbot response and append to chat history
                chatbot_response = get_chatbot_response(user_message)
                st.session_state.chat_history.append(chatbot_response)
                # Clear input box after sending the message
                st.session_state.user_input = ""
            
            if uploaded_file is not None:
                # Append uploaded file name to chat history
                st.session_state.chat_history.append(f"You uploaded: {uploaded_file.name}")
                # You can add logic here to process the file as needed
                # Clear the uploader after processing
                st.session_state.file_uploader = None

        # Display chat history
        for message in st.session_state.chat_history:
            st.text_area("", value=message, height=75, disabled=True)

    elif st.session_state.current_page == "settings":
        display_settings_page()

# Initialize session states
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'current_page' not in st.session_state:
    st.session_state.current_page = "main"
if 'file_uploader' not in st.session_state:
    st.session_state.file_uploader = None

# Run the main chat window function
main_chat_window()
