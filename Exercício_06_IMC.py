# -*- coding: latin1 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        # DIMENSÕES DA JANELA:
        self.topo = 400
        self.esquerda = 550
        self.largura = 575
        self.altura = 400
        self.titulo = "Cálculo do IMC - Índice de Massa Corporal"

        # CAIXAS DE TEXTO:
        self.caixa_nome = QLineEdit(self)
        self.caixa_nome.move(155, 20)
        self.caixa_nome.resize(400, 25)

        self.caixa_endereco = QLineEdit(self)
        self.caixa_endereco.move(155, 50)
        self.caixa_endereco.resize(400, 25)

        self.caixa_altura = QLineEdit(self)
        self.caixa_altura.move(155, 80)
        self.caixa_altura.resize(50, 25)

        self.caixa_peso = QLineEdit(self)
        self.caixa_peso.move(155, 110)
        self.caixa_peso.resize(50, 25)

        # BOTÕES:
        btCalc = QPushButton('Calcular', self)
        btCalc.move(20, 360)
        btCalc.resize(70, 25)
        btCalc.setStyleSheet('QPushButton {font-size:15px}')
        btCalc.clicked.connect(self.Mostra_resultado)

        btRein = QPushButton('Reiniciar', self)
        btRein.move(100, 360)
        btRein.resize(70, 25)
        btRein.setStyleSheet('QPushButton {font-size: 15px}')
        btRein.clicked.connect(self.btRein_click)

        btSair = QPushButton('Sair', self)
        btSair.move(475, 360)
        btSair.resize(70, 25)
        btSair.setStyleSheet('QPushButton {font-size:15px}')
        btSair.clicked.connect(self.btSair_click)

        # TEXTOS DAS CAIXAS DE TEXTO
        self.label_nome = QLabel(self)
        self.label_nome.setText("Nome do paciente:")
        self.label_nome.move(20,22)
        self.label_nome.setStyleSheet('QLabel {font-size:15px}')
        self.label_nome.resize(400, 25)

        self.label_endereco = QLabel(self)
        self.label_endereco.setText("Endereço completo:")
        self.label_endereco.move(20, 52)
        self.label_endereco.setStyleSheet('QLabel {font-size:15px}')
        self.label_endereco.resize(400, 25)

        self.label_altura = QLabel(self)
        self.label_altura.setText("Altura (cm):")
        self.label_altura.move(20, 82)
        self.label_altura.setStyleSheet('QLabel {font-size:15px}')
        self.label_altura.resize(400, 25)

        self.label_peso = QLabel(self)
        self.label_peso.setText("Peso (kg):")
        self.label_peso.move(20, 112)
        self.label_peso.setStyleSheet('QLabel {font-size:15px}')
        self.label_peso.resize(400, 25)

        self.caixa_texto = QLabel(self)
        self.caixa_texto.setText("______________________________________________________________________________________________\n\nRESULTADO:")
        self.caixa_texto.move(20, 135)
        self.caixa_texto.setStyleSheet('QLabel {font-size:15px}')
        self.caixa_texto.resize(535, 65)

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def btRein_click(self):
        self.caixa_nome.clear()
        self.caixa_endereco.clear()
        self.caixa_altura.clear()
        self.caixa_peso.clear()

    def btSair_click(self):
        self.close()

    def Mostra_resultado(self):
        nome = self.caixa_nome.text()
        endereco = self.caixa_endereco.text()
        altura = self.caixa_altura.text()
        peso = self.caixa_peso.text()

        imc = self.calcular_imc(peso, altura)

        if imc is not None:
            resultado_texto = (
                "______________________________________________________________________________________________\n\nRESULTADO:\n"
                f" - PACIENTE: {nome}\n - ENDEREÇO: {endereco}\n - PESO: {peso} kg\n - ALTURA: {altura} cm\n"
                f" - IMC: {imc:.2f}\n______________________________________________________________________________________________"
            )
        else:
            resultado_texto = "Entrada inválida. Por favor, insira valores numéricos para peso e altura."

        self.caixa_texto.setText(resultado_texto)
        self.caixa_texto.move(20, 134)
        self.caixa_texto.setStyleSheet('QLabel {font-size:15px}')
        self.caixa_texto.resize(535, 175)

    def calcular_imc(self, peso, altura):
        try:
            peso = float(peso)
            altura = float(altura) / 100
            imc = peso / (altura ** 2)
            return imc
        except ValueError:
                return None  # VERIFICAÇÃO CASO HAJA ALGUMA ENTRADA INVÁLIDA

aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())
