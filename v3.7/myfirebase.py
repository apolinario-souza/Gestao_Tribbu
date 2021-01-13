
import pyrebase
import requests
import json
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
import certifi


class MyFirebase():
	wak = "AIzaSyBCG5bgSfij-1bn1E018zNQJ73ZpXxzvfo"  # Web Api Key
	config = {
	    "apiKey": "AIzaSyBCG5bgSfij-1bn1E018zNQJ73ZpXxzvfo",
	    "authDomain": "tribus-e2a87.firebaseapp.com",
	    "databaseURL": "https://tribus-e2a87-default-rtdb.firebaseio.com",
	    "projectId": "tribus-e2a87",
	    "storageBucket": "tribus-e2a87.appspot.com",
	    "messagingSenderId": "979651852089",
	    "appId": "1:979651852089:web:cfd2d9ceff2daa73839ae8",
	    "measurementId": "G-1YQDNH2D8C"
	}
	  
	firebase = pyrebase.initialize_app(config);
	  
	dados = firebase.database()
	meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
	itens = {'agua': 0,'energia': 0, 'aluguel': 0, 'internet': 0, 'inss': 0, 'fgts': 0,
	 'simples': 0, 'honorarios': 0, 'salario': 0, 'folgistas': 0, 'software': 0, 'banco': 0, 
	 
	 'royalties':0, 'fundo':0, 'acai':0, 'frutas':0, 'paletas':0, 'refeicoes': 0, 'opcionais':0, 'sorvete':0, 'limpeza':0, 'outras':0, 'manutencao':0, 'extras':0, 'delivery':0, 'subsidios':0,
	 
	 'quantdelivery1':0, 'quantdelivery2':0, 'quantdelivery3':0, 'quantdelivery4':0, 'faturamento1':0, 'faturamento2':0, 'faturamento3':0,'faturamento4':0}
	
	
	check_request = requests.get('https://tribus-e2a87-default-rtdb.firebaseio.com/itens.json')	
	data = json.loads(check_request.content.decode())
	
		
	def add_data(self, ano):
		
		self.ano = ano
		ano_ref = self.dados.child('ano')
		mes_ref = ano_ref.child(ano)
		users_ref = mes_ref.child('mes')



		users_ref.set({
		self.meses [0]: self.itens, self.meses [1]: self.itens, self.meses [2]: self.itens, self.meses [3]: self.itens,self.meses [4]: self.itens,self.meses [5]: self.itens,self.meses [6]: self.itens,self.meses [7]: self.itens,self.meses [8]: self.itens,self.meses [9]: self.itens,self.meses [10]: self.itens,self.meses [11]: self.itens
		})
		
		
		ano_ref2 = self.dados.child('ano2')
		mes_ref2 = ano_ref.child(ano)
		users_ref2 = mes_ref.child('mes')



		users_ref2.set({
		self.meses [0]: 'empty', self.meses [1]: 'empty', self.meses [2]: 'empty', self.meses [3]: 'empty',self.meses [4]: 'empty',self.meses [5]: 'empty',self.meses [6]:'empty',self.meses [7]: 'empty',self.meses [8]: 'empty',self.meses [9]: 'empty',self.meses [10]: 'empty',self.meses [11]: 'empty'})



