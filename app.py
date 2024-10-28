import streamlit as st

# Ustawienia tytułu aplikacji
st.title("28.10.2024")

# HTML do wyświetlenia
html_code = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    
  <table border="1" class="table table-dark table-hover table-striped text-center">
      <thead>
        <tr>
          <th>Mecz</th>
          <th>PKT</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Mallorca - Athletic Bilbao</td>
          <td>1.33</td>
        </tr>
        <tr>
          <td>Istanbul Basaksehir - Eyupspor</td>
          <td>-8.54</td>
        </tr>
        <tr>
          <td>FC Botosani - Universitatea Cluj</td>
          <td>-2.96</td>
        </tr>
        <tr>
          <td>Galatasaray - Besiktas</td>
          <td>6.13</td>
        </tr>
        <tr>
          <td>CD Mafra - UD Leiria</td>
          <td>-5.49</td>
        </tr>
        <tr>
          <td>GKS Tychy - Znicz Pruszków</td>
          <td>4.41</td>
        </tr>
        <tr>
          <td>Randers FC - FC Nordsjaelland</td>
          <td>3.03</td>
        </tr>
        <tr>
          <td>Bodo/Glimt - Rosenborg</td>
          <td>4.58</td>
        </tr>
        <tr>
          <td>Djurgarden - Västerås SK FK</td>
          <td>7.07</td>
        </tr>
        <tr>
          <td>IK Oddevold - Skövde AIK</td>
          <td>-2.81</td>
        </tr>
        <tr>
          <td>Malmo FF - IFK Goteborg</td>
          <td>10.00</td>
        </tr>
        <tr>
          <td>Farul Constanta - CS U Craiova</td>
          <td>4.91</td>
        </tr>
        <tr>
          <td>Racing Ferrol - Tenerife</td>
          <td>-2.24</td>
        </tr>
        <tr>
          <td>Blackpool - Wigan</td>
          <td>0.18</td>
        </tr>
        <tr>
          <td>AVS - FC Porto</td>
          <td>-1.75</td>
        </tr>
        <tr>
          <td>Coritiba - CRB</td>
          <td>1.98</td>
        </tr>
        <tr>
          <td>Cuiaba - Corinthians</td>
          <td>1.25</td>
        </tr>
        <tr>
          <td>Ituano - Santos</td>
          <td>4.39</td>
        </tr>
      </tbody>
  </table>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
"""

# Wyświetlenie kodu HTML w Streamlit
st.markdown(html_code, unsafe_allow_html=True)
