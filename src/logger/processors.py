import logging
import time

from structlog.types import EventDict


def add_log_level(_: logging.Logger, method_name: str, event_dict: EventDict) -> EventDict:
    if method_name == "warn":
        method_name = "warning"

    event_dict["loglevel"] = method_name

    return event_dict


def render_to_logmsg(_: logging.Logger, __: str, event_dict: EventDict) -> EventDict:
    if "event" in event_dict:
        event_dict["logmsg"] = event_dict.pop("event")

    return event_dict


def add_log_time(_: logging.Logger, __: str, event_dict: EventDict) -> EventDict:
    default_time_format = "%Y-%m-%dT%H:%M:%S"
    default_msec_format = "%s.%03d+00:00"
    if "_record" in event_dict:
        ct = time.localtime(event_dict["_record"].created)
        cms = event_dict["_record"].msecs
    else:
        t = time.time()
        ct = time.localtime(t)
        cms = (t - int(t)) * 1000
    s = time.strftime(default_time_format, ct)
    s = default_msec_format % (s, cms)
    event_dict["logtime"] = s
    return event_dict
