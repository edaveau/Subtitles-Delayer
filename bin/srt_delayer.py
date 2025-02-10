from bin.time_utils import parse_timestamp, capture_srt_ts_format, strfdelta
from datetime import timedelta
from pathlib import Path

class srtDelayer:

    def __init__(self, path: str, timestamp: str, delay: int):
        self.srt_path = Path(path)
        self.timestamp = parse_timestamp(timestamp)
        self.delay = timedelta(seconds=delay)

    def open_srt_file(self):
        with open(self.srt_path, mode="r") as f_in:
            yield from f_in

    def delay_after_timestamp(self, srt_as_generator):
        for srt_line in srt_as_generator:
            srt_line_list = [elem.strip() for elem in srt_line.split(sep=" ")]
            if "-->" in srt_line_list:
                srt_line = self.delay_subtitles(srt_line_list)
            yield(srt_line.strip())
        
    def delay_subtitles(self, ts_line_as_list: list):
        for index, elem in enumerate(ts_line_as_list):
            if not "-->" in elem:
                ts = parse_timestamp(elem)  # Conversion en timedelta

                if ts >= self.timestamp:
                    ts += self.delay  # Décalage du timestamp
                    ts_format = capture_srt_ts_format(elem)  # Détection du format
                    ts_line_as_list[index] = strfdelta(ts, ts_format)  # Conversion en string

        return " ".join(ts_line_as_list)
    
    def write_to_file(self, corrected_srt_generator: str, prefix="copy_"):
        filepath = self.srt_path.parent
        file_copy_name = prefix + self.srt_path.name
        file_copy_fullpath = Path(filepath/file_copy_name).as_posix()

        with open(file_copy_fullpath, "w") as f_out:
            for line in corrected_srt_generator:
                f_out.write(line)
            print(f"Subtitles successfully delayed by {str(self.delay)} after {str(self.timestamp)}. The new copy can be found here: {file_copy_fullpath}")
