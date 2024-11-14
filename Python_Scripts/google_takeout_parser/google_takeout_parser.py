import sys
from loading_bar import LoadingBar

import time

def parser():
    # Example usage of loading_bar within google_takeout_parser
    bar = LoadingBar(total=1000)
    for i in range(1000):
        # Simulate a task
        bar.update(i + 1)
        time.sleep(0.1)
    bar.close()

if __name__ == "__main__":
    parser()