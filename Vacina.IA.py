import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objects as go

from tensorflow.keras.models import load_model

st.set_page_config(page_title="Vacina.IA", page_icon="icon.png")
status=st.sidebar.radio('',('Home',"Safety Measures"))

if status =="Home":
	st.image("icon.png")
	st.markdown("# Vacina.IA")

	age = st.number_input("Digite sua idade")
	sex = st.selectbox("Sexo", ('Male','Female'))
	symptoms = st.multiselect("Escolha Todas as Condições de Saúde Anteriores",('Nenhuma','Hipertensão', 'Asma', 'Diabetes','Corona', 'Hypothyroidism', 'Hyperlipidemia', 'Chelestrol','Depression', 'Obesity', 'Kidney'))
	vaccine_name = st.selectbox("Selecione a Vacina", ('PFIZER(BIONTECH)','MODERNA', 'BUTANTAN'))
	st.markdown("")

	if st.button('Prevendo Efeito Colateral'):
		model = load_model('MP.h5', compile=False)
		x = []
		x.append(age)

		if sex == "Male":
			x.append(0)
		else:
			x.append(1)

		if vaccine_name == "PFIZER(BIONTECH)":
			x.append(0)
		else:
			x.append(1)

		if symptoms[0] == "None":
			for i in range(10):
				x.append(0)

		else:
			if "Hipertensão" in symptoms:
				x.append(1)
			else:
				x.append(0)

			if "Asma" in symptoms:
				x.append(1)
			else:
				x.append(0)
			if "Diabetes" in symptoms:
				x.append(1)
			else:
				x.append(0)
			if "Corona" in symptoms:
				x.append(1)
			else:
				x.append(0)
			if "Hypothyroidism" in symptoms:
				x.append(1)
			else:
				x.append(0)
			if "Hyperlipidemia" in symptoms:
				x.append(1)
			else:
				x.append(0)
			if "Chelestrol" in symptoms:
				x.append(1)
			else:
				x.append(0)
			if "Depression" in symptoms:
				x.append(1)
			else:
				x.append(0)
			if "Obesity" in symptoms:
				x.append(1)
			else:
				x.append(0)
			if "Kidney" in symptoms:
				x.append(1)
			else:
				x.append(0)

		print(x)
		x = np.array(x)
		x = np.reshape(x, (1,13))
		y = model.predict(x)
		print(y)

		symptoms_label = ['Dor no Corpo', 'Pyrexia', 'Dor de Cabeça', 'Dispneia', 'Fadiga', 'Chills','Dizziness', 'Nausea', 'Asthenia', 'Cough']
		indices = (-y).argsort()[:4]
		values = []
		labels = []
		for count in range(4):
			idx = np.where(indices==count)
			values.append(y[0][idx[1][0]])
			labels.append(symptoms_label[idx[1][0]])

		st.markdown("## Efeitos colaterais prováveis ​​de ocorrer")
		fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
		st.plotly_chart(fig)

		st.markdown("")
		st.markdown("## Probabilidade de cada um dos efeitos colaterais ocorrer")
		fig2 = go.Figure([go.Bar(x=symptoms_label, y=y[0])])
		st.plotly_chart(fig2)


if status == "Safety Measures":
	st.markdown("# Use máscara, fique seguro")
	st.image("icon2.png")

