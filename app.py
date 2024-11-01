import streamlit as st

# Funkcja do przekierowania
def redirect_to(url):
    # Kod HTML i JavaScript do wykonania przekierowania
    html = f"""
    <script>
        window.location.href = "{url}";
    </script>
    """
    # Wyświetlenie komponentu HTML w Streamlit
    st.components.v1.html(html)

# Przykładowe użycie - przekierowanie do innego adresu
if st.button('Przekierowanie'):
    redirect_to('https://brylapl.github.io/corner/')   # Podaj adres URL, na który chcesz przekierować
