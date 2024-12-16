import whisper
from Speech_2_Text import logger
from Speech_2_Text.config.configuration import ConfigurationManager
from Speech_2_Text.entity.config_entity import ModelConfig


class ModelSetup:

    def __init__(self,config = ModelConfig):
        self.config = config

    def model_setup(self):
        logger.info("Model setup initialized")
        model = whisper.load_model(self.config.Model_name,
                                   download_root    = self.config.download_dir)
        
        logger.info(f"model----{(self.config.Model_name).split('/')[-1]}----created")
        logger.info(f"Model saved at {(self.config.download_dir)}") 
        return model 
    



if __name__ == "__main__":
    manager             = ConfigurationManager()
    model_config        = manager.get_model_config()
    model_setup         = ModelSetup(config=model_config)
    model               = model_setup.model_setup()