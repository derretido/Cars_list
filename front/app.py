import os
import streamlit as st
import requests

API_url = "http://127.0.0.1:8000/cars"

#CSS para estilizar a aplicação
st.markdown( 
    """
    <style>
    .titulo {
        color: #d00000;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }
    .car-card {
        background: white;
        padding: 15px;
        margin: 10px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='title'>Car Management System</div>", unsafe_allow_html=True)

images ={
    "Porsche 911 Carrera": "images/Porsche_911_Carrera.png",
    "Porsche Cayenne": "images/Porsche_Cayenne.png",
    "Porsche Panamera": "images/Porsche_Panamera.png",
    "Porsche Macan": "images/Porsche_Macan.png",
    "Porsche Taycan": "images/Porsche_Taycan.png",
    "Porsche 911 Gt3 Rs": "images/Porsche_911_Gt3_Rs.png",
}

#Listagem de carros
st.header("Car List")
response = requests.get(API_url)
carros = response.json()
for carro in carros:
    st.markdown("<div class='car-card'>", unsafe_allow_html=True)
    st.subheader(carro["model"])
    st.write(f"Ano: {carro['year']} | Potência: {carro['power']}")

    if carro.get("image") and os.path.exists(carro["image"]):
        st.image(carro["image"], width=300)
    elif carro["model"] in images and os.path.exists(images[carro["model"]]):
        st.image(images[carro["model"]], width=300)

# adicionar um novo carro
st.header("Add a New Car")
id = st.number_input("ID", min_value=1)
model = st.text_input("Model")
year = st.number_input("Year", min_value=1900, step=1)
power = st.text_input("Power")
if st.button("Add Car"):
    new = {
        "id": id,
        "model": model,
        "year": year,
        "power": power,
        "image": f"images/{model.replace(' ', '_').lower()}.png"
    }
    r = requests.post(API_url, json=new)
    if r.status_code == 200:
        st.success("Car added successfully")
    else:
        st.error("Error adding car")

#Atualização 
st.header("Update a Car")
id_update = st.number_input("ID of the car to update", min_value=1)
model_update = st.text_input("New Model")
year_update = st.number_input("New Year", min_value=1900, step=1)
power_update = st.text_input("New Power")
if st.button("Update Car"):
    updated_car = {
        "id": id_update,
        "model": model_update,
        "year": year_update,
        "power": power_update
    }
    r = requests.put(f"{API_url}/{id_update}", json=updated_car)
    if r.status_code == 200:
        st.success("Car updated successfully")
    else:
        st.error("Error updating car")

#Deletar um carro
st.header("Delete a Car")
id_delete = st.number_input("ID of the car to delete", min_value=1)
if st.button("Delete Car"):
    r = requests.delete(f"{API_url}/{id_delete}")
    if r.status_code == 200:
        st.success("Car deleted successfully")
    else:
        st.error("Error deleting car")