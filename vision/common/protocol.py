"""Module for keeping track of supported Vision-web3 protocol versions.

"""
import typing

import semantic_version  # type: ignore

_SUPPORTED_PROTOCOL_VERSIONS: typing.Final[set[semantic_version.Version]] = {
    semantic_version.Version('0.3.0')
}


def get_latest_protocol_version() -> semantic_version.Version:
    """Get the latest supported Vision-web3 protocol version.

    Returns
    -------
    semantic_version.Version
        The protocol version.

    """
    return max(_SUPPORTED_PROTOCOL_VERSIONS)


def get_supported_protocol_versions() -> list[semantic_version.Version]:
    """Get all supported Vision-web3 protocol versions.

    Returns
    -------
    list of semantic_version.Version
        The protocol versions.

    """
    return sorted(_SUPPORTED_PROTOCOL_VERSIONS)


def is_supported_protocol_version(version: semantic_version.Version) -> bool:
    """Check if a given version is a supported Vision-web3 protocol version.

    Parameters
    ----------
    version : semantic_version.Version
        The version to check.

    Returns
    -------
    bool
        True if the protocol version is supported.

    """
    return version in _SUPPORTED_PROTOCOL_VERSIONS
