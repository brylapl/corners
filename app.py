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
</head>
<body>
<div class="container mt-5">
<div class="accordion" id="accordionExample">

<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading0">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse0" aria-expanded="true" aria-controls="collapse0">
<span class="h4">Amazonas vs Botafogo SP <span class= "badge text-bg-dark">4.38</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse0" class="accordion-collapse collapse" aria-labelledby="heading0" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Amazonas</td>
<td>12</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>1</td>
<td>Avai</td>
<td>6</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>7</td>
<td>Novorizontino</td>
<td>3</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>1</td>
<td>Operario PR</td>
<td>2</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>7</td>
<td>Ceara</td>
<td>1</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">4</span></td>
<td>1</td>
<td>Ponte Preta</td>
<td>1</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>2</td>
<td>CRB</td>
<td>3</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>2</td>
<td>Ituano</td>
<td>3</td>
<td>1</td>
<td>11.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>12</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>2</td>
<td>Guarani</td>
<td>6</td>
<td>0</td>
<td>11.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>16</td>
<td class="text-center"><span class="badge text-bg-warning">20</span></td>
<td>4</td>
<td>Vila Nova</td>
<td>7</td>
<td>4</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">16</span></td>
<td>6</td>
<td>Coritiba</td>
<td>7</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>2</td>
<td>Chapecoense</td>
<td>3</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>12</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>1</td>
<td>Brusque</td>
<td>8</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>5</td>
<td>Mirassol</td>
<td>4</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>9</td>
<td>Paysandu</td>
<td>4</td>
<td>7</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>1</td>
<td>Santos</td>
<td>2</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>4</td>
<td>Sport Recife</td>
<td>2</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>1</td>
<td>Botafogo SP</td>
<td>3</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Goias</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>5</td>
<td>Amazonas</td>
<td>5</td>
<td>3</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Vila Nova</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>3</td>
<td>Amazonas</td>
<td>6</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Coritiba</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Amazonas</td>
<td>3</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Chapecoense</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>5</td>
<td>Amazonas</td>
<td>2</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Brusque</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>7</td>
<td>Amazonas</td>
<td>2</td>
<td>6</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Mirassol</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>6</td>
<td>Amazonas</td>
<td>3</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Paysandu</td>
<td>13</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>2</td>
<td>Amazonas</td>
<td>7</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Santos</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>5</td>
<td>Amazonas</td>
<td>1</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Sport Recife</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>2</td>
<td>Amazonas</td>
<td>3</td>
<td>0</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>America MG</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>8</td>
<td>Amazonas</td>
<td>2</td>
<td>6</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>11</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>4</td>
<td>Amazonas</td>
<td>2</td>
<td>4</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Avai</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>4</td>
<td>Amazonas</td>
<td>3</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>2</td>
<td>Amazonas</td>
<td>1</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Operario PR</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>6</td>
<td>Amazonas</td>
<td>1</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Ceara</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>5</td>
<td>Amazonas</td>
<td>2</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Ponte Preta</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>3</td>
<td>Amazonas</td>
<td>2</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>CRB</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>3</td>
<td>Amazonas</td>
<td>0</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Botafogo SP</td>
<td>11</td>
<td class="text-center"><span class="badge text-bg-warning">22</span></td>
<td>11</td>
<td>Ituano</td>
<td>6</td>
<td>6</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>6</td>
<td>Operario PR</td>
<td>2</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>3</td>
<td>Guarani</td>
<td>0</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>4</td>
<td>CRB</td>
<td>3</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>3</td>
<td>Santos</td>
<td>3</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">17</span></td>
<td>8</td>
<td>Goias</td>
<td>2</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>4</td>
<td>Paysandu</td>
<td>1</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>6</td>
<td>Coritiba</td>
<td>1</td>
<td>5</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>2</td>
<td>Brusque</td>
<td>3</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>11</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>4</td>
<td>Amazonas</td>
<td>2</td>
<td>4</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>5</td>
<td>Sport Recife</td>
<td>2</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>1</td>
<td>Ponte Preta</td>
<td>3</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>5</td>
<td>Vila Nova</td>
<td>3</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>3</td>
<td>Novorizontino</td>
<td>3</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>14</td>
<td class="text-center"><span class="badge text-bg-warning">16</span></td>
<td>2</td>
<td>Chapecoense</td>
<td>5</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>5</td>
<td>Mirassol</td>
<td>5</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">3</span></td>
<td>1</td>
<td>America MG</td>
<td>0</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Sport Recife</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>1</td>
<td>Botafogo SP</td>
<td>5</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Ponte Preta</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>3</td>
<td>Botafogo SP</td>
<td>2</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Vila Nova</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>4</td>
<td>Botafogo SP</td>
<td>1</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>8</td>
<td>Botafogo SP</td>
<td>4</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Chapecoense</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>5</td>
<td>Botafogo SP</td>
<td>4</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Mirassol</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>6</td>
<td>Botafogo SP</td>
<td>0</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>America MG</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>5</td>
<td>Botafogo SP</td>
<td>3</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Avai</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>5</td>
<td>Botafogo SP</td>
<td>2</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Ceara</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>3</td>
<td>Botafogo SP</td>
<td>1</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>CRB</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>4</td>
<td>Botafogo SP</td>
<td>0</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Ituano</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>13</td>
<td>Botafogo SP</td>
<td>1</td>
<td>5</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Operario PR</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>2</td>
<td>Botafogo SP</td>
<td>5</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Santos</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>1</td>
<td>Botafogo SP</td>
<td>3</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Goias</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">3</span></td>
<td>2</td>
<td>Botafogo SP</td>
<td>1</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Botafogo SP</td>
<td>3</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Paysandu</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>2</td>
<td>Botafogo SP</td>
<td>3</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>1</td>
<td>Botafogo SP</td>
<td>3</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading1">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1" aria-expanded="true" aria-controls="collapse1">
<span class="h4">Deportivo Pasto vs Aguilas Doradas <span class= "badge text-bg-dark">-2.86</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse1" class="accordion-collapse collapse" aria-labelledby="heading1" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Deportivo Pasto</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>2</td>
<td>Atletico Nacional Medellin</td>
<td>3</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>11</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>1</td>
<td>Alianza</td>
<td>6</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>7</td>
<td>Independiente Medellin</td>
<td>3</td>
<td>3</td>
<td>8.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>2</td>
<td>Junior</td>
<td>3</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>1</td>
<td>Atletico Bucaramanga</td>
<td>3</td>
<td>0</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>1</td>
<td>Deportivo Pereira</td>
<td>4</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>7</td>
<td>La Equidad</td>
<td>1</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">4</span></td>
<td>1</td>
<td>Millonarios</td>
<td>2</td>
<td>0</td>
<td>8.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>3</td>
<td>Once Caldas</td>
<td>1</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>3</td>
<td>Boyaca Chico</td>
<td>6</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>4</td>
<td>Fortaleza CEIF</td>
<td>0</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>5</td>
<td>Deportivo Cali</td>
<td>3</td>
<td>4</td>
<td>11.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>1</td>
<td>Envigado FC</td>
<td>3</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>2</td>
<td>Jaguares de Cordoba</td>
<td>2</td>
<td>0</td>
<td>12.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>5</td>
<td>Deportes Tolima</td>
<td>0</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">4</span></td>
<td>0</td>
<td>Independiente Santa Fe</td>
<td>2</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>5</td>
<td>Aguilas Doradas</td>
<td>0</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Once Caldas</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Deportivo Pasto</td>
<td>1</td>
<td>0</td>
<td>9.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>3</td>
<td>Deportivo Pasto</td>
<td>8</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Boyaca Chico</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>3</td>
<td>Deportivo Pasto</td>
<td>5</td>
<td>0</td>
<td>9.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Fortaleza CEIF</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>4</td>
<td>Deportivo Pasto</td>
<td>1</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Cali</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>4</td>
<td>Deportivo Pasto</td>
<td>2</td>
<td>3</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Jaguares de Cordoba</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>1</td>
<td>Deportivo Pasto</td>
<td>2</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportes Tolima</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">4</span></td>
<td>2</td>
<td>Deportivo Pasto</td>
<td>1</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Independiente Santa Fe</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>4</td>
<td>Deportivo Pasto</td>
<td>2</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Patriotas FC</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>5</td>
<td>Deportivo Pasto</td>
<td>1</td>
<td>0</td>
<td>8.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>America de Cali</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>1</td>
<td>Deportivo Pasto</td>
<td>4</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>2</td>
<td>Deportivo Pasto</td>
<td>3</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Atletico Nacional Medellin</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Deportivo Pasto</td>
<td>3</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Alianza</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>3</td>
<td>Deportivo Pasto</td>
<td>1</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Independiente Medellin</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">16</span></td>
<td>9</td>
<td>Deportivo Pasto</td>
<td>3</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Atletico Bucaramanga</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>6</td>
<td>Deportivo Pasto</td>
<td>2</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Junior</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">4</span></td>
<td>0</td>
<td>Deportivo Pasto</td>
<td>2</td>
<td>0</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>14</td>
<td class="text-center"><span class="badge text-bg-warning">17</span></td>
<td>3</td>
<td>Deportivo Pasto</td>
<td>6</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Aguilas Doradas</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>2</td>
<td>Atletico Bucaramanga</td>
<td>3</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>8</td>
<td>Deportivo Cali</td>
<td>5</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>2</td>
<td>Deportivo Pereira</td>
<td>3</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>10</td>
<td>Independiente Medellin</td>
<td>3</td>
<td>3</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>1</td>
<td>Millonarios</td>
<td>3</td>
<td>0</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>3</td>
<td>Jaguares de Cordoba</td>
<td>1</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>5</td>
<td>Patriotas FC</td>
<td>1</td>
<td>3</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>5</td>
<td>America de Cali</td>
<td>2</td>
<td>3</td>
<td>9.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>3</td>
<td>Fortaleza CEIF</td>
<td>4</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>0</td>
<td>Alianza</td>
<td>2</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>2</td>
<td>Deportivo Pasto</td>
<td>3</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">16</span></td>
<td>11</td>
<td>Independiente Santa Fe</td>
<td>3</td>
<td>6</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>3</td>
<td>Junior</td>
<td>4</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>0</td>
<td class="text-center"><span class="badge text-bg-warning">3</span></td>
<td>3</td>
<td>Envigado FC</td>
<td>0</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>4</td>
<td>La Equidad</td>
<td>4</td>
<td>2</td>
<td>12.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>5</td>
<td>Atletico Nacional Medellin</td>
<td>2</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>6</td>
<td>Once Caldas</td>
<td>1</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>6</td>
<td>Aguilas Doradas</td>
<td>3</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Independiente Santa Fe</td>
<td>11</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>1</td>
<td>Aguilas Doradas</td>
<td>2</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Junior</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>4</td>
<td>Aguilas Doradas</td>
<td>2</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>La Equidad</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>5</td>
<td>Aguilas Doradas</td>
<td>2</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Atletico Nacional Medellin</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>2</td>
<td>Aguilas Doradas</td>
<td>6</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Once Caldas</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>7</td>
<td>Aguilas Doradas</td>
<td>1</td>
<td>5</td>
<td>9.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Boyaca Chico</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>Aguilas Doradas</td>
<td>3</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportes Tolima</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>6</td>
<td>Aguilas Doradas</td>
<td>1</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Deportivo Cali</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>2</td>
<td>Aguilas Doradas</td>
<td>3</td>
<td>1</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Atletico Bucaramanga</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>3</td>
<td>Aguilas Doradas</td>
<td>2</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">4</span></td>
<td>1</td>
<td>Aguilas Doradas</td>
<td>2</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Independiente Medellin</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>1</td>
<td>Aguilas Doradas</td>
<td>2</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Millonarios</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>3</td>
<td>Aguilas Doradas</td>
<td>3</td>
<td>3</td>
<td>8.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Jaguares de Cordoba</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>7</td>
<td>Aguilas Doradas</td>
<td>2</td>
<td>7</td>
<td>12.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Patriotas FC</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>Aguilas Doradas</td>
<td>3</td>
<td>1</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>America de Cali</td>
<td>11</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>2</td>
<td>Aguilas Doradas</td>
<td>7</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>5</td>
<td>Aguilas Doradas</td>
<td>0</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading2">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse2" aria-expanded="true" aria-controls="collapse2">
<span class="h4">Deportivo Pereira vs Envigado FC <span class= "badge text-bg-dark">-2.31</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse2" class="accordion-collapse collapse" aria-labelledby="heading2" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Deportivo Pereira</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>6</td>
<td>Deportes Tolima</td>
<td>1</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>5</td>
<td>Patriotas FC</td>
<td>0</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>1</td>
<td>Alianza</td>
<td>3</td>
<td>1</td>
<td>None</td>
<td><span class="badge text-bg-primary">None</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>1</td>
<td>Once Caldas</td>
<td>4</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>13</td>
<td class="text-center"><span class="badge text-bg-warning">16</span></td>
<td>3</td>
<td>Boyaca Chico</td>
<td>4</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>5</td>
<td>Independiente Medellin</td>
<td>4</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>Millonarios</td>
<td>2</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">16</span></td>
<td>11</td>
<td>Junior</td>
<td>4</td>
<td>6</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>7</td>
<td>Atletico Bucaramanga</td>
<td>0</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>Millonarios</td>
<td>1</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>2</td>
<td>Jaguares de Cordoba</td>
<td>7</td>
<td>2</td>
<td>11.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>1</td>
<td>Atletico Bucaramanga</td>
<td>2</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">4</span></td>
<td>1</td>
<td>Aguilas Doradas</td>
<td>2</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>7</td>
<td>America de Cali</td>
<td>4</td>
<td>6</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>5</td>
<td>Junior</td>
<td>7</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>5</td>
<td>Independiente Santa Fe</td>
<td>2</td>
<td>1</td>
<td>11.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>7</td>
<td>Fortaleza CEIF</td>
<td>3</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>14</td>
<td class="text-center"><span class="badge text-bg-warning">17</span></td>
<td>3</td>
<td>Deportivo Pasto</td>
<td>6</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>4</td>
<td>Deportivo Cali</td>
<td>4</td>
<td>2</td>
<td>None</td>
<td><span class="badge text-bg-primary">None</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>2</td>
<td>Envigado FC</td>
<td>3</td>
<td>0</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Junior</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>3</td>
<td>Deportivo Pereira</td>
<td>5</td>
<td>1</td>
<td>8.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Atletico Bucaramanga</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>4</td>
<td>Deportivo Pereira</td>
<td>3</td>
<td>4</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Independiente Santa Fe</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>7</td>
<td>Deportivo Pereira</td>
<td>3</td>
<td>4</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>2</td>
<td>Deportivo Pereira</td>
<td>3</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>America de Cali</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>4</td>
<td>Deportivo Pereira</td>
<td>1</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Fortaleza CEIF</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>5</td>
<td>Deportivo Pereira</td>
<td>1</td>
<td>0</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>1</td>
<td>Deportivo Pereira</td>
<td>4</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Cali</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>6</td>
<td>Deportivo Pereira</td>
<td>1</td>
<td>4</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Atletico Bucaramanga</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>1</td>
<td>Deportivo Pereira</td>
<td>3</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Junior</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">1</span></td>
<td>0</td>
<td>Deportivo Pereira</td>
<td>0</td>
<td>0</td>
<td>8.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Millonarios</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>7</td>
<td>Deportivo Pereira</td>
<td>1</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>La Equidad</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">3</span></td>
<td>0</td>
<td>Deportivo Pereira</td>
<td>2</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Atletico Nacional Medellin</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">3</span></td>
<td>0</td>
<td>Deportivo Pereira</td>
<td>1</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Deportivo Pereira</td>
<td>3</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportes Tolima</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">4</span></td>
<td>3</td>
<td>Deportivo Pereira</td>
<td>0</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Once Caldas</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>1</td>
<td>Deportivo Pereira</td>
<td>4</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Alianza</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Deportivo Pereira</td>
<td>3</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Boyaca Chico</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>8</td>
<td>Deportivo Pereira</td>
<td>3</td>
<td>4</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Independiente Medellin</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>6</td>
<td>Deportivo Pereira</td>
<td>3</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Envigado FC</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>6</td>
<td>Aguilas Doradas</td>
<td>3</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>3</td>
<td>Deportivo Pasto</td>
<td>8</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>8</td>
<td>Atletico Bucaramanga</td>
<td>5</td>
<td>3</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>7</td>
<td>Once Caldas</td>
<td>2</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>7</td>
<td>Fortaleza CEIF</td>
<td>4</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>7</td>
<td>Independiente Santa Fe</td>
<td>1</td>
<td>4</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>7</td>
<td>La Equidad</td>
<td>0</td>
<td>5</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>5</td>
<td>Independiente Medellin</td>
<td>0</td>
<td>4</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>4</td>
<td>Deportes Tolima</td>
<td>1</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Deportivo Pereira</td>
<td>3</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>6</td>
<td>Atletico Nacional Medellin</td>
<td>2</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>2</td>
<td>Millonarios</td>
<td>1</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>3</td>
<td>Jaguares de Cordoba</td>
<td>3</td>
<td>2</td>
<td>11.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>9</td>
<td>Patriotas FC</td>
<td>1</td>
<td>5</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>6</td>
<td>America de Cali</td>
<td>1</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>3</td>
<td>Alianza</td>
<td>2</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Envigado FC</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>9</td>
<td>Boyaca Chico</td>
<td>4</td>
<td>5</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Atletico Nacional Medellin</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">16</span></td>
<td>7</td>
<td>Envigado FC</td>
<td>6</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Millonarios</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>5</td>
<td>Envigado FC</td>
<td>6</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Jaguares de Cordoba</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>3</td>
<td>Envigado FC</td>
<td>2</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Patriotas FC</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>1</td>
<td>Envigado FC</td>
<td>3</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Boyaca Chico</td>
<td>12</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>0</td>
<td>Envigado FC</td>
<td>4</td>
<td>0</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Alianza</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>3</td>
<td>Envigado FC</td>
<td>5</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>America de Cali</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>3</td>
<td>Envigado FC</td>
<td>1</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Cali</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>2</td>
<td>Envigado FC</td>
<td>5</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Junior</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>3</td>
<td>Envigado FC</td>
<td>5</td>
<td>3</td>
<td>8.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Atletico Bucaramanga</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">4</span></td>
<td>1</td>
<td>Envigado FC</td>
<td>1</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Once Caldas</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>2</td>
<td>Envigado FC</td>
<td>3</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Aguilas Doradas</td>
<td>0</td>
<td class="text-center"><span class="badge text-bg-warning">3</span></td>
<td>3</td>
<td>Envigado FC</td>
<td>0</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Deportivo Pasto</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>1</td>
<td>Envigado FC</td>
<td>3</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Fortaleza CEIF</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>8</td>
<td>Envigado FC</td>
<td>2</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Independiente Santa Fe</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>3</td>
<td>Envigado FC</td>
<td>3</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>La Equidad</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>3</td>
<td>Envigado FC</td>
<td>3</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Deportivo Pereira</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>2</td>
<td>Envigado FC</td>
<td>3</td>
<td>0</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading3">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse3" aria-expanded="true" aria-controls="collapse3">
<span class="h4">Feyenoord vs Ajax <span class= "badge text-bg-dark">7.52</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse3" class="accordion-collapse collapse" aria-labelledby="heading3" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Feyenoord</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>6</td>
<td>FC Twente</td>
<td>0</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Feyenoord</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>2</td>
<td>NAC</td>
<td>0</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Feyenoord</td>
<td>14</td>
<td class="text-center"><span class="badge text-bg-warning">17</span></td>
<td>3</td>
<td>Willem II</td>
<td>6</td>
<td>3</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>FC Utrecht</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>8</td>
<td>Feyenoord</td>
<td>0</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Go Ahead Eagles</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>6</td>
<td>Feyenoord</td>
<td>0</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>NEC</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>9</td>
<td>Feyenoord</td>
<td>0</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>FC Groningen</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>6</td>
<td>Feyenoord</td>
<td>2</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Sparta Rotterdam</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">17</span></td>
<td>11</td>
<td>Feyenoord</td>
<td>2</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>PEC Zwolle</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">3</span></td>
<td>2</td>
<td>Feyenoord</td>
<td>1</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Ajax</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>1</td>
<td>Willem II</td>
<td>0</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Ajax</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>2</td>
<td>FC Groningen</td>
<td>0</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Ajax</td>
<td>15</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>0</td>
<td>Fortuna Sittard</td>
<td>0</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Ajax</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>2</td>
<td>Heerenveen</td>
<td>2</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Heracles</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">3</span></td>
<td>0</td>
<td>Ajax</td>
<td>0</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>RKC</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>12</td>
<td>Ajax</td>
<td>0</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Go Ahead Eagles</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>2</td>
<td>Ajax</td>
<td>0</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>NAC</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>8</td>
<td>Ajax</td>
<td>0</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading4">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse4" aria-expanded="true" aria-controls="collapse4">
<span class="h4">Guarani vs Novorizontino <span class= "badge text-bg-dark">2.08</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse4" class="accordion-collapse collapse" aria-labelledby="heading4" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Guarani</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>7</td>
<td>CRB</td>
<td>2</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>7</td>
<td>Avai</td>
<td>3</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>4</td>
<td>Mirassol</td>
<td>0</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">16</span></td>
<td>7</td>
<td>Coritiba</td>
<td>4</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>4</td>
<td>Santos</td>
<td>1</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Vila Nova</td>
<td>1</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>2</td>
<td>Brusque</td>
<td>2</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>1</td>
<td>Goias</td>
<td>7</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>5</td>
<td>Sport Recife</td>
<td>4</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>6</td>
<td>Ponte Preta</td>
<td>2</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>2</td>
<td>Ituano</td>
<td>4</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>5</td>
<td>Operario PR</td>
<td>3</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>6</td>
<td>Paysandu</td>
<td>2</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>8</td>
<td>America MG</td>
<td>5</td>
<td>5</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Botafogo SP</td>
<td>3</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>14</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>0</td>
<td>Chapecoense</td>
<td>7</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>7</td>
<td>Novorizontino</td>
<td>4</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Sport Recife</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>4</td>
<td>Guarani</td>
<td>3</td>
<td>3</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Ponte Preta</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>6</td>
<td>Guarani</td>
<td>3</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>3</td>
<td>Guarani</td>
<td>0</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Ituano</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>5</td>
<td>Guarani</td>
<td>2</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Operario PR</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>7</td>
<td>Guarani</td>
<td>3</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Paysandu</td>
<td>12</td>
<td class="text-center"><span class="badge text-bg-warning">20</span></td>
<td>8</td>
<td>Guarani</td>
<td>10</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>America MG</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>11</td>
<td>Guarani</td>
<td>1</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Chapecoense</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>Guarani</td>
<td>0</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Ceara</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>4</td>
<td>Guarani</td>
<td>2</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>12</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>2</td>
<td>Guarani</td>
<td>6</td>
<td>0</td>
<td>11.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>4</td>
<td>Guarani</td>
<td>0</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>CRB</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>10</td>
<td>Guarani</td>
<td>2</td>
<td>7</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Avai</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>4</td>
<td>Guarani</td>
<td>2</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Mirassol</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>7</td>
<td>Guarani</td>
<td>2</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Coritiba</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>5</td>
<td>Guarani</td>
<td>1</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Santos</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>7</td>
<td>Guarani</td>
<td>2</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Vila Nova</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>7</td>
<td>Guarani</td>
<td>1</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Novorizontino</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>5</td>
<td>Avai</td>
<td>2</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>5</td>
<td>Sport Recife</td>
<td>2</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Ponte Preta</td>
<td>2</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>2</td>
<td>Brusque</td>
<td>2</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>8</td>
<td>Botafogo SP</td>
<td>4</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Vila Nova</td>
<td>3</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>3</td>
<td>Ituano</td>
<td>2</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>6</td>
<td>America MG</td>
<td>0</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>2</td>
<td>Goias</td>
<td>3</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>7</td>
<td>Chapecoense</td>
<td>4</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>4</td>
<td>Guarani</td>
<td>0</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>6</td>
<td>Mirassol</td>
<td>2</td>
<td>5</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>2</td>
<td>Amazonas</td>
<td>1</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">4</span></td>
<td>1</td>
<td>Santos</td>
<td>0</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>6</td>
<td>Coritiba</td>
<td>4</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>2</td>
<td>Ceara</td>
<td>4</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Novorizontino</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>6</td>
<td>CRB</td>
<td>4</td>
<td>3</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Mirassol</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>4</td>
<td>Novorizontino</td>
<td>8</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Amazonas</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>7</td>
<td>Novorizontino</td>
<td>3</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Santos</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">3</span></td>
<td>1</td>
<td>Novorizontino</td>
<td>1</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Coritiba</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>5</td>
<td>Novorizontino</td>
<td>3</td>
<td>2</td>
<td>None</td>
<td><span class="badge text-bg-primary">None</span></td>
</tr>

<tr>
<td>Ceara</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>3</td>
<td>Novorizontino</td>
<td>4</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>CRB</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>8</td>
<td>Novorizontino</td>
<td>1</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Paysandu</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>2</td>
<td>Novorizontino</td>
<td>3</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Operario PR</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>5</td>
<td>Novorizontino</td>
<td>1</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Avai</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>2</td>
<td>Novorizontino</td>
<td>2</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Sport Recife</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>4</td>
<td>Novorizontino</td>
<td>3</td>
<td>0</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Ponte Preta</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>3</td>
<td>Novorizontino</td>
<td>1</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Brusque</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>Novorizontino</td>
<td>5</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Botafogo SP</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>3</td>
<td>Novorizontino</td>
<td>3</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Vila Nova</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Novorizontino</td>
<td>2</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Ituano</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>12</td>
<td>Novorizontino</td>
<td>1</td>
<td>6</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>America MG</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>2</td>
<td>Novorizontino</td>
<td>2</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Guarani</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>7</td>
<td>Novorizontino</td>
<td>4</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading5">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse5" aria-expanded="true" aria-controls="collapse5">
<span class="h4">Atalanta vs Monza <span class= "badge text-bg-dark">-8.47</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse5" class="accordion-collapse collapse" aria-labelledby="heading5" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Atalanta</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>2</td>
<td>Verona</td>
<td>2</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Atalanta</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>2</td>
<td>Genua</td>
<td>3</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Atalanta</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>2</td>
<td>Como</td>
<td>3</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Atalanta</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>2</td>
<td>Fiorentina</td>
<td>2</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Venezia</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>5</td>
<td>Atalanta</td>
<td>1</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Bologna</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>9</td>
<td>Atalanta</td>
<td>1</td>
<td>4</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Inter Milan</td>
<td>0</td>
<td class="text-center"><span class="badge text-bg-warning">0</span></td>
<td>0</td>
<td>Atalanta</td>
<td>0</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Torino</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>6</td>
<td>Atalanta</td>
<td>2</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Lecce</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>3</td>
<td>Atalanta</td>
<td>3</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Monza</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>3</td>
<td>Venezia</td>
<td>2</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Monza</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">4</span></td>
<td>3</td>
<td>Roma</td>
<td>1</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Monza</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">4</span></td>
<td>2</td>
<td>Bologna</td>
<td>2</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Monza</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>8</td>
<td>Inter Milan</td>
<td>0</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Monza</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>3</td>
<td>Genua</td>
<td>2</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Verona</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>6</td>
<td>Monza</td>
<td>6</td>
<td>3</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Napoli</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">4</span></td>
<td>3</td>
<td>Monza</td>
<td>0</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Fiorentina</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>0</td>
<td>Monza</td>
<td>3</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Empoli</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>Monza</td>
<td>2</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading6">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse6" aria-expanded="true" aria-controls="collapse6">
<span class="h4">Cittadella vs Sampdoria <span class= "badge text-bg-dark">-1.46</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse6" class="accordion-collapse collapse" aria-labelledby="heading6" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Cittadella</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>4</td>
<td>Cosenza</td>
<td>6</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Cittadella</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>4</td>
<td>Frosinone</td>
<td>2</td>
<td>3</td>
<td>8.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Cittadella</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>2</td>
<td>Catanzaro</td>
<td>5</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Cittadella</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>5</td>
<td>Pisa</td>
<td>1</td>
<td>4</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Carrarese</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>8</td>
<td>Cittadella</td>
<td>1</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Sassuolo</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>3</td>
<td>Cittadella</td>
<td>2</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Mantova</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>4</td>
<td>Cittadella</td>
<td>4</td>
<td>3</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Modena</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>3</td>
<td>Cittadella</td>
<td>5</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Brescia</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Cittadella</td>
<td>2</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Salernitana</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>1</td>
<td>Cittadella</td>
<td>9</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Sampdoria</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>5</td>
<td>Mantova</td>
<td>2</td>
<td>4</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Sampdoria</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">3</span></td>
<td>1</td>
<td>Juve Stabia</td>
<td>1</td>
<td>0</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Sampdoria</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>2</td>
<td>Sudtirol</td>
<td>1</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Sampdoria</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>4</td>
<td>Bari</td>
<td>0</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Sampdoria</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>4</td>
<td>AC Reggiana</td>
<td>2</td>
<td>3</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Cesena</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>5</td>
<td>Sampdoria</td>
<td>2</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Modena</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>6</td>
<td>Sampdoria</td>
<td>2</td>
<td>5</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Cosenza</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>9</td>
<td>Sampdoria</td>
<td>0</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Salernitana</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>4</td>
<td>Sampdoria</td>
<td>4</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Frosinone</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>4</td>
<td>Sampdoria</td>
<td>0</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading7">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse7" aria-expanded="true" aria-controls="collapse7">
<span class="h4">Empoli vs Inter Milan <span class= "badge text-bg-dark">4.26</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse7" class="accordion-collapse collapse" aria-labelledby="heading7" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Empoli</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>7</td>
<td>Napoli</td>
<td>5</td>
<td>5</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Empoli</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>4</td>
<td>Fiorentina</td>
<td>1</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Empoli</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>8</td>
<td>Juventus</td>
<td>2</td>
<td>6</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Empoli</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>Monza</td>
<td>2</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Parma</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>3</td>
<td>Empoli</td>
<td>5</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Lazio</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>3</td>
<td>Empoli</td>
<td>5</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Cagliari</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>4</td>
<td>Empoli</td>
<td>5</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Bologna</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>3</td>
<td>Empoli</td>
<td>3</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Roma</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>5</td>
<td>Empoli</td>
<td>3</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Inter Milan</td>
<td>13</td>
<td class="text-center"><span class="badge text-bg-warning">18</span></td>
<td>5</td>
<td>Juventus</td>
<td>3</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Inter Milan</td>
<td>14</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>0</td>
<td>Torino</td>
<td>6</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Inter Milan</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>2</td>
<td>AC Milan</td>
<td>4</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Inter Milan</td>
<td>0</td>
<td class="text-center"><span class="badge text-bg-warning">0</span></td>
<td>0</td>
<td>Atalanta</td>
<td>0</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Inter Milan</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">16</span></td>
<td>6</td>
<td>Lecce</td>
<td>5</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Roma</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>3</td>
<td>Inter Milan</td>
<td>1</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Udinese</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>Inter Milan</td>
<td>2</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Monza</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>8</td>
<td>Inter Milan</td>
<td>0</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Genua</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>4</td>
<td>Inter Milan</td>
<td>0</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading8">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse8" aria-expanded="true" aria-controls="collapse8">
<span class="h4">Juventus vs Parma <span class= "badge text-bg-dark">3.43</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse8" class="accordion-collapse collapse" aria-labelledby="heading8" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Juventus</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>1</td>
<td>Lazio</td>
<td>4</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Juventus</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>3</td>
<td>Cagliari</td>
<td>6</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Juventus</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>3</td>
<td>Napoli</td>
<td>2</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Juventus</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>4</td>
<td>Roma</td>
<td>4</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Juventus</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">3</span></td>
<td>0</td>
<td>Como</td>
<td>1</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Inter Milan</td>
<td>13</td>
<td class="text-center"><span class="badge text-bg-warning">18</span></td>
<td>5</td>
<td>Juventus</td>
<td>3</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Genua</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>3</td>
<td>Juventus</td>
<td>2</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Empoli</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>8</td>
<td>Juventus</td>
<td>2</td>
<td>6</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Verona</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>1</td>
<td>Juventus</td>
<td>1</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Parma</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>3</td>
<td>Empoli</td>
<td>5</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Parma</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>3</td>
<td>Cagliari</td>
<td>4</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Parma</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>6</td>
<td>Udinese</td>
<td>3</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Parma</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>9</td>
<td>AC Milan</td>
<td>1</td>
<td>9</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Parma</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>9</td>
<td>Fiorentina</td>
<td>3</td>
<td>6</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Como</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>1</td>
<td>Parma</td>
<td>3</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Bologna</td>
<td>13</td>
<td class="text-center"><span class="badge text-bg-warning">19</span></td>
<td>6</td>
<td>Parma</td>
<td>5</td>
<td>5</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Lecce</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>12</td>
<td>Parma</td>
<td>2</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Napoli</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>4</td>
<td>Parma</td>
<td>3</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading9">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse9" aria-expanded="true" aria-controls="collapse9">
<span class="h4">Mantova vs Palermo <span class= "badge text-bg-dark">1.33</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse9" class="accordion-collapse collapse" aria-labelledby="heading9" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Mantova</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>3</td>
<td>Brescia</td>
<td>2</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Mantova</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>4</td>
<td>Cittadella</td>
<td>4</td>
<td>3</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Mantova</td>
<td>0</td>
<td class="text-center"><span class="badge text-bg-warning">1</span></td>
<td>1</td>
<td>Salernitana</td>
<td>0</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Mantova</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>5</td>
<td>Cosenza</td>
<td>3</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Sampdoria</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>5</td>
<td>Mantova</td>
<td>2</td>
<td>4</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Carrarese</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>3</td>
<td>Mantova</td>
<td>4</td>
<td>0</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Cesena</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>8</td>
<td>Mantova</td>
<td>5</td>
<td>4</td>
<td>8.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Bari</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>5</td>
<td>Mantova</td>
<td>4</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Juve Stabia</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>7</td>
<td>Mantova</td>
<td>3</td>
<td>2</td>
<td>8.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>AC Reggiana</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">4</span></td>
<td>1</td>
<td>Mantova</td>
<td>3</td>
<td>0</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Palermo</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>AC Reggiana</td>
<td>4</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Palermo</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>2</td>
<td>Salernitana</td>
<td>1</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Palermo</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>4</td>
<td>Cesena</td>
<td>3</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Palermo</td>
<td>12</td>
<td class="text-center"><span class="badge text-bg-warning">20</span></td>
<td>8</td>
<td>Cosenza</td>
<td>8</td>
<td>4</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Modena</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>4</td>
<td>Palermo</td>
<td>2</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Sudtirol</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>6</td>
<td>Palermo</td>
<td>3</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Juve Stabia</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>2</td>
<td>Palermo</td>
<td>2</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Cremonese</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>5</td>
<td>Palermo</td>
<td>3</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Pisa</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>7</td>
<td>Palermo</td>
<td>1</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Brescia</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>6</td>
<td>Palermo</td>
<td>1</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading10">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse10" aria-expanded="true" aria-controls="collapse10">
<span class="h4">Pisa vs Catanzaro <span class= "badge text-bg-dark">-7.51</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse10" class="accordion-collapse collapse" aria-labelledby="heading10" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Pisa</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>7</td>
<td>Cesena</td>
<td>4</td>
<td>2</td>
<td>8.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Pisa</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>4</td>
<td>Brescia</td>
<td>0</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Pisa</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>4</td>
<td>AC Reggiana</td>
<td>0</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Pisa</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>7</td>
<td>Palermo</td>
<td>1</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Pisa</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>2</td>
<td>Spezia</td>
<td>4</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Frosinone</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">17</span></td>
<td>13</td>
<td>Pisa</td>
<td>1</td>
<td>7</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Sudtirol</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>2</td>
<td>Pisa</td>
<td>3</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Juve Stabia</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>1</td>
<td>Pisa</td>
<td>4</td>
<td>0</td>
<td>8.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Salernitana</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>0</td>
<td>Pisa</td>
<td>4</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Cittadella</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>5</td>
<td>Pisa</td>
<td>1</td>
<td>4</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Catanzaro</td>
<td>0</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>8</td>
<td>Sudtirol</td>
<td>0</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Catanzaro</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>8</td>
<td>Modena</td>
<td>0</td>
<td>6</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Catanzaro</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>6</td>
<td>Cremonese</td>
<td>1</td>
<td>5</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Catanzaro</td>
<td>0</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>5</td>
<td>Carrarese</td>
<td>0</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Catanzaro</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>4</td>
<td>Juve Stabia</td>
<td>4</td>
<td>3</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Catanzaro</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>7</td>
<td>Sassuolo</td>
<td>2</td>
<td>5</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Bari</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>5</td>
<td>Catanzaro</td>
<td>1</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Salernitana</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>0</td>
<td>Catanzaro</td>
<td>0</td>
<td>0</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Cittadella</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>2</td>
<td>Catanzaro</td>
<td>5</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Cesena</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>2</td>
<td>Catanzaro</td>
<td>1</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading11">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse11" aria-expanded="true" aria-controls="collapse11">
<span class="h4">Sudtirol vs Frosinone <span class= "badge text-bg-dark">-1.96</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse11" class="accordion-collapse collapse" aria-labelledby="heading11" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Sudtirol</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>2</td>
<td>Pisa</td>
<td>3</td>
<td>2</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Sudtirol</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>6</td>
<td>Palermo</td>
<td>3</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Sudtirol</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>3</td>
<td>Brescia</td>
<td>6</td>
<td>0</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Sudtirol</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>5</td>
<td>Salernitana</td>
<td>3</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Sudtirol</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>2</td>
<td>Modena</td>
<td>2</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Catanzaro</td>
<td>0</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>8</td>
<td>Sudtirol</td>
<td>0</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Cosenza</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>0</td>
<td>Sudtirol</td>
<td>7</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Sampdoria</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>2</td>
<td>Sudtirol</td>
<td>1</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>AC Reggiana</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>5</td>
<td>Sudtirol</td>
<td>3</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Carrarese</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>8</td>
<td>Sudtirol</td>
<td>4</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Frosinone</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">17</span></td>
<td>13</td>
<td>Pisa</td>
<td>1</td>
<td>7</td>
<td>9.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Frosinone</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>5</td>
<td>Carrarese</td>
<td>4</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Frosinone</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>3</td>
<td>Bari</td>
<td>1</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Frosinone</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>2</td>
<td>Juve Stabia</td>
<td>3</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Frosinone</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>6</td>
<td>Modena</td>
<td>0</td>
<td>5</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Frosinone</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>4</td>
<td>Sampdoria</td>
<td>0</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>AC Reggiana</td>
<td>0</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>8</td>
<td>Frosinone</td>
<td>0</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Cittadella</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>4</td>
<td>Frosinone</td>
<td>2</td>
<td>3</td>
<td>8.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Brescia</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>1</td>
<td>Frosinone</td>
<td>2</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Spezia</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>7</td>
<td>Frosinone</td>
<td>3</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading12">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse12" aria-expanded="true" aria-controls="collapse12">
<span class="h4">Venezia vs Udinese <span class= "badge text-bg-dark">-5.15</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse12" class="accordion-collapse collapse" aria-labelledby="heading12" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Venezia</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>5</td>
<td>Atalanta</td>
<td>1</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Venezia</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>4</td>
<td>Genua</td>
<td>0</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Venezia</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>3</td>
<td>Torino</td>
<td>1</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Monza</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>3</td>
<td>Venezia</td>
<td>2</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Verona</td>
<td>13</td>
<td class="text-center"><span class="badge text-bg-warning">19</span></td>
<td>6</td>
<td>Venezia</td>
<td>6</td>
<td>5</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Roma</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>3</td>
<td>Venezia</td>
<td>2</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>AC Milan</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>1</td>
<td>Venezia</td>
<td>2</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Fiorentina</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>Venezia</td>
<td>3</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Lazio</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>3</td>
<td>Venezia</td>
<td>3</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Udinese</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>4</td>
<td>Cagliari</td>
<td>2</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Udinese</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>0</td>
<td>Lecce</td>
<td>2</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Udinese</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>Inter Milan</td>
<td>2</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Udinese</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>6</td>
<td>Como</td>
<td>1</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Udinese</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">17</span></td>
<td>13</td>
<td>Lazio</td>
<td>2</td>
<td>6</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>AC Milan</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>4</td>
<td>Udinese</td>
<td>5</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Roma</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">3</span></td>
<td>1</td>
<td>Udinese</td>
<td>1</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Parma</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>6</td>
<td>Udinese</td>
<td>3</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Bologna</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>5</td>
<td>Udinese</td>
<td>3</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading13">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse13" aria-expanded="true" aria-controls="collapse13">
<span class="h4">Aberdeen vs Rangers <span class= "badge text-bg-dark">8.31</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse13" class="accordion-collapse collapse" aria-labelledby="heading13" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Aberdeen</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>2</td>
<td>Dundee Utd</td>
<td>3</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Aberdeen</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>5</td>
<td>Hearts</td>
<td>2</td>
<td>3</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Aberdeen</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>5</td>
<td>Motherwell</td>
<td>2</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Aberdeen</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>6</td>
<td>Kilmarnock</td>
<td>3</td>
<td>3</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Aberdeen</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>2</td>
<td>St Mirren</td>
<td>2</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Celtic</td>
<td>18</td>
<td class="text-center"><span class="badge text-bg-warning">20</span></td>
<td>2</td>
<td>Aberdeen</td>
<td>5</td>
<td>1</td>
<td>12.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Dundee</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>3</td>
<td>Aberdeen</td>
<td>4</td>
<td>2</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Ross County</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>12</td>
<td>Aberdeen</td>
<td>0</td>
<td>5</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>St Johnstone</td>
<td>12</td>
<td class="text-center"><span class="badge text-bg-warning">19</span></td>
<td>7</td>
<td>Aberdeen</td>
<td>5</td>
<td>5</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Rangers</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>St Mirren</td>
<td>4</td>
<td>1</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Rangers</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>St Johnstone</td>
<td>3</td>
<td>0</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Rangers</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>7</td>
<td>Hibernian</td>
<td>4</td>
<td>3</td>
<td>11.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Rangers</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>0</td>
<td>Ross County</td>
<td>3</td>
<td>0</td>
<td>11.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Rangers</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>4</td>
<td>Motherwell</td>
<td>4</td>
<td>1</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Kilmarnock</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>6</td>
<td>Rangers</td>
<td>1</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Dundee Utd</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>4</td>
<td>Rangers</td>
<td>0</td>
<td>3</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Celtic</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>4</td>
<td>Rangers</td>
<td>4</td>
<td>1</td>
<td>11.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Hearts</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>7</td>
<td>Rangers</td>
<td>4</td>
<td>3</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading14">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse14" aria-expanded="true" aria-controls="collapse14">
<span class="h4">Celtic vs Dundee <span class= "badge text-bg-dark">12.24</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse14" class="accordion-collapse collapse" aria-labelledby="heading14" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Celtic</td>
<td>18</td>
<td class="text-center"><span class="badge text-bg-warning">20</span></td>
<td>2</td>
<td>Aberdeen</td>
<td>5</td>
<td>1</td>
<td>12.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Celtic</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>3</td>
<td>Hearts</td>
<td>3</td>
<td>2</td>
<td>11.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Celtic</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>4</td>
<td>Rangers</td>
<td>4</td>
<td>1</td>
<td>11.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Celtic</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>1</td>
<td>Kilmarnock</td>
<td>5</td>
<td>0</td>
<td>11.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Motherwell</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>10</td>
<td>Celtic</td>
<td>2</td>
<td>6</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Ross County</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>9</td>
<td>Celtic</td>
<td>1</td>
<td>4</td>
<td>11.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>St Johnstone</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">16</span></td>
<td>13</td>
<td>Celtic</td>
<td>1</td>
<td>7</td>
<td>11.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>St Mirren</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>10</td>
<td>Celtic</td>
<td>0</td>
<td>6</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Hibernian</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>5</td>
<td>Celtic</td>
<td>1</td>
<td>0</td>
<td>11.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Dundee</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>3</td>
<td>St Johnstone</td>
<td>1</td>
<td>0</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Dundee</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>10</td>
<td>Kilmarnock</td>
<td>1</td>
<td>2</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Dundee</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>3</td>
<td>Aberdeen</td>
<td>4</td>
<td>2</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Dundee</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>1</td>
<td>St Mirren</td>
<td>1</td>
<td>0</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Dundee</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>10</td>
<td>Hearts</td>
<td>1</td>
<td>2</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Ross County</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>8</td>
<td>Dundee</td>
<td>2</td>
<td>3</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Hibernian</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Dundee</td>
<td>2</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Dundee Utd</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>6</td>
<td>Dundee</td>
<td>2</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Motherwell</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>4</td>
<td>Dundee</td>
<td>1</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading15">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse15" aria-expanded="true" aria-controls="collapse15">
<span class="h4">Dundee Utd vs Motherwell <span class= "badge text-bg-dark">4.39</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse15" class="accordion-collapse collapse" aria-labelledby="heading15" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Dundee Utd</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>5</td>
<td>Hibernian</td>
<td>3</td>
<td>4</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Dundee Utd</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>4</td>
<td>Rangers</td>
<td>0</td>
<td>3</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Dundee Utd</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>6</td>
<td>St Johnstone</td>
<td>1</td>
<td>3</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Dundee Utd</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>6</td>
<td>Dundee</td>
<td>2</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Aberdeen</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>2</td>
<td>Dundee Utd</td>
<td>3</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>St Mirren</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>3</td>
<td>Dundee Utd</td>
<td>2</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Kilmarnock</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>Dundee Utd</td>
<td>3</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Hearts</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>4</td>
<td>Dundee Utd</td>
<td>2</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Ross County</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>5</td>
<td>Dundee Utd</td>
<td>4</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Motherwell</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>10</td>
<td>Celtic</td>
<td>2</td>
<td>6</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Motherwell</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>6</td>
<td>St Mirren</td>
<td>6</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Motherwell</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>7</td>
<td>Hearts</td>
<td>5</td>
<td>4</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Motherwell</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>3</td>
<td>Ross County</td>
<td>2</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Motherwell</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>4</td>
<td>Dundee</td>
<td>1</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Hibernian</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>5</td>
<td>Motherwell</td>
<td>5</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Aberdeen</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>5</td>
<td>Motherwell</td>
<td>2</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>St Johnstone</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">17</span></td>
<td>13</td>
<td>Motherwell</td>
<td>2</td>
<td>3</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Rangers</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>4</td>
<td>Motherwell</td>
<td>4</td>
<td>1</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading16">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse16" aria-expanded="true" aria-controls="collapse16">
<span class="h4">Hearts vs Kilmarnock <span class= "badge text-bg-dark">4.91</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse16" class="accordion-collapse collapse" aria-labelledby="heading16" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Hearts</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>6</td>
<td>St Mirren</td>
<td>1</td>
<td>3</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Hearts</td>
<td>11</td>
<td class="text-center"><span class="badge text-bg-warning">16</span></td>
<td>5</td>
<td>Ross County</td>
<td>2</td>
<td>3</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Hearts</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>4</td>
<td>Dundee Utd</td>
<td>2</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Hearts</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>7</td>
<td>Rangers</td>
<td>4</td>
<td>3</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Hibernian</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>6</td>
<td>Hearts</td>
<td>0</td>
<td>3</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Aberdeen</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>5</td>
<td>Hearts</td>
<td>2</td>
<td>3</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>St Mirren</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Hearts</td>
<td>2</td>
<td>2</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Celtic</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>3</td>
<td>Hearts</td>
<td>3</td>
<td>2</td>
<td>11.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Motherwell</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>7</td>
<td>Hearts</td>
<td>5</td>
<td>4</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Dundee</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>10</td>
<td>Hearts</td>
<td>1</td>
<td>2</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Kilmarnock</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>6</td>
<td>Rangers</td>
<td>1</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Kilmarnock</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>Dundee Utd</td>
<td>3</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Kilmarnock</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>7</td>
<td>Hibernian</td>
<td>1</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Kilmarnock</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>4</td>
<td>St Johnstone</td>
<td>1</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Ross County</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>5</td>
<td>Kilmarnock</td>
<td>2</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Dundee</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>10</td>
<td>Kilmarnock</td>
<td>1</td>
<td>2</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>St Mirren</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>10</td>
<td>Kilmarnock</td>
<td>1</td>
<td>7</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Aberdeen</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>6</td>
<td>Kilmarnock</td>
<td>3</td>
<td>3</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Celtic</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>1</td>
<td>Kilmarnock</td>
<td>5</td>
<td>0</td>
<td>11.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading17">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse17" aria-expanded="true" aria-controls="collapse17">
<span class="h4">Internacional vs Flamengo <span class= "badge text-bg-dark">2.23</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse17" class="accordion-collapse collapse" aria-labelledby="heading17" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Internacional</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>6</td>
<td>Gremio</td>
<td>3</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Internacional</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>6</td>
<td>Vitoria</td>
<td>2</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Internacional</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>3</td>
<td>Cuiaba</td>
<td>2</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Internacional</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>3</td>
<td>Fortaleza</td>
<td>2</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Internacional</td>
<td>12</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>3</td>
<td>Cruzeiro</td>
<td>6</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Internacional</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>1</td>
<td>Juventude</td>
<td>6</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Internacional</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>0</td>
<td>Athletico Paranaense</td>
<td>4</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Internacional</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>11</td>
<td>Palmeiras</td>
<td>3</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Internacional</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>4</td>
<td>Vasco da Gama</td>
<td>1</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Internacional</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>9</td>
<td>Atletico Mineiro</td>
<td>4</td>
<td>4</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Internacional</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>7</td>
<td>Corinthians</td>
<td>2</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Internacional</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>3</td>
<td>Sao Paulo</td>
<td>1</td>
<td>1</td>
<td>9.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Internacional</td>
<td>13</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>0</td>
<td>Atletico GO</td>
<td>5</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Internacional</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>3</td>
<td>Bahia</td>
<td>3</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Atletico Mineiro</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>3</td>
<td>Internacional</td>
<td>1</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Corinthians</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">18</span></td>
<td>9</td>
<td>Internacional</td>
<td>3</td>
<td>5</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Bragantino</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>9</td>
<td>Internacional</td>
<td>1</td>
<td>8</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Sao Paulo</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>4</td>
<td>Internacional</td>
<td>1</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Juventude</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>4</td>
<td>Internacional</td>
<td>5</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Cruzeiro</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>3</td>
<td>Internacional</td>
<td>6</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Atletico GO</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>7</td>
<td>Internacional</td>
<td>3</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Bahia</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>2</td>
<td>Internacional</td>
<td>2</td>
<td>0</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Botafogo</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">3</span></td>
<td>1</td>
<td>Internacional</td>
<td>2</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Fluminense</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>4</td>
<td>Internacional</td>
<td>2</td>
<td>2</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Criciuma</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>5</td>
<td>Internacional</td>
<td>0</td>
<td>3</td>
<td>9.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Gremio</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Internacional</td>
<td>4</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Vitoria</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>2</td>
<td>Internacional</td>
<td>0</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Cuiaba</td>
<td>0</td>
<td class="text-center"><span class="badge text-bg-warning">2</span></td>
<td>2</td>
<td>Internacional</td>
<td>0</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Athletico Paranaense</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>3</td>
<td>Internacional</td>
<td>2</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Palmeiras</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>2</td>
<td>Internacional</td>
<td>1</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Flamengo</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>1</td>
<td>Juventude</td>
<td>2</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Flamengo</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>1</td>
<td>Fluminense</td>
<td>2</td>
<td>1</td>
<td>9.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Flamengo</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>1</td>
<td>Athletico Paranaense</td>
<td>3</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Flamengo</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>6</td>
<td>Vasco da Gama</td>
<td>5</td>
<td>4</td>
<td>11.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Flamengo</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">16</span></td>
<td>10</td>
<td>Bragantino</td>
<td>4</td>
<td>6</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Flamengo</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>2</td>
<td>Palmeiras</td>
<td>4</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Flamengo</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>3</td>
<td>Atletico GO</td>
<td>5</td>
<td>1</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Flamengo</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>4</td>
<td>Criciuma</td>
<td>4</td>
<td>3</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Flamengo</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>4</td>
<td>Fortaleza</td>
<td>8</td>
<td>2</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Flamengo</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>0</td>
<td>Cuiaba</td>
<td>2</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Flamengo</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>5</td>
<td>Cruzeiro</td>
<td>1</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Flamengo</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>2</td>
<td>Bahia</td>
<td>2</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Flamengo</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>6</td>
<td>Gremio</td>
<td>1</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Flamengo</td>
<td>13</td>
<td class="text-center"><span class="badge text-bg-warning">19</span></td>
<td>6</td>
<td>Corinthians</td>
<td>8</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Flamengo</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>3</td>
<td>Botafogo</td>
<td>5</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Flamengo</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>1</td>
<td>Sao Paulo</td>
<td>2</td>
<td>0</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Bahia</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>7</td>
<td>Flamengo</td>
<td>3</td>
<td>4</td>
<td>10.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Gremio</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>6</td>
<td>Flamengo</td>
<td>3</td>
<td>4</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Corinthians</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>2</td>
<td>Flamengo</td>
<td>2</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Botafogo</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>2</td>
<td>Flamengo</td>
<td>4</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Sao Paulo</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>3</td>
<td>Flamengo</td>
<td>3</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Vitoria</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>8</td>
<td>Flamengo</td>
<td>3</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Atletico Mineiro</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>4</td>
<td>Flamengo</td>
<td>1</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Juventude</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>8</td>
<td>Flamengo</td>
<td>3</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Fluminense</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>6</td>
<td>Flamengo</td>
<td>2</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Athletico Paranaense</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">14</span></td>
<td>9</td>
<td>Flamengo</td>
<td>3</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Vasco da Gama</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>8</td>
<td>Flamengo</td>
<td>0</td>
<td>5</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Bragantino</td>
<td>8</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>4</td>
<td>Flamengo</td>
<td>4</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Palmeiras</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>5</td>
<td>Flamengo</td>
<td>3</td>
<td>2</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Atletico GO</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>4</td>
<td>Flamengo</td>
<td>3</td>
<td>1</td>
<td>10.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading18">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse18" aria-expanded="true" aria-controls="collapse18">
<span class="h4">Ross County vs Hibernian <span class= "badge text-bg-dark">-0.96</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse18" class="accordion-collapse collapse" aria-labelledby="heading18" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Ross County</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>5</td>
<td>Kilmarnock</td>
<td>2</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Ross County</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>9</td>
<td>Celtic</td>
<td>1</td>
<td>4</td>
<td>11.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Ross County</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">4</span></td>
<td>3</td>
<td>St Johnstone</td>
<td>0</td>
<td>3</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Ross County</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>8</td>
<td>Dundee</td>
<td>2</td>
<td>3</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Ross County</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>12</td>
<td>Aberdeen</td>
<td>0</td>
<td>5</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Ross County</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>5</td>
<td>Dundee Utd</td>
<td>4</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Hearts</td>
<td>11</td>
<td class="text-center"><span class="badge text-bg-warning">16</span></td>
<td>5</td>
<td>Ross County</td>
<td>2</td>
<td>3</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Rangers</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>0</td>
<td>Ross County</td>
<td>3</td>
<td>0</td>
<td>11.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Motherwell</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>3</td>
<td>Ross County</td>
<td>2</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>St Johnstone</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>2</td>
<td>Ross County</td>
<td>1</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>Hibernian</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>6</td>
<td>Hearts</td>
<td>0</td>
<td>3</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Hibernian</td>
<td>10</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>5</td>
<td>Motherwell</td>
<td>5</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Hibernian</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>7</td>
<td>St Johnstone</td>
<td>1</td>
<td>4</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Hibernian</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Dundee</td>
<td>2</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Hibernian</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>5</td>
<td>Celtic</td>
<td>1</td>
<td>0</td>
<td>11.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Dundee Utd</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>5</td>
<td>Hibernian</td>
<td>3</td>
<td>4</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Rangers</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>7</td>
<td>Hibernian</td>
<td>4</td>
<td>3</td>
<td>11.0</td>
<td><span class="badge text-bg-primary">Draw</span></td>
</tr>

