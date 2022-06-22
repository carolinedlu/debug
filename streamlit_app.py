import streamlit as st

def load_previous_input(label):
    """If it exists, populate input with previous user entry, otherwise None"""
    return st.session_state[label] if label in st.session_state else None

def save_input(label, new_value):
    """Overwrite previous input with new input"""
    st.session_state[label] = new_value

with st.sidebar:
    selected_page = st.radio('Select Page', ['Page 1', 'Page 2'])

if selected_page == 'Page 1':
    label = 'Multiselect Field'
    value = load_previous_input(label)
    options = ['a','b','c']
    user_val = st.multiselect(label, options, value)
    save_input(label, user_val)

elif selected_page == 'Page 2':
    st.write("""Page 2: User does stuff on this page, when clicking back to Page 1, I want the field to
    prepopulate with what they entered before (if it exists). It seemingly works, (prepopulates with previous input)
    but look what happens when you try to change the selection...
    """)
