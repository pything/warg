__all__ = ["get_version"]

import datetime
from logging import warning


def get_version(version: str, append_time: bool) -> str:
    """

    :param version:
    :param append_time:
    :return:
    """

    if not version:
        version = "0.0.0"

    if append_time:
        now = datetime.datetime.utcnow()
        date_version = now.strftime("%Y%m%d%H%M%S")
        # date_version = time.time()

        if version:
            # Most git tags are prefixed with 'v' (example: v1.2.3) this is
            # never desirable for artefact repositories, so we strip the
            # leading 'v' if it's present.
            version = version[1:] if isinstance(version, str) and version.startswith("v") else version
        else:
            # The Default version is an ISO8601 compliant datetime. PyPI doesn't allow
            # the colon ':' character in its versions, and time is required to allow
            # for multiple publications to master in one day. This datetime string
            # uses the 'basic' ISO8601 format for both its date and time components
            # to avoid issues with the colon character (ISO requires that date and
            # time components of a date-time string must be uniformly basic or
            # extended, which is why the date component does not have dashes.)
            #
            # Publications using datetime versions should only be made from master
            # to represent the HEAD moving forward.
            warning(f"Environment variable VERSION is not set, only using datetime: {date_version}")

            # warn(f'Environment variable VERSION is not set, only using timestamp: {version}')

        version = f"{version}.{date_version}"

    return version