<tr>
<td>Kilmarnock</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">11</span></td>
<td>7</td>
<td>Hibernian</td>
<td>1</td>
<td>3</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>St Mirren</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>8</td>
<td>Hibernian</td>
<td>2</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>


<div class="accordion">
<div class="accordion-item">
<h2 class="accordion-header" id="heading19">
<button class="accordion-button d-flex" type="button" data-bs-toggle="collapse" data-bs-target="#collapse19" aria-expanded="true" aria-controls="collapse19">
<span class="h4">St Mirren vs St Johnstone <span class= "badge text-bg-dark">-1.78</span>
<span class="text-right">pokaż szczegóły</span>
</button>
</h2>
<div id="collapse19" class="accordion-collapse collapse" aria-labelledby="heading19" data-bs-parent="#accordionExample">
<div class="accordion-body">
<div style="display: flex; justify-content: space-between;">
<div style="flex: 1; margin-right: 10px;">
<h5>Ilość rożnych w meczach gospodarzy</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>St Mirren</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">6</span></td>
<td>3</td>
<td>Dundee Utd</td>
<td>2</td>
<td>0</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>St Mirren</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">9</span></td>
<td>4</td>
<td>Hearts</td>
<td>2</td>
<td>2</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>St Mirren</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">13</span></td>
<td>10</td>
<td>Kilmarnock</td>
<td>1</td>
<td>7</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>St Mirren</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>10</td>
<td>Celtic</td>
<td>0</td>
<td>6</td>
<td>11.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>St Mirren</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>8</td>
<td>Hibernian</td>
<td>2</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Rangers</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>St Mirren</td>
<td>4</td>
<td>1</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Hearts</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>6</td>
<td>St Mirren</td>
<td>1</td>
<td>3</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Motherwell</td>
<td>9</td>
<td class="text-center"><span class="badge text-bg-warning">15</span></td>
<td>6</td>
<td>St Mirren</td>
<td>6</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Dundee</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>1</td>
<td>St Mirren</td>
<td>1</td>
<td>0</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Aberdeen</td>
<td>6</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>2</td>
<td>St Mirren</td>
<td>2</td>
<td>1</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Home Stats -->

<div style="flex: 1; margin-left: 10px;">
<h5>Ilość rożnych w meczach gości</h5>
<table class="table table-dark table-bordered table-sm text-center">
<thead>
<tr>
<th>Home</th>
<th>Home Corner</th>
<th>Suma</th>
<th>Away Corner</th>
<th>Away</th>
<th>HT Home Corner</th>
<th>HT Away Corner</th>
<th>Linia</th>
<th>U/O</th>
</tr>
</thead>
<tbody>

<tr>
<td>St Johnstone</td>
<td>3</td>
<td class="text-center"><span class="badge text-bg-warning">16</span></td>
<td>13</td>
<td>Celtic</td>
<td>1</td>
<td>7</td>
<td>11.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>St Johnstone</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">17</span></td>
<td>13</td>
<td>Motherwell</td>
<td>2</td>
<td>3</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>St Johnstone</td>
<td>12</td>
<td class="text-center"><span class="badge text-bg-warning">19</span></td>
<td>7</td>
<td>Aberdeen</td>
<td>5</td>
<td>5</td>
<td>10.0</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>St Johnstone</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">7</span></td>
<td>2</td>
<td>Ross County</td>
<td>1</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Dundee</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">5</span></td>
<td>3</td>
<td>St Johnstone</td>
<td>1</td>
<td>0</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Rangers</td>
<td>7</td>
<td class="text-center"><span class="badge text-bg-warning">10</span></td>
<td>3</td>
<td>St Johnstone</td>
<td>3</td>
<td>0</td>
<td>11.0</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Ross County</td>
<td>1</td>
<td class="text-center"><span class="badge text-bg-warning">4</span></td>
<td>3</td>
<td>St Johnstone</td>
<td>0</td>
<td>3</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Hibernian</td>
<td>5</td>
<td class="text-center"><span class="badge text-bg-warning">12</span></td>
<td>7</td>
<td>St Johnstone</td>
<td>1</td>
<td>4</td>
<td>10.5</td>
<td><span class="badge text-bg-success">Over</span></td>
</tr>

<tr>
<td>Dundee Utd</td>
<td>2</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>6</td>
<td>St Johnstone</td>
<td>1</td>
<td>3</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

<tr>
<td>Kilmarnock</td>
<td>4</td>
<td class="text-center"><span class="badge text-bg-warning">8</span></td>
<td>4</td>
<td>St Johnstone</td>
<td>1</td>
<td>2</td>
<td>10.5</td>
<td><span class="badge text-bg-danger">Under</span></td>
</tr>

</tbody>
</table>
</div> <!-- End of Away Stats -->
</div> <!-- End of Flex Container -->
</div>
</div>
</div>

</div>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
"""

# Wyświetlenie kodu HTML w Streamlit
st.markdown(html_code, unsafe_allow_html=True)
