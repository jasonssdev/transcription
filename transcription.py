from pydub import AudioSegment
import speech_recognition as sr
import os

# Path to the local audio file
audio_file_path = './audio/audio.mp3'

# Check if the file exists
if not os.path.isfile(audio_file_path):
    raise FileNotFoundError(f"The file {audio_file_path} does not exist.")

# Convert MP3 to WAV
sound = AudioSegment.from_mp3(audio_file_path)
wav_file_path = audio_file_path.replace('.mp3', '.wav')
sound.export(wav_file_path, format="wav")

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Convert audio to text
with sr.AudioFile(wav_file_path) as source:
    audio = recognizer.record(source)
    text = recognizer.recognize_google(audio, language="en-US")

# Print the transcribed text
print("Transcribed text:")
print(text)

# Save the transcribed text to a new .txt file
transcription_file_path = audio_file_path.replace('.mp3', '.txt')
with open(transcription_file_path, 'w') as file:
    file.write(text)

print(f"Transcription saved to {transcription_file_path}")

