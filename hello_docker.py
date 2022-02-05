import logging
from pathlib import Path


def log_something():
    logger.info("Hello Docker, this is a test log.")


if __name__ == '__main__':
    REPO_ROOT = Path(__file__).parents[0]
    LOG_FOLDER = REPO_ROOT / "logs"
    LOG_FOLDER.mkdir(exist_ok=True)
    LOG_FILE_PATH = Path(LOG_FOLDER, "hello_docker.log")

    logger = logging.getLogger("hello_docker_class")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(LOG_FILE_PATH)
    log_formatter = logging.Formatter(f"%(asctime)s\t%(levelname)s - {__file__} : %(message)s")
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)

    log_something()
