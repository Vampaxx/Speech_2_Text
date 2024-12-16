from Speech_2_Text import logger

from Speech_2_Text.components.Model import ModelSetup
from Speech_2_Text.config.configuration import ConfigurationManager




STAGE_NAME = "Data Model Stage"

class ModelPipeline:

    def __init__(self):
        pass
    def main(self):
        manager             = ConfigurationManager()
        model_config        = manager.get_model_config()
        model_setup         = ModelSetup(config=model_config)
        model               = model_setup.model_setup()

if __name__ == "__main__":
    try:

        logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<")
        obj     = ModelPipeline()
        obj.main()

        logger.info((f">>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx======x"))
    except Exception as e:
        raise e