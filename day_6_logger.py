import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(filename='logs/day_6.log', 
                    level=logging.INFO, 
                    format='%(asctime)-15s - %(name)-8s - %(levelname)-8s - %(message)-15s', 
                    filemode='w')

logger = logging.getLogger(__name__)