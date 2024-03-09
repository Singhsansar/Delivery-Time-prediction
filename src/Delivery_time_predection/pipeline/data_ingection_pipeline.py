from Delivery_time_predection.config.configuration  import ConfigurationManager
from Delivery_time_predection.components import DataIngestion
from Delivery_time_predection.logger import logger 


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)

            # Assuming download_file and extract_zip_file can raise specific exceptions
            data_ingestion.download_file()
            # data_ingestion.extract_zip_file()
        except FileNotFoundError as file_not_found_error:
            print(f"File not found: {file_not_found_error}")

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            raise
