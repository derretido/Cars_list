# 🚗 Car Management System

Este projeto é um sistema de gerenciamento de carros que combina **FastAPI** no backend e **Streamlit** no frontend.  
Ele permite realizar operações de **CRUD** (criar, listar, atualizar e deletar carros), além de exibir imagens locais associadas a cada modelo.

---

## 📚 Bibliotecas utilizadas

- **FastAPI**  
  Framework moderno e rápido para construção de APIs em Python.  
  Utilizado para definir rotas (`GET`, `POST`, `PUT`, `DELETE`) e validar dados com **Pydantic**.

- **Pydantic (BaseModel)**  
  Responsável pela validação automática dos dados recebidos pela API.  
  Garante que os campos tenham os tipos corretos (ex: `id: int`, `year: int`).

- **Streamlit**  
  Biblioteca para criação de interfaces web de forma simples e interativa.  
  Usada para construir formulários (`st.text_input`, `st.number_input`, `st.button`) e exibir resultados (`st.subheader`, `st.write`, `st.image`).  
  Também permite estilização com HTML/CSS via `st.markdown(..., unsafe_allow_html=True)`.

- **Requests**  
  Biblioteca para enviar requisições HTTP do frontend para o backend.  
  Usada para consumir a API (`requests.get`, `requests.post`, `requests.put`, `requests.delete`).

- **OS (módulo padrão do Python)**  
  Utilizado para verificar se os arquivos de imagem realmente existem (`os.path.exists(...)`), evitando erros quando o caminho não é válido.

---

## ⚙️ Funcionalidades principais

- **Listagem de carros**: mostra todos os carros cadastrados, com modelo, ano, potência e imagem.  
- **Adição de carros**: formulário para inserir novos carros, gerando automaticamente o caminho da imagem.  
- **Atualização de carros**: permite modificar os dados de um carro existente.  
- **Remoção de carros**: exclui carros pelo ID.  
- **Exibição de imagens locais**: cada carro pode ter uma imagem associada, exibida no frontend.

---

# 🚗 Car Management System

This project is a **car management system** that integrates **FastAPI** as the backend and **Streamlit** as the frontend.  
It allows full **CRUD operations** (Create, Read, Update, Delete) and displays local images associated with each car model.

---

## 📚 Libraries Used

- **FastAPI**  
  Modern and fast framework for building APIs in Python.  
  Used to define routes (`GET`, `POST`, `PUT`, `DELETE`) and validate data with **Pydantic**.

- **Pydantic (BaseModel)**  
  Provides automatic data validation.  
  Ensures fields have the correct types (e.g., `id: int`, `year: int`).

- **Streamlit**  
  Library for creating interactive web interfaces.  
  Used to build forms (`st.text_input`, `st.number_input`, `st.button`) and display results (`st.subheader`, `st.write`, `st.image`).  
  Supports custom styling with HTML/CSS via `st.markdown(..., unsafe_allow_html=True)`.

- **Requests**  
  Used to send HTTP requests from the frontend to the backend.  
  Handles API consumption (`requests.get`, `requests.post`, `requests.put`, `requests.delete`).

- **OS (Python standard library)**  
  Used to check if image files exist (`os.path.exists(...)`), preventing errors when paths are invalid.

---

## ⚙️ Features

- **Car listing**: Displays all registered cars with model, year, power, and image.  
- **Add new cars**: Form to insert new cars, automatically generating the image path.  
- **Update cars**: Modify existing car details.  
- **Delete cars**: Remove cars by ID.  
- **Local image display**: Each car can have an associated image stored in the `images/` folder.

---

## 📂 Project Structure

