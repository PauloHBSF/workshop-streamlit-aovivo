# Projeto - Formulário utilizando Streamlit

## Introdução

Este projeto foi desenvolvido após o Workshop de "Realtime Dashborads com Streamlit" do professor Luciano Galvão com participação do Kaio, onde aprendemos a criar um Formulário para ingestão de dados para um banco Postgree na Nuvem e um Dashboard que os consome.

## How to Use

1. Clone o Respositório
```
git clone https://github.com/PauloHBSF/workshop-streamlit-aovivo
cd workshop-streamlit-aovivo
```

2. Faça o Setup do Pyenv
*Documentação para Instalação do Poetry*
*https://github.com/pyenv/pyenv?tab=readme-ov-file#installation*
-
```
pyenv install 3.12.1
pyenv local 3.12.1
```

3. Instale as dependências do Projeto - Utilize preferencialmente o Poetry
*Documentação para Instalação do Poetry*
*https://python-poetry.org/docs/* 
```
poetry install
```

4. Rode o Projeto
```
poetry shell
python src/dashboard.py
```