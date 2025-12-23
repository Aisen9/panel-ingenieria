# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 17:25:39 2025

@author: Usuario
"""

import streamlit as st

# 1. Título y Configuración del Panel
st.set_page_config(page_title="Herramientas Isai", page_icon="⚗️")
st.title("⚗️ Panel de Ingeniería Química")
st.write("Bienvenido al panel interactivo. Elige una herramienta abajo.")

# 2. Barra lateral (Sidebar) para navegar
opcion = st.sidebar.selectbox(
    "¿Qué quieres hacer hoy?",
    ("Convertir Temperatura", "Calculadora de Reactores", "Juego Simple")
)

# --- OPCIÓN 1: Convertidor ---
if opcion == "Convertir Temperatura":
    st.header("🌡️ Conversor de Unidades")
    
    col1, col2 = st.columns(2) # Creamos dos columnas
    with col1:
        celsius = st.number_input("Grados Celsius:", value=25.0)
    
    kelvin = celsius + 273.15
    fahrenheit = (celsius * 9/5) + 32
    
    # Mostrar resultados en tarjetas bonitas
    st.success(f"Kelvin: {kelvin} K")
    st.info(f"Fahrenheit: {fahrenheit} °F")

# --- OPCIÓN 2: Calculadora (Ejemplo Formal) ---
elif opcion == "Calculadora de Reactores":
    st.header("🏭 Tiempo de Residencia (tau)")
    volumen = st.slider("Volumen del Reactor (L)", 10, 1000, 500)
    caudal = st.number_input("Caudal (L/min)", value=50.0)
    
    if st.button("Calcular Tau"):
        if caudal > 0:
            tau = volumen / caudal
            st.metric(label="Tiempo de Residencia", value=f"{tau} min")
        else:
            st.error("El caudal debe ser mayor a 0")

# --- OPCIÓN 3: El Juego (Algo divertido) ---
elif opcion == "Juego Simple":
    st.header("🎲 Tira el dado")
    if st.button("Lanzar"):
        import random
        dado = random.randint(1, 6)
        if dado == 6:
            st.balloons() # ¡Efecto especial de globos!
            st.write(f"¡Sacaste un {dado}! ¡Ganaste!")
        else:
            st.write(f"Sacaste un {dado}. Intenta de nuevo.")
# --- Tienes que importar esto al principio del archivo junto con streamlit
import urllib.parse 

# ... (tu código anterior) ...

# --- NUEVA SECCIÓN: Automatización de WhatsApp ---
if opcion == "Respuestas Rápidas":
    st.header("🚀 Panel de Comandos de WhatsApp")
    st.write("Selecciona una respuesta para enviar:")

    # Definimos el número destino (o déjalo vacío para elegir contacto al abrir)
    # Si quieres que se abra para elegir contacto, no pongas número.
    numero = ""  # Ej: "51999999999"
    
    # Botón 1: Modo Estudio (Para cuando no quieres que te molesten)
    msg_estudio = "Estoy estudiando para Ingeniería Química ⚗️, te hablo luego."
    # Codificamos el texto para que funcione en internet (cambia espacios por %20, etc.)
    msg_estudio_url = urllib.parse.quote(msg_estudio)
    link_estudio = f"https://wa.me/{numero}?text={msg_estudio_url}"
    
    st.link_button("🚫 Modo Estudio", link_estudio)

    # Botón 2: Mandar Ubicación (Simulada o texto)
    msg_casa = "Ya estoy yendo a la casa. Llego en 20 min."
    msg_casa_url = urllib.parse.quote(msg_casa)
    link_casa = f"https://wa.me/{numero}?text={msg_casa_url}"
    
    st.link_button("🏠 Yendo a casa", link_casa)
    
    # Botón 3: Pedir Apuntes
    msg_apuntes = "¿Alguien tiene los apuntes de Termodinámica de hoy?"
    msg_apuntes_url = urllib.parse.quote(msg_apuntes)
    link_apuntes = f"https://wa.me/{numero}?text={msg_apuntes_url}"
    
    st.link_button("📚 Pedir Apuntes (Grupo)", link_apuntes)