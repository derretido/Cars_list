## 🌐 Languages
- [English](README.md)
- [Português](READMEpt.md)

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

