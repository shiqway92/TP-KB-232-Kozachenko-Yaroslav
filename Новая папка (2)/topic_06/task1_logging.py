
import logging

logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_calculation(operation, a, b, result):
    logging.info(f"{operation} {a}, {b} = {result}")

if __name__ == "__main__":
    log_calculation("add", 2, 3, 5)
    log_calculation("subtract", 10, 3, 7)
    print("Logging completed. Check 'calculator.log' file.")
