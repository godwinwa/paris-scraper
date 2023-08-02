import streamlit as st

def main():
    google_ads_source = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8531075395137869"
    

    st.title("Simple Streamlit Test")
    st.write("Welcome to your first Streamlit app!")
    
    st.header("Here's a sample image:")
    image_url = "https://via.placeholder.com/350x150"
    st.image(image_url, caption="Sample Image", use_column_width=True)
    HtmlFile = open("test.html", "r", encoding="utf-8")
    source_code = HtmlFile.read()
    st.components.v1.html(source_code, height=600)

if __name__ == "__main__":
    main()
