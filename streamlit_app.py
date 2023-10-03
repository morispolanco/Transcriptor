import streamlit as st
import whisper

# Función para transcribir notas de voz
def transcribir_notas_de_voz(api_key):
    # Cargar el archivo de audio
    audio_file = st.file_uploader("Cargar archivo de audio", type=["wav", "mp3"])

    if audio_file is not None:
        # Crear un objeto de transcripción
        transcriptor = whisper.Transcriber(api_key=api_key, language='es')

        # Transcribir el audio
        transcripcion = transcriptor.transcribe(audio_file)

        # Mostrar la transcripción
        st.write("Transcripción:")
        st.write(transcripcion)

# Título de la aplicación
st.title("Transcripción de Notas de Voz en Español")

# Solicitar la clave API al usuario
api_key = st.text_input("Introduce tu clave API de OpenAI")

# Transcribir notas de voz si se proporciona una clave API
if api_key:
    transcribir_notas_de_voz(api_key)
