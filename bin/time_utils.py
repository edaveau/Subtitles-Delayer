import re
from datetime import timedelta
from string import Formatter


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


def strfdelta(tdelta, fmt='{D:02}d {H:02}h {M:02}m {S:02}s', inputtype='timedelta'):
    """
    Thanks to @MarredCheese for the code, you're the best dude !
    https://stackoverflow.com/a/42320260

    Convert a datetime.timedelta object or a regular number to a custom-
    formatted string, just like the stftime() method does for datetime.datetime
    objects.

    The fmt argument allows custom formatting to be specified.  Fields can 
    include seconds, minutes, hours, days, and weeks.  Each field is optional.

    Some examples:
        '{D:02}d {H:02}h {M:02}m {S:02}s' --> '05d 08h 04m 02s' (default)
        '{W}w {D}d {H}:{M:02}:{S:02}'     --> '4w 5d 8:04:02'
        '{D:2}d {H:2}:{M:02}:{S:02}'      --> ' 5d  8:04:02'
        '{H}h {S}s'                       --> '72h 800s'

    The inputtype argument allows tdelta to be a regular number instead of the  
    default, which is a datetime.timedelta object.  Valid inputtype strings: 
        's', 'seconds', 
        'm', 'minutes', 
        'h', 'hours', 
        'd', 'days', 
        'w', 'weeks'
    """

    # Convertir en total de secondes et extraire les millisecondes
    if inputtype == 'timedelta':
        total_seconds = tdelta.total_seconds()
    elif inputtype in ['s', 'seconds']:
        total_seconds = float(tdelta)
    elif inputtype in ['m', 'minutes']:
        total_seconds = float(tdelta) * 60
    elif inputtype in ['h', 'hours']:
        total_seconds = float(tdelta) * 3600
    elif inputtype in ['d', 'days']:
        total_seconds = float(tdelta) * 86400
    elif inputtype in ['w', 'weeks']:
        total_seconds = float(tdelta) * 604800
    else:
        raise ValueError(f"Invalid input type: {inputtype}")

    # Séparer les secondes entières et les millisecondes
    remainder = int(total_seconds)  # Secondes entières
    milliseconds = int((total_seconds - remainder) * 1000)  # Millisecondes

    f = Formatter()
    desired_fields = [field_tuple[1] for field_tuple in f.parse(fmt)]
    possible_fields = ('W', 'D', 'H', 'M', 'S', 'MS')
    constants = {'W': 604800, 'D': 86400, 'H': 3600, 'M': 60, 'S': 1}
    values = {}

    # Calcul des valeurs pour W, D, H, M, S
    for field in possible_fields:
        if field in desired_fields and field in constants:
            values[field], remainder = divmod(remainder, constants[field])

    # Ajouter les millisecondes
    if 'MS' in desired_fields:
        values['MS'] = milliseconds

    return f.format(fmt, **values)


def capture_srt_ts_format(ts_as_string) -> str:
    # Format hh:mm:ss,SSS
    match = re.fullmatch(r"(\d{2}):(\d{2}):(\d{2}),(\d{3})", ts_as_string)
    if match:
        return "{H:02}:{M:02}:{S:02},{MS:03}"

    # Format hh:mm:ss.SSS
    match = re.fullmatch(r"(\d{2}):(\d{2}):(\d{2})\.(\d{3})", ts_as_string)
    if match:
        return "{H:02}:{M:02}:{S:02}.{MS:03}"
