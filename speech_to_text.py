import whisper

# Load Whisper model
model = whisper.load_model("base")

# Load your audio file (replace with your own path)
audio_path = "sample_audio.mp3"

# Transcribe the audio
print("Transcribing audio... please wait.")
result = model.transcribe(audio_path)

# Print the text
print("\n--- TRANSCRIBED TEXT ---\n")
print(result["text"])

# Save the result into a text file
with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
print("\n✅ Transcription saved to 'transcript.txt'")
