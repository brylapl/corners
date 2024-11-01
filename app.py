import streamlit as st

# Tytuł aplikacji

# Adres URL do otwarcia
url = "https://brylapl.github.io/corner/"

# Tworzenie przycisku, który otworzy nowy adres w nowym oknie
if st.button('Otwórz nowy adres'):
    js = f"""
    <script>
        window.open('{url}', '_blank');
    </script>
    """
    st.markdown(js, unsafe_allow_html=True)
