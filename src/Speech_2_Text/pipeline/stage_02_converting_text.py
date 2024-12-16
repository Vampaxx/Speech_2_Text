from Speech_2_Text import logger

from Speech_2_Text.components.data_processing import DataProcessing
from Speech_2_Text.config.configuration import ConfigurationManager



STAGE_NAME = "Data Processing Stage"

class DataProcessingPipeline:

    def __init__(self):
        pass
    def main(self):
        logger.info("processing initialized....")
        config                  = ConfigurationManager()
        data_processing_config  = config.get_data_processing_config()
        model_config            = DataProcessing(config=data_processing_config)
        model_config.save_transcription_txt()

if __name__ == "__main__":
    try:

        logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<")
        obj     = DataProcessingPipeline()
        obj.main()

        logger.info((f">>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx======x"))
    except Exception as e:
        raise e