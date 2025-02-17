"""Module for Cronos-specific utilities and errors. Since Cronos is
Ethereum-compatible, the utilities implementation inherits from the
vision.common.blockchains.ethereum module.

"""
from vision.common.blockchains.base import BlockchainUtilitiesError
from vision.common.blockchains.enums import Blockchain
from vision.common.blockchains.ethereum import EthereumUtilities
from vision.common.blockchains.ethereum import EthereumUtilitiesError


class CronosUtilitiesError(EthereumUtilitiesError):
    """Exception class for all Cronos utilities errors.

    """
    pass


class CronosUtilities(EthereumUtilities):
    """Class for Cronos-specific utilities.

    """
    @classmethod
    def get_blockchain(cls) -> Blockchain:
        # Docstring inherited
        return Blockchain.CRONOS

    @classmethod
    def get_error_class(cls) -> type[BlockchainUtilitiesError]:
        # Docstring inherited
        return CronosUtilitiesError
