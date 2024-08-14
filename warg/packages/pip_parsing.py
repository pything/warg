#!/usr/bin/env python3
import logging
from pathlib import Path
from typing import Union
from urllib.parse import urlparse

logger = logging.getLogger(__name__)
from warg.functions import sink

__all__ = ["get_requirements_from_file"]

try:
    # from packaging.requirements import Requirement

    # noinspection PyProtectedMember
    from pip._internal.network.session import PipSession

    # noinspection PyProtectedMember
    from pip._internal.req import parse_requirements

    # noinspection PyProtectedMember
    from pip._internal.req.req_file import ParsedRequirement

    # noinspection PyProtectedMember
    from pip._internal.utils.packaging import get_requirement

    def get_reqed(
        req,
        #: ParsedRequirement
    ):  # -> Requirement:
        """
        https://packaging.python.org/en/latest/specifications/direct-url/#example-pip-commands-and-their-effect-on-direct-url-json

        :param req:
        :type req: ParsedRequirement
        :return:
        :rtype: Requirement
        """

        req_ = req.requirement

        if req.is_editable:  # parse out egg=... fragment from VCS URL
            parsed = urlparse(req_)
            egg_name = parsed.fragment.partition("egg=")[-1]

            if not egg_name:
                egg_name = parsed.path.split("/")[-1]

            without_fragment = parsed._replace(fragment="").geturl()
            req_parsed = f"{egg_name} @ {without_fragment}"
        else:
            req_parsed = req_

        try:
            return get_requirement(req_parsed)
        except:
            return None

    def get_requirements_from_file(
        file_path: Union[str, Path], session: Union[str, PipSession] = "test"
    ):  # -> List[Requirement]
        """Turn requirements.txt into a list"""
        if isinstance(file_path, Path):
            file_path = str(file_path)

        parsed_reqs = [get_reqed(ir) for ir in parse_requirements(file_path, session=session)]

        return [p for p in parsed_reqs if p]

except Exception as e:  # (ModuleNotFoundError, ImportError) as e: #KeyError occurred
    logger.error(e)
    get_requirements_from_file = sink
    # logger.info('You version of python is to old!')

if __name__ == "__main__":
    logger.info(get_requirements_from_file(Path(__file__).parent.parent.parent / "requirements.txt"))
