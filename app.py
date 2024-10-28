import streamlit as st

# Ustawienia tytułu aplikacji

# HTML do wyświetlenia
html_code = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <style>
        .badge {
            color: white; /* Ustawia kolor czcionki na czarny */
          font-size:16px;
        }
    </style>
</head>
<body>

<table class="table table-dark table-striped text-center">
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
        <td><span class="badge bg-success">10.00</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>Djurgarden - Västerås SK FK</td>
        <td><span class="badge bg-success">7.07</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>Galatasaray - Besiktas</td>
        <td><span class="badge bg-success">6.13</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>Farul Constanta - CS U Craiova</td>
        <td><span class="badge bg-success">4.91</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>Bodo/Glimt - Rosenborg</td>
        <td><span class="badge bg-success">4.58</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>GKS Tychy - Znicz Pruszków</td>
        <td><span class="badge bg-success">4.41</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>Ituano - Santos</td>
        <td><span class="badge bg-success">4.39</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>Randers FC - FC Nordsjaelland</td>
        <td><span class="badge bg-success">3.03</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>Coritiba - CRB</td>
        <td><span class="badge bg-success">1.98</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>Mallorca - Athletic Bilbao</td>
        <td><span class="badge bg-success">1.33</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>Cuiaba - Corinthians</td>
        <td><span class="badge bg-success">1.25</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>Blackpool - Wigan</td>
        <td><span class="badge bg-success">0.18</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>AVS - FC Porto</td>
        <td><span class="badge bg-danger">-1.75</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>AVS - FC Porto</td>
        <td><span class="badge bg-danger">-1.75</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>Racing Ferrol - Tenerife</td>
        <td><span class="badge bg-danger">-2.24</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>IK Oddevold - Skövde AIK</td>
        <td><span class="badge bg-danger">-2.81</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>FC Botosani - Universitatea Cluj</td>
        <td><span class="badge bg-danger">-2.96</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>CD Mafra - UD Leiria</td>
        <td><span class="badge bg-danger">-5.49</span></td>
    </tr>
    <tr>
        <td>28.10.2024</td>
        <td>Istanbul Basaksehir - Eyupspor</td>
        <td><span class="badge bg-danger">-8.54</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Cagliari - Bologna</td>
        <td><span class="badge bg-success">8.83</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Lorient - Dunkerque</td>
        <td><span class="badge bg-success">8.67</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>AC Milan - Napoli</td>
        <td><span class="badge bg-success">7.99</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Goias - Operario PR</td>
        <td><span class="badge bg-success">4.29</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>America MG - Sport Recife</td>
        <td><span class="badge bg-success">3.83</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Stevenage - Bolton</td>
        <td><span class="badge bg-success">3.27</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Troyes - Pau</td>
        <td><span class="badge bg-success">2.38</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Lecce - Verona</td>
        <td><span class="badge bg-success">2.16</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Grenoble - Annecy</td>
        <td><span class="badge bg-success">1.79</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Martigues - Caen</td>
        <td><span class="badge bg-success">1.79</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Amiens - Paris FC</td>
        <td><span class="badge bg-success">1.63</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Guingamp - AC Ajaccio</td>
        <td><span class="badge bg-success">1.22</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Laval - Clermont Foot</td>
        <td><span class="badge bg-success">1.17</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>AC Reggiana - Cosenza</td>
        <td><span class="badge bg-success">1.04</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Brescia - Spezia</td>
        <td><span class="badge bg-success">0.13</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Stockport - Reading</td>
        <td><span class="badge bg-danger">-0.15</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Modena - Cremonese</td>
        <td><span class="badge bg-danger">-0.99</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>SC Bastia - Rodez</td>
        <td><span class="badge bg-danger">-1.19</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Bari - Carrarese</td>
        <td><span class="badge bg-danger">-1.25</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Brusque - Chapecoense</td>
        <td><span class="badge bg-danger">-1.38</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Vasco da Gama - Bahia</td>
        <td><span class="badge bg-danger">-1.80</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Red Star FC 93 - Metz</td>
        <td><span class="badge bg-danger">-2.25</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Lincoln City - Northampton</td>
        <td><span class="badge bg-danger">-2.48</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Boyaca Chico - La Equidad</td>
        <td><span class="badge bg-danger">-2.50</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Independiente Medellin - Jaguares de Cordoba</td>
        <td><span class="badge bg-danger">-4.95</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Juve Stabia - Sassuolo</td>
        <td><span class="badge bg-danger">-5.38</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Salernitana - Cesena</td>
        <td><span class="badge bg-danger">-5.79</span></td>
    </tr>
    <tr>
        <td>29.10.2024</td>
        <td>Huracan - Central Cordoba SdE</td>
        <td><span class="badge bg-danger">-6.36</span></td>
    </tr>
    </tbody>
</table>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>


"""

# Wyświetlenie kodu HTML w Streamlit
st.markdown(html_code, unsafe_allow_html=True)
