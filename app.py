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
    
  
<table class="table table-dark table-stripped text-center">
  <thead>
    <tr>
      <th>DATA</th>
      <th>MECZ</th>
      <th>PKT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>28.10.2024</td>
      <td>Malmo FF - IFK Goteborg</td>
      <td>10.00</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>Djurgarden - Västerås SK FK</td>
      <td>7.07</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>Galatasaray - Besiktas</td>
      <td>6.13</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>Farul Constanta - CS U Craiova</td>
      <td>4.91</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>Bodo/Glimt - Rosenborg</td>
      <td>4.58</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>GKS Tychy - Znicz Pruszków</td>
      <td>4.41</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>Ituano - Santos</td>
      <td>4.39</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>Randers FC - FC Nordsjaelland</td>
      <td>3.03</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>Coritiba - CRB</td>
      <td>1.98</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>Mallorca - Athletic Bilbao</td>
      <td>1.33</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>Cuiaba - Corinthians</td>
      <td>1.25</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>Blackpool - Wigan</td>
      <td>0.18</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>AVS - FC Porto</td>
      <td>-1.75</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>AVS - FC Porto</td>
      <td>-1.75</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>Racing Ferrol - Tenerife</td>
      <td>-2.24</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>IK Oddevold - Skövde AIK</td>
      <td>-2.81</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>FC Botosani - Universitatea Cluj</td>
      <td>-2.96</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>CD Mafra - UD Leiria</td>
      <td>-5.49</td>
    </tr>
    <tr>
      <td>28.10.2024</td>
      <td>Istanbul Basaksehir - Eyupspor</td>
      <td>-8.54</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Cagliari - Bologna</td>
      <td>8.83</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Lorient - Dunkerque</td>
      <td>8.67</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>AC Milan - Napoli</td>
      <td>7.99</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Goias - Operario PR</td>
      <td>4.29</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>America MG - Sport Recife</td>
      <td>3.83</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Stevenage - Bolton</td>
      <td>3.27</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Troyes - Pau</td>
      <td>2.38</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Lecce - Verona</td>
      <td>2.16</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Grenoble - Annecy</td>
      <td>1.79</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Martigues - Caen</td>
      <td>1.79</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Amiens - Paris FC</td>
      <td>1.63</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Guingamp - AC Ajaccio</td>
      <td>1.22</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Laval - Clermont Foot</td>
      <td>1.17</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>AC Reggiana - Cosenza</td>
      <td>1.04</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Brescia - Spezia</td>
      <td>0.13</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Stockport - Reading</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Modena - Cremonese</td>
      <td>-0.99</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>SC Bastia - Rodez</td>
      <td>-1.19</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Bari - Carrarese</td>
      <td>-1.25</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Brusque - Chapecoense</td>
      <td>-1.38</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Vasco da Gama - Bahia</td>
      <td>-1.80</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Red Star FC 93 - Metz</td>
      <td>-2.25</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Lincoln City - Northampton</td>
      <td>-2.48</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Boyaca Chico - La Equidad</td>
      <td>-2.50</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Independiente Medellin - Jaguares de Cordoba</td>
      <td>-4.95</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Juve Stabia - Sassuolo</td>
      <td>-5.38</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Salernitana - Cesena</td>
      <td>-5.79</td>
    </tr>
    <tr>
      <td>29.10.2024</td>
      <td>Huracan - Central Cordoba SdE</td>
      <td>-6.36</td>
    </tr>
  </tbody>
</table>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>

"""

# Wyświetlenie kodu HTML w Streamlit
st.markdown(html_code, unsafe_allow_html=True)
