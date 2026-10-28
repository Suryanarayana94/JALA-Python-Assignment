# Logging errors
import logging
logging.basicConfig(level=logging.ERROR)
try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("Error occurred: %s", e)
print("Logged error above")
