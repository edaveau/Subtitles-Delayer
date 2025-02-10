from pathlib import Path
from time_utils import parse_timestamp

class srtDelayer():

    def __init__(self, path: str, timestamp: str, delay: int):
        path = Path(path)
        timestamp = parse_timestamp(timestamp)
        delay = delay

    def open_srt_file(self):
        print("")
