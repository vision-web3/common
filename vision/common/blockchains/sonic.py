"""Module for Sonic-specific utilities and errors. Since Sonic is
Ethereum-compatible, the utilities implementation inherits from the
vision.common.blockchains.ethereum module.

Note that Vision-web3 used to support Sonic's predecessor Fantom. This module
was renamed accordingly on 2024-10-17.

"""
from vision.common.blockchains.base import BlockchainUtilitiesError
from vision.common.blockchains.enums import Blockchain
from vision.common.blockchains.ethereum import EthereumUtilities
from vision.common.blockchains.ethereum import EthereumUtilitiesError


class SonicUtilitiesError(EthereumUtilitiesError):
    """Exception class for all Sonic utilities errors.

    """
    pass


class SonicUtilities(EthereumUtilities):
    """Class for Sonic-specific utilities.

    """
    @classmethod
    def get_blockchain(cls) -> Blockchain:
        # Docstring inherited
        return Blockchain.SONIC

    @classmethod
    def get_error_class(cls) -> type[BlockchainUtilitiesError]:
        # Docstring inherited
        return SonicUtilitiesError
