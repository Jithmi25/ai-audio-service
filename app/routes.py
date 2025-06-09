from fastapi import APIRouter, UploadFile, File
from app.whisper_model import transcribe_audio
from utils.file_handler import save_temp_file, remove_file

router = APIRouter()

@router.post("/analyze-audio/")
async def analyze_audio(file: UploadFile = File(...)):
    file_path = save_temp_file(file)
    transcription = transcribe_audio(file_path)
    remove_file(file_path)
    return {"transcription": transcription}
