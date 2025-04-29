import logging

# Set up logging configuration
logging.basicConfig(filename='app.log', level=logging.INFO)

def main():
    logging.info("Script started.")
    try:
        # Intentional division by zero to raise an exception
        x = 10 / 0
    except ZeroDivisionError as e:
        logging.error(f"Error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
