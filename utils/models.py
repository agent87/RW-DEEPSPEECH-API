from pydantic import BaseModel

class InferenceObj(BaseModel):
    text: str
    file_path : str