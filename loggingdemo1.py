import logging

# Configure logging
logging.basicConfig(
    filename="C:\\Users\\ACER\Documents\\Selenium_automation\\More_SeleniumPractise\\demo.log",
    level=logging.DEBUG,  # Set the minimum logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Set the log message format
    datefmt='%Y-%m-%d %H:%M:%S'  # Set the date format
)

# Create a logger instance
logger = logging.getLogger('MyLogger')  # Name the logger

# Log messages at different levels
logger.debug("This is a DEBUG message. Used for detailed debugging information.")
logger.info("This is an INFO message. General information about program execution.")
logger.warning("This is a WARNING message. An indication of a possible issue.")
logger.error("This is an ERROR message. An error occurred during execution.")
logger.critical("This is a CRITICAL message. A serious error indicating the program may not be able to continue.")