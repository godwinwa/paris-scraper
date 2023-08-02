import streamlit as st

def main():
    st.title("Simple Streamlit Test")
    st.write("Welcome to your first Streamlit app!")
    
    st.header("Here's a sample image:")
    image_url = "https://via.placeholder.com/350x150"
    st.image(image_url, caption="Sample Image", use_column_width=True)

if __name__ == "__main__":
    main()
