import streamlit as st
import whisper
import sounddevice as sd
import soundfile as sf

# Función para transcribir notas de voz
def transcribir_notas_de_voz():
    # Botón para iniciar la grabación
    if st.button("Iniciar Grabación"):
        # Configurar parámetros de grabación
        duration = 10  # Duración de la grabación en segundos
        sample_rate = 44100  # Tasa de muestreo en Hz
        channels = 1  # Número de canales de audio

        # Grabar audio
        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
        sd.wait()  # Esperar a que termine la grabación

        # Guardar audio en archivo temporal
        audio_file = "temp.wav"
        sf.write(audio_file, audio, sample_rate)

        # Crear un objeto de transcripción
        transcriptor = whisper.Transcriber(language='es')

        # Transcribir el audio
        transcripcion = transcriptor.transcribe(audio_file)

        # Mostrar la transcripción
        st.write("Transcripción:")
        st.write(transcripcion)

# Título de la aplicación
st.title("Transcripción de Notas de Voz en Español")

# Transcribir notas de voz
transcribir_notas_de_voz()
