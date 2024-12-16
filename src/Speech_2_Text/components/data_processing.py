import sys
import os 
from Speech_2_Text.utils.common import * 
from Speech_2_Text.config.configuration import ConfigurationManager
from Speech_2_Text.entity.config_entity import PreprocessingConfig



class DataProcessing:

    def __init__(self, config = PreprocessingConfig):
        self.config_ = config


    def transcribe_audio(self):
        audio_array, sample_rate    = load_and_preprocess_audio(self.config_.audio_file_path) 
        audio_filtered              = noise_filtering(audio_array, sr=sample_rate)
        
        mel             = whisper.pad_or_trim(audio_filtered)
        model           = whisper.load_model(self.config_.model_path)
        result          = model.transcribe(mel)
        transcription   = result["text"]
        return transcription
    

    def save_transcription_txt(self):
        transcription   = self.transcribe_audio()

        with open(self.config_.text_file_path, 'w') as file:
            file.write(transcription)
        print(f"Transcription saved to {self.config_.text_file_path}")


if __name__ == "__main__":
    config                  = ConfigurationManager()
    data_processing_config  = config.get_data_processing_config()
    model_config            = DataProcessing(config=data_processing_config)
    model_config.save_transcription_txt()
    