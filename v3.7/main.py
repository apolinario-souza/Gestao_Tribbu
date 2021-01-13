from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from specialbuttons import ImageButton, LabelButton, ImageButtonSelectable
from myfirebase import MyFirebase
import requests
import json
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
import pandas as pd
import numpy as np
from kivy.uix.boxlayout import BoxLayout

import easygui
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

import matplotlib.pyplot as plt



class LoginScreen(Screen):
	pass
   

class HomeScreen(Screen):
	pass

class AdduserScreen(Screen):
	pass

class AddyearScreen(Screen):
	pass


class ImageBotton(ButtonBehavior, Image):
	pass	

class CostsFixedScreen(Screen):
	pass

class CostsVariableScreen(Screen):
	pass
	
class IncomeScreen(Screen):
	pass


class AccScreen(Screen):
	pass
	
	
class Tarefa(BoxLayout):
	def __init__(self, text1='',text2='',text3='',text4='',text5='',text6='', text7='',**kwargs):
			super().__init__(**kwargs)
			self.ids.label1.text = text1
			self.ids.label2.text = text2
			self.ids.label3.text = text3
			self.ids.label4.text = text4
			self.ids.label5.text = text5
			self.ids.label6.text = text6
			self.ids.label7.text = text7
			
class StatisticScreen(Screen):
	pass

	
	



GUI = Builder.load_file("main.kv")


class MainApp(App):
	my_user = ""
	my_year = ""
	my_month = ""
	my_cont = False
	my_graphic = ''
	
	
	
	
	def build(self):
		self.my_firebase = MyFirebase()		
		return GUI
	
	

		
	
	def change_screen (self, screen_name):
		screen_manager = self.root.ids['screen_manager']
		screen_manager.current = screen_name	
	
	def add_user(self):
		
		user = self.root.ids["adduser_screen"].ids["add_user_input"]
		senha = self.root.ids["adduser_screen"].ids["add_id_input"]
		
		self.my_user = user.text, senha.text
		patch_data = '{"%s":"%s"}' %self.my_user 
		patch_request = requests.patch('https://tribus-e2a87-default-rtdb.firebaseio.com/users/name.json', data = patch_data)
		
		self.root.ids["adduser_screen"].ids["add_user_input"].text = ''
		self.root.ids["adduser_screen"].ids["add_id_input"].text = ''
	def login (self):
		result = requests.get("https://tribus-e2a87-default-rtdb.firebaseio.com/users/name.json")
		data = json.loads(result.content.decode())
		
		
		
		user = self.root.ids["login_screen"].ids["usuario"].text
		senha = self.root.ids["login_screen"].ids["senha"].text
		
		check_user = str(user) in data
		
		
		if check_user == True:
		
			if data[str(user)] == str(senha):
				self.change_screen("home_screen")
				
			else:
				self.root.ids["login_screen"].ids["login_message"].text = "Senha invalida" 
			
			
		else:
			self.root.ids["login_screen"].ids["login_message"].text = "Usuário invalido"
	
	
	def add_year(self, year):
		
		self.my_year = self.root.ids["addyear_screen"].ids["add_year_input"]
		self.my_firebase = MyFirebase()
		self.my_firebase.add_data(self.my_year.text)
	
	
############################ Fixed costs ###################################
	
	
	def add_items_fixed (self, item1,item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12):
	
		
		#Selec moths
		self.my_month = self.root.ids["costsfixed_screen"].ids["btn_months"]
		
		#Selec year
		self.my_year=self.root.ids["costsfixed_screen"].ids["btn_years"]									
		
		
		
		f = item1,item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12
		
				
		#Add items
		for i in range (len(f)):
			x = f[i].replace('add_', '') 		
			x = x.replace('_input', '')
			
			v = self.root.ids["costsfixed_screen"].ids[f[i]]
					
			b =  x, v.text			
				
			items = '{"%s": %s}' %b
					
			patch_request = requests.patch('https://tribus-e2a87-default-rtdb.firebaseio.com/ano/'+ self.my_year.text + '/mes/'+ self.my_month.text +'.json', data = items )
		
		#clear items
		
		for i in range (len(f)):
			x = f[i].replace('add_', '') 		
			x = x.replace('_input', '')
			
			v = self.root.ids["costsfixed_screen"].ids[f[i]].text = ''
										
	
	def get_items_fixed (self,  item1,item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12):
		
			
		#Selecionar o mês
		self.my_month = self.root.ids["costsfixed_screen"].ids["btn_months"]
		
		#Selecionar o ano
		self.my_year=self.root.ids["costsfixed_screen"].ids["btn_years"]									
		
		result = requests.get("https://tribus-e2a87-default-rtdb.firebaseio.com/ano/"+ self.my_year.text + '/mes/'+ self.my_month.text +'.json')
			
		data = json.loads(result.content.decode())
		
		f = item1,item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12
		
		for i in range (len(f)):
			x = f[i].replace('add_', '') 		
			x = x.replace('_input', '')
			
			v = self.root.ids["costsfixed_screen"].ids[f[i]]
			
			v.text = str (data[x])
			
		
