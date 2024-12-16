from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class ModelConfig:
    Model_name          : str 
    download_dir        : Path

@dataclass(frozen=True)
class PreprocessingConfig:
    model_path      : Path
    audio_file_path : Path
    text_file_path  : Path 
    
    
