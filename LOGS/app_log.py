import logging
import os

# Function to set up logging
def setup_logging():
    log_dir = '/Users/mananrawat/Desktop/Project/UPDATED CODEE/DevOpsProject/LOGS'  # Log directory path

    # Create the 'LOGS' directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Configure logging to write logs to 'LOGS/app.log'
    logging.basicConfig(
        filename=os.path.join(log_dir, 'app.log'),  # Save logs to 'LOGS/app.log'
        level=logging.INFO,  # Set log level
        format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
    )

    # Optional: Add a stream handler to also output logs to the console
    console_handler = logging.StreamHandler()
    logging.getLogger().addHandler(console_handler)

    logging.info("Logging has been configured.")  # Log that setup is complete
