#!/usr/bin/env python3
# app.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView

HTML_APP = r"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Neuro Churn - Dashboard</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
  body { font-family: 'Inter', sans-serif; background-color: #f9fafc; margin:0; padding:0; }
  header { padding:20px; background:#1E40AF; color:white; text-align:center; }
  .container { display:flex; justify-content:center; gap:20px; padding:20px; }
  .card { padding:20px; border-radius:12px; box-shadow:0 4px 8px rgba(0,0,0,0.1); background:#fff; }
  footer { text-align:center; margin-top:20px; color:#555; }
  button { padding:8px 15px; background:#1E40AF; color:#fff; border:none; cursor:pointer; }
</style>
</head>
<body>
<header>
  <h1>Neuro Churn Bank</h1>
  <p>Dashboard com IA para Predição de Churn</p>
</header>

<div class="container">
  <div class="card" style="width:250px">
    <h3>Simulador de Churn</h3>
    <input type="number" id="tenure" placeholder="Tempo Cliente (meses)"><br><br>
    <input type="number" id="monthlyValue" placeholder="Valor Mensal"><br><br>
    <input type="number" id="usage" placeholder="Uso (%)"><br><br>
    <select id="techSupport">
      <option value="0.8">Sem Suporte</option>
      <option value="0.4">Suporte Básico</option>
      <option value="0.1">Suporte Premium</option>
    </select><br><br>
    <select id="paymentMethod">
      <option value="0.2">Cartão Crédito</option>
      <option value="0.5">Boleto Bancário</option>
      <option value="0.1">Débito Automático</option>
      <option value="0.3">Pagamento Digital</option>
    </select><br><br>
    <button onclick="calculateChurn()">Calcular</button>
    <p id="result"></p>
    <p id="financialResult"></p>
  </div>

  <div class="card" style="width:600px;">
    <canvas id="chart1"></canvas>
  </div>
</div>

<div class="container">
  <div class="card" style="width:400px;">
    <canvas id="chart2"></canvas>
  </div>
  <div class="card" style="width:400px;">
    <canvas id="chart3"></canvas>
  </div>
  <div class="card" style="width:400px;">
    <canvas id="chart4"></canvas>
  </div>
</div>

<footer>Desenvolvido por Cezi Cola Tecnologia | 2025</footer>

<script>
const customerValue = 350;
const retentionCost = 120;
const acquisitionCost = 280;

function calculateChurn(){
  let score = (document.getElementById('tenure').value * 0.03) + 
              (document.getElementById('monthlyValue').value * 0.02) +
              (document.getElementById('usage').value * 0.025) +
              parseFloat(document.getElementById('techSupport').value) +
              parseFloat(document.getElementById('paymentMethod').value);

  document.getElementById('result').innerHTML = score > 0.7 ? 'Alto Risco: ' + score.toFixed(2) : 'Baixo Risco: ' + score.toFixed(2);

  let ganho = score > 0.7 ? (customerValue - retentionCost) : customerValue;
  let perda = score > 0.7 ? acquisitionCost : retentionCost;

  document.getElementById('financialResult').innerHTML = `Banco ganha: R$${ganho}, Banco perde se não agir: R$${perda}`;

  updateChart(score);
}

const ctx1 = document.getElementById('chart1').getContext('2d');
const chart1 = new Chart(ctx1, { type:'bar', data:{ labels:['Churn'], datasets:[{label:'Score', data:[0],backgroundColor:'#1E40AF'}]}, options:{scales:{y:{beginAtZero:true}}}});

function updateChart(score){ chart1.data.datasets[0].data[0]=score; chart1.update(); }

new Chart(document.getElementById('chart2'),{type:'pie',data:{labels:['Churn','Não Churn'],datasets:[{data:[35,65],backgroundColor:['#3B82F6','#1E40AF']}]}});

new Chart(document.getElementById('chart3'),{type:'line',data:{labels:['Jan','Fev','Mar','Abr'],datasets:[{label:'Churn %',data:[5,10,8,12],backgroundColor:'#1E40AF'}]}});

new Chart(document.getElementById('chart4'),{type:'doughnut',data:{labels:['Suporte Premium','Básico','Sem Suporte'],datasets:[{data:[20,30,50],backgroundColor:['#1E40AF','#3B82F6','#3ccfcf']}]} });
</script>

</body>
</html>
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Neuro Churn - Predição Inteligente")
        self.resize(1280, 800)
        web = QWebEngineView()
        web.setHtml(HTML_APP)
        self.setCentralWidget(web)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
