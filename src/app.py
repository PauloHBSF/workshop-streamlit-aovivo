import streamlit as st
import pandas as pd
import numpy as np

def printa_dados(dados):
    print(dados)

estados = ["SP", "RJ", "TO"]
cidades = {
    "SP": ["Dois Córregos", "Jaú", "Sorocaba"],
    "RJ": ["Cachoeiras de Macacu", "Rio de Janeiro"],
    "TO": ["Palmas", "Paranã"]
}


# Configurando a Página
st.set_page_config(
    page_title="Formulário de Acionamentos",
    page_icon="🚚",
    layout="wide"   
)


# Adicionando um Título
st.title("Acionamento de Cargas")

# Cria as duas colunas para separar o Conteudo
col1, col2 = st.columns(2)


with col1:
    
    with st.form("Empresas", clear_on_submit=True):
        st.subheader("Adicionar Locais")
        tipo_local = st.radio("Escolha se é um Local de Coleta ou Entrega", options=["Coleta", "Entrega"], horizontal=True, label_visibility="hidden")
        
        nome_empresa = st.text_input("Nome da Empresa",
                                     label_visibility="hidden",
                                     placeholder="Nome da Empresa"
                                     )
        
        col1_f1_a1, col1_f1_a2 = st.columns([1, 5])
        with col1_f1_a1:
            uf_empresa = st.selectbox("Escolha a UF", estados) 
            st.write(uf_empresa)
    
        with col1_f1_a2:
            cidade_empresa = st.selectbox("Escolha a Cidade", cidades[uf_empresa])
        
        col1_f1_a1_r2, col1_f1_a2_r2, col1_f1_a3_r2 = st.columns([3, 2, 2])
        with col1_f1_a1_r2:
            data_entrega = st.date_input("Data de Entrega")
        with col1_f1_a2_r2:
            hora_chegada = st.time_input("Hora Chegada")
        with col1_f1_a3_r2:
            hora_saida = st.time_input("Hora Saída")
        
        # SUBMIT BUTTON
        dados_localidade = st.form_submit_button("Adicionar Local")
            

        
        

    with st.form("Características da Carga"):
        
        col1_f2_a1, col2_f2_a2 = st.columns([1, 2])
        
        with col1_f2_a1:
            peso = st.text_input("Insira o Peso")
            onue = st.text_input("ONU")
            
        with col2_f2_a2:
            produto = st.text_input("Produto")
            produto = st.text_input("Tipo Veículo")
            
        # SUBMIT BUTTON
        observacao = st.text_area("Observação")
        enviar_acionamento = st.form_submit_button("Enviar Acionamento")
        
with col2:

    with st.container(border=True):
        
        st.write("Teste")