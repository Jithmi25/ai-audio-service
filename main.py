from fastapi import FastAPI, File, UploadFile
import whisper
import shutil
import os

app = FastAPI()

# Load Whisper model (you can change "base" to "small", "medium", or "large")
model = whisper.load_model("base")

@app.post("/analyze-audio/")
async def analyze_audio(file: UploadFile = File(...)):
    try:
        # Create a temp folder if it doesn't exist
        os.makedirs("temp", exist_ok=True)

        # Save uploaded file temporarily
        file_location = f"temp/{file.filename}"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Run Whisper model to transcribe audio
        result = model.transcribe(file_location)

        # Remove the temporary file
        os.remove(file_location)

        # Return the transcription result
        return {"transcription": result["text"]}
    
    except Exception as e:
        return {"error": str(e)}
