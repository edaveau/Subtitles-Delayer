from pathlib import Path
import re

def assert_srt(srt_file: str):
    file = Path(srt_file)
    if file.exists() and "srt" in file.suffix:
        return srt_file
    elif file.exists():
        answer = input("Le fichier spécifié en input ne semble pas correspondre à un fichier .srt, continuer ? [o / n]")
        if answer.lower() in ["y", "o", "yes", "oui"]:
            return srt_file
    else:
        raise FileNotFoundError

def assert_ts(time_str: str):
    patterns = [
        r"^\d{2}:\d{2}:\d{2},\d{3}$",  # hh:mm:ss,SSS
        r"^\d{2}:\d{2}:\d{2}\.\d{3}$",  # hh:mm:ss.SSS
        r"^\d+$",  # secondes (nombre entier)
        r"^\d+m\d+s$",  # %Mm%Ss
    ]
    
    if any(re.fullmatch(pattern, time_str) for pattern in patterns):
        return time_str
    else:
        raise ValueError
