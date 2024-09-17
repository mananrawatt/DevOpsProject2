# import logging
# import os
#
# def setup_logging():
#     # Set the log directory path
#     log_dir = '/Users/mananrawat/Desktop/Project/UPDATED CODEE/DevOpsProject/LOGS'
#
#     # Create the 'LOGS' directory if it doesn't exist
#     try:
#         if not os.path.exists(log_dir):
#             os.makedirs(log_dir)
#             print(f"Directory {log_dir} created successfully.")
#         else:
#             print(f"Directory {log_dir} already exists.")
#     except Exception as e:
#         print(f"Failed to create directory: {e}")
#         return
#
#     # Set the log file path
#     log_file = os.path.join(log_dir, 'app.log')
#
#     # Check if we have permission to write to the directory
#     if not os.access(log_dir, os.W_OK):
#         print(f"Cannot write to directory: {log_dir}")
#         return
#
#     # Configure logging to save logs in the specified file with a .log extension
#     try:
#         logging.basicConfig(
#             filename=log_file,  # Save logs to 'LOGS/app.log'
#             level=logging.INFO,  # Log level
#             format='%(asctime)s - %(levelname)s - %(message)s',
#             filemode='w'  # Overwrite the log file each time the script runs
#         )
#
#         # Optional: Add a console handler if you want to see logs in the terminal too
#         console_handler = logging.StreamHandler()
#         console_handler.setLevel(logging.INFO)
#         formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#         console_handler.setFormatter(formatter)
#         logging.getLogger().addHandler(console_handler)
#
#         # Log an initial message when logging is configured
#         logging.info("Logging is set up successfully")
#         print(f"Logging set up successfully. Logs are being saved to {log_file}.")
#     except Exception as e:
#         print(f"Failed to set up logging: {e}")
#
# # Ensure logging is configured by calling the function
# setup_logging()


import logging
import os


def setup_logging():
    # Set the log directory path
    log_dir = '/Users/mananrawat/Desktop/Project/UPDATED CODEE/abv/DevOpsProject/LOGS'

    # Create the 'LOGS' directory if it doesn't exist
    try:
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            print(f"Directory {log_dir} created successfully.")
        else:
            print(f"Directory {log_dir} already exists.")
    except Exception as e:
        print(f"Failed to create directory: {e}")
        return

    # Set the log file path
    log_file = os.path.join(log_dir, 'app.log')

    # Check if we have permission to write to the directory
    if not os.access(log_dir, os.W_OK):
        print(f"Cannot write to directory: {log_dir}")
        return

    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create handlers: one for file and one for console
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Log an initial message when logging is configured
    logger.info("Logging is set up successfully")
    print(f"Logging set up successfully. Logs are being saved to {log_file}.")

    # Check if the log file is created
    if os.path.exists(log_file):
        print(f"Log file created successfully at {log_file}")
    else:
        print("Log file was not created.")


# Ensure logging is configured by calling the function
setup_logging()
