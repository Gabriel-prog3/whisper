import os
import whisper

# Get filenames in the current directory
filenames = os.listdir()

model = whisper.load_model("medium")

# Print each filename
for filename in filenames:
    try:
        result = model.transcribe(filename)
        print(filename)
        print(result["text"],'\n\n')
    except:
        pass