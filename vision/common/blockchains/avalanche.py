"""Module for Avalanche-specific utilities and errors. Since the
Avalanche C-Chain is Ethereum-compatible, the utilities implementation
inherits from the vision.common.blockchains.ethereum module.

"""
from vision.common.blockchains.base import BlockchainUtilitiesError
from vision.common.blockchains.enums import Blockchain
from vision.common.blockchains.ethereum import EthereumUtilities
from vision.common.blockchains.ethereum import EthereumUtilitiesError


class AvalancheUtilitiesError(EthereumUtilitiesError):
    """Exception class for all Avalanche utilities errors.

    """
    pass


class AvalancheUtilities(EthereumUtilities):
    """Class for Avalanche-specific utilities.

    """
    @classmethod
    def get_blockchain(cls) -> Blockchain:
        # Docstring inherited
        return Blockchain.AVALANCHE

    @classmethod
    def get_error_class(cls) -> type[BlockchainUtilitiesError]:
        # Docstring inherited
        return AvalancheUtilitiesError
