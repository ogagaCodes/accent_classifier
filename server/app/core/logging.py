import logging, sys

def setup_logging():
    fmt = '{"time":"%(asctime)s","level":"%(levelname)s","message":%(message)s}'
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=fmt)