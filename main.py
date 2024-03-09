from Delivery_time_predection.logger import logger 
from Delivery_time_predection.pipeline.data_ingection_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try: 
    logger.info(f">>>> stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n x===========x")

except Exception as e : 
    logger.exception(e)
    raise e 