import os 
import yaml
import json

import whisper
import librosa

from box import ConfigBox
from pathlib import Path

from ensure import ensure_annotations
from box.exceptions import BoxValueError

from Speech_2_Text import logger



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}") 


def load_and_preprocess_audio(file_path, target_sample_rate=16000):
    logger.info("load_and_preprocess_audio initialization....")
    audio_array, sample_rate = librosa.load(file_path, sr=None)  
    
    if sample_rate != target_sample_rate:
        audio_array = librosa.resample(audio_array,
                                       orig_sr   = sample_rate,
                                       target_sr = target_sample_rate)
    return audio_array, target_sample_rate


def noise_filtering(audio_array, sr=16000):
    logger.info("Apply a high-pass filter using librosa (removes low-frequency noise")
    audio_filtered = librosa.effects.preemphasis(audio_array)
    return audio_filtered







if __name__ == "__main__":
    logger.info("initialization....")
    