############################ variable costs ###################################
	
	
	def add_items_variable (self, item1,item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14):
	
		
		#Selec moths
		self.my_month = self.root.ids["costsvariable_screen"].ids["btn_months"]
		
		#Selec year
		self.my_year=self.root.ids["costsvariable_screen"].ids["btn_years"]									
		
		
		
		f = item1,item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14
		
				
		#Add items
		for i in range (len(f)):
			x = f[i].replace('add_', '') 		
			x = x.replace('_input', '')
			
			v = self.root.ids["costsvariable_screen"].ids[f[i]]
					
			b =  x, v.text			
				
			items = '{"%s": %s}' %b
					
			patch_request = requests.patch('https://tribus-e2a87-default-rtdb.firebaseio.com/ano/'+ self.my_year.text + '/mes/'+ self.my_month.text +'.json', data = items )
		
		#clear items
		
		for i in range (len(f)):
			x = f[i].replace('add_', '') 		
			x = x.replace('_input', '')
			
			v = self.root.ids["costsvariable_screen"].ids[f[i]].text = ''
										
	
	def get_items_variable (self,  item1,item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14):
		
			
		#Selecionar o mês
		self.my_month = self.root.ids["costsvariable_screen"].ids["btn_months"]
		
		#Selecionar o ano
		self.my_year=self.root.ids["costsvariable_screen"].ids["btn_years"]									
		
		result = requests.get("https://tribus-e2a87-default-rtdb.firebaseio.com/ano/"+ self.my_year.text + '/mes/'+ self.my_month.text +'.json')
			
		data = json.loads(result.content.decode())
		
		f = item1,item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14
		
		for i in range (len(f)):
			x = f[i].replace('add_', '') 		
			x = x.replace('_input', '')
			
			v = self.root.ids["costsvariable_screen"].ids[f[i]]
			
			v.text = str (data[x])
			

############################ Income ###################################
	
	
	def add_items_income (self, item1,item2, item3, item4, item5, item6, item7, item8):
	
		
		#Selec moths
		self.my_month = self.root.ids["income_screen"].ids["btn_months"]
		
		#Selec year
		self.my_year=self.root.ids["income_screen"].ids["btn_years"]									
		
		
		
		f = item1,item2, item3, item4, item5, item6, item7, item8
		
				
		#Add items
		for i in range (len(f)):
			x = f[i].replace('add_', '') 		
			x = x.replace('_input', '')
			
			v = self.root.ids["income_screen"].ids[f[i]]
					
			b =  x, v.text			
				
			items = '{"%s": %s}' %b
					
			patch_request = requests.patch('https://tribus-e2a87-default-rtdb.firebaseio.com/ano/'+ self.my_year.text + '/mes/'+ self.my_month.text +'.json', data = items )
		
		#clear items
		
		for i in range (len(f)):
			x = f[i].replace('add_', '') 		
			x = x.replace('_input', '')
			
			v = self.root.ids["income_screen"].ids[f[i]].text = ''
										
	
	def get_items_income (self,  item1,item2, item3, item4, item5, item6, item7, item8):
		
			
		#Selecionar o mês
		self.my_month = self.root.ids["income_screen"].ids["btn_months"]
		
		#Selecionar o ano
		self.my_year=self.root.ids["income_screen"].ids["btn_years"]									
		
		result = requests.get("https://tribus-e2a87-default-rtdb.firebaseio.com/ano/"+ self.my_year.text + '/mes/'+ self.my_month.text +'.json')
			
		data = json.loads(result.content.decode())
		
		f = item1,item2, item3, item4, item5, item6, item7, item8
		
		for i in range (len(f)):
			x = f[i].replace('add_', '') 		
			x = x.replace('_input', '')
			
			v = self.root.ids["income_screen"].ids[f[i]]
			
			v.text = str (data[x])


