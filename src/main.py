import logging 
import sys

from config.setting import settings

def setup_logging():
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(settings.log_file),
        ],
    )

def run_scan():
    logger = logging.getLogger(__name__) 
    try:
        pass
    except KeyboardInterrupt:
        logging.warning("scan interupted by user")
        sys.exit(1)
    except Exception:
            logging.warning("System Failed")
            sys.exit(1)

def main():
    setup_logging()
    run_scan()


if __name__ == '__main__':
    main()