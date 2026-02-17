
## 🌐 Languages
- [English](README.md)
- [Português](README.pt.md)

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