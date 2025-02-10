from bin.assert_type import assert_srt, assert_ts
from bin.srt_delayer import srtDelayer
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Script which allows you to delay a .srt file
        by N seconds after a given timecode"""
    )
    parser.add_argument("--filein", "-i", 
                        required=True, 
                        type=assert_srt,
                        help="Relative/Absolute path to srt file")
    parser.add_argument("--timestamp", "-t", 
                        required=True, 
                        type=assert_ts,
                        help="""Timestamp you want to start the delay from.
                        Examples of accepted formats : 
                        01:02:03,123 - 02:03:04.456 - 3560 - 3m20s""")
    parser.add_argument("--delay", "-d", 
                        required=True, 
                        type=float,
                        help="Delay for your subtitles (in seconds)")
    args = parser.parse_args()

    file_in = args.filein
    ts = args.timestamp
    delay = args.delay

    srt_delayer = srtDelayer(path=file_in, timestamp=ts, delay=delay)
    srt_generator = srt_delayer.open_srt_file()
    corrected_srt_generator = srt_delayer.delay_after_timestamp(srt_as_generator=srt_generator)
    srt_delayer.write_to_file(corrected_srt_generator=corrected_srt_generator)