############### Accompaniment ################
										
	def addWidget(self):
	
		#Selecionar o mês
		self.my_month = self.root.ids["acc_screen"].ids["btn_months"]
		
		#Selecionar o ano
		self.my_year=self.root.ids["acc_screen"].ids["btn_years"]	
		
		
		
		texto1 = self.root.ids["acc_screen"].ids['btn_descricao'].text
		texto2 = self.root.ids["acc_screen"].ids['texto2'].text
		texto3 = self.root.ids["acc_screen"].ids['texto3'].text
		texto4 = self.root.ids["acc_screen"].ids['texto4'].text
		texto5= self.root.ids["acc_screen"].ids['texto5'].text
		texto6 = self.root.ids["acc_screen"].ids['texto6'].text
		texto7 = self.root.ids["acc_screen"].ids['texto7'].text
		
		self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text1=texto1))
		self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text2=texto2))
		self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text3=texto3))
		self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text4=texto4))
		self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text5=texto5))
		self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text6=texto6))
		self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text7=texto7))
		
		textos = texto1+';'+texto2+';'+texto3+';'+texto4+';'+texto5+';'+texto6+";"+texto7+";"			
		
		b = str(textos), 0
		
		items = '{"%s": %i}' %b
		
			
		data = items
		
		patch_request = requests.patch('https://tribus-e2a87-default-rtdb.firebaseio.com/ano2/'+ self.my_year.text + '/mes/'+ self.my_month.text +'.json', data = items )
		
		
		self.root.ids["acc_screen"].ids['texto2'].text = ''
		self.root.ids["acc_screen"].ids['texto3'].text = ''
		self.root.ids["acc_screen"].ids['texto4'].text = ''
		self.root.ids["acc_screen"].ids['texto5'].text = ''
		self.root.ids["acc_screen"].ids['texto6'].text = ''
		self.root.ids["acc_screen"].ids['texto7'].text = ''
		
		print('ok')
		
	def get_acc (self):
		
		#Selecionar o mês
		self.my_month = self.root.ids["acc_screen"].ids["btn_months"]
		
		#Selecionar o ano
		self.my_year=self.root.ids["acc_screen"].ids["btn_years"]
		
		
		
		result = requests.get("https://tribus-e2a87-default-rtdb.firebaseio.com/ano2/"+ self.my_year.text + '/mes/'+ self.my_month.text +'.json')
			
		data = json.loads(result.content.decode())
		c = str(data)
		b = c.replace("{'", '').replace("': 0", '').replace("'", '')
		
		indices = []
		
		
		
		for i in range (len(b)):
			
			if b[i] == ';':
				indices.append(i)				
			
		
		variable = []
		variables = []
		for i in range (len(indices)-1):
			
			if i == 0:
				variables.append(b[0:indices[0]])
				
				
			variable.append(b[indices[i]:indices[i+1]])
			variables.append(variable[i].replace(';', '').replace(', ', '')) 
				
		
		for i in range (int(len(variables)/7)):	
			if i == 0:
			
				self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text1=variables[0]))
				self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text2=variables[1]))
				self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text3=variables[2]))
				self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text4=variables[3]))
				self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text5=variables[4]))
				self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text6=variables[5]))
				self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text7=variables[6]))
			if i > 0:
				self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text1=variables[i*6]))
				self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text2=variables[i*6+1]))
				self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text3=variables[i*6+2]))
				self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text4=variables[i*6+3]))
				self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text5=variables[i*6+4]))
				self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text6=variables[i*6+5]))
				self.root.ids["acc_screen"].ids["box1"].add_widget(Tarefa(text7=variables[i*6+6]))
			
	
	def make_graphic(self):
		
		if self.my_cont == False:
		
			self.my_year=self.root.ids["statistic_screen"].ids["btn_years"]
			
			
			nome_meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
			
			nomes_despesa_fixa = ['agua','energia', 'aluguel', 'internet', 'inss', 'fgts','simples', 'honorarios', 'salario', 'folgistas', 'software', 'banco']
			
			nomes_despesa_variavel =['royalties', 'fundo', 'acai', 'frutas', 'paletas', 'refeicoes', 'opcionais', 'sorvete', 'limpeza', 'outras', 'manutencao', 'extras', 'delivery', 'subsidios']
		 
			nomes_faturamento = ['quantdelivery1', 'quantdelivery2', 'quantdelivery3', 'quantdelivery4', 'faturamento1', 'faturamento2', 'faturamento3','faturamento4']
			
			despesa_fixa_anual = []
			despesa_variavel_anual = [] 
			faturamento_anual = []
			
			### means###
			for k in range(len(nome_meses)):
				
							
				result = requests.get("https://tribus-e2a87-default-rtdb.firebaseio.com/ano/"+ self.my_year.text + '/mes/'+ nome_meses[k] +'.json')
					
				data = json.loads(result.content.decode())
				
				despesa_fixa = []
				despesa_variavel = []
				faturamento = []
				for i in range (len(nomes_despesa_fixa)):
					despesa_fixa.append(data[nomes_despesa_fixa[i]])
				for i in	 range (len(nomes_despesa_variavel)):
					despesa_variavel.append(data[nomes_despesa_variavel[i]])
				for i in range (len(nomes_faturamento)):
					faturamento.append(data[nomes_faturamento[i]])
					
				
				despesa_fixa_anual.append(np.mean(despesa_fixa))
				despesa_variavel_anual.append(np.mean(despesa_variavel))
				faturamento_anual.append(np.mean(faturamento))		
						
			faturamento_anual = np.array(faturamento_anual)
			despesa_fixa_anual = np.array(despesa_fixa_anual)
			despesa_variavel_anual = np.array(despesa_variavel_anual)
			
			despesas = despesa_fixa_anual + despesa_variavel_anual
			balanco = faturamento_anual - despesas
			
			
			### Graphics
			fig, ax = plt.subplots()
			idx = np.asarray([i for i in range(len(nome_meses))])
			width = 0.2
			
			
			ax.bar(idx, [despesa_fixa_anual [ii] for ii in range(len(despesa_fixa_anual))], width=width, edgecolor = 'k')
			ax.bar(idx+width, [despesa_variavel_anual [ii] for ii in range (len(despesa_variavel_anual))], width=width, edgecolor = 'k')
			ax.bar(idx+(width*2), [faturamento_anual [ii] for ii in range(len(faturamento_anual))], width=width,edgecolor = 'k')
			ax.bar(idx+(width*3), [balanco [ii] for ii in range (len(balanco))], width=width,edgecolor = 'k')
			
			
			ax.set_xticks(idx)
			ax.set_xticklabels(nome_meses, rotation=0)
			ax.legend(['Despesas fixas', 'Despesas variável', 'Faturamento', 'Balanço'])
			ax.set_ylabel('# of patients')

			fig.tight_layout()		
			plt.ylabel('R$')
			
			
			
			x = self.root.ids["statistic_screen"].ids["box1"]		
			
			self.my_graphic = FigureCanvasKivyAgg(plt.gcf())
			
			x.add_widget(self.my_graphic)
			
			
			
			
			for i in range(len(faturamento_anual)):
				faturamento_anual [i] = format(faturamento_anual [i], '.2f')
				self.root.ids["statistic_screen"].ids["faturamento"+str(i+1)].text = str(faturamento_anual [i])
				
				despesa_variavel_anual [i] = format(despesa_variavel_anual [i], '.2f')
				self.root.ids["statistic_screen"].ids["Desp_Var"+str(i+1)].text = str(despesa_variavel_anual [i])
				
				despesa_fixa_anual [i] = format(despesa_fixa_anual [i], '.2f')
				self.root.ids["statistic_screen"].ids["Desp_Fix"+str(i+1)].text = str(despesa_fixa_anual [i])
				
				balanco [i] = format(balanco [i], '.2f')
				self.root.ids["statistic_screen"].ids["balanco"+str(i+1)].text = str(balanco [i])
				
				
			
			b = np.sum(faturamento_anual)
			b = format(b, '.2f')
			self.root.ids["statistic_screen"].ids["faturamento13"].text = str(b)
			
			b = np.sum(despesa_variavel_anual)
			b = format(b, '.2f')	
			self.root.ids["statistic_screen"].ids["Desp_Var13"].text = str(b)
			
			b = np.sum(despesa_fixa_anual)
			b = format(b, '.2f')		
			self.root.ids["statistic_screen"].ids["Desp_Fix13"].text = str(b)
			
			b = np.sum(balanco)
			b = format(b, '.2f')
			self.root.ids["statistic_screen"].ids["balanco13"].text = str(b)
			
			self.my_cont = True
		else:
			easygui.msgbox("Retorne ao menu inicial!", title="")
			
			
		
		
		
				
	def clear (self):
		
		if self.my_cont == True:
			x = self.root.ids["statistic_screen"].ids["box1"]	
				
			x.remove_widget(self.my_graphic)
		
		self.my_cont = False					
		
	
MainApp().run()
