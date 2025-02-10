import re
from datetime import timedelta

def parse_timestamp(value) -> timedelta:
    """ Convertit un timestamp en timedelta. """

    # Format hh:mm:ss,SSS
    match = re.fullmatch(r"(\d{2}):(\d{2}):(\d{2}),(\d{3})", value)
    if match:
        hours, minutes, seconds, milliseconds = map(int, match.groups())
        return timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)

    # Format hh:mm:ss.SSS
    match = re.fullmatch(r"(\d{2}):(\d{2}):(\d{2})\.(\d{3})", value)
    if match:
        hours, minutes, seconds, milliseconds = map(int, match.groups())
        return timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)

    # Format secondes (ex: "3560" -> 3560 sec)
    match = re.fullmatch(r"(\d+)", value)
    if match:
        return timedelta(seconds=int(value))

    # Format %Mm%Ss (ex: "3m20s")
    match = re.fullmatch(r"(\d+)m(\d+)s", value)
    if match:
        minutes, seconds = map(int, match.groups())
        return timedelta(minutes=minutes, seconds=seconds)

    # Si aucun format ne correspond, lever une erreur
    raise ValueError(f"Invalid timestamp format: {value}")

