import os
from dotenv import load_dotenv
from Speech_2_Text import logger
from Speech_2_Text.constants import *
from Speech_2_Text.utils.common import *
from Speech_2_Text.entity.config_entity import (ModelConfig,
                                                PreprocessingConfig)
                                                    



class ConfigurationManager:
    def __init__(self,
                 config_filepath    = CONFIG_FILE_PATH,
                 params_filepath    = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        


    def get_model_config(self) -> ModelConfig:
        params  = self.params
        config  = self.config
        logger.info("Model config initialized")
        load_dotenv()
        model_config = ModelConfig(Model_name       = params.MODEL_NAME,
                                   download_dir     = config.download_dir)
        return model_config
    
    def get_data_processing_config(self) -> PreprocessingConfig:
        config_                     = self.config.preprocessing_dir
        self.data_processing_config = PreprocessingConfig(
            model_path      = Path(config_.model_file_path),
            audio_file_path = Path(config_.audio_file_path),
            text_file_path  = Path(config_.text_file_path))
        
        return self.data_processing_config



if __name__ == "__main__":
    obj = ConfigurationManager()
    print(obj.get_data_processing_config().audio_file_path)
    
    