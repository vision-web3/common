"""Module for Polygon-specific utilities and errors. Since Polygon is
Ethereum-compatible, the utilities implementation inherits from the
vision.common.blockchains.ethereum module.

"""
from vision.common.blockchains.base import BlockchainUtilitiesError
from vision.common.blockchains.enums import Blockchain
from vision.common.blockchains.ethereum import EthereumUtilities
from vision.common.blockchains.ethereum import EthereumUtilitiesError


class PolygonUtilitiesError(EthereumUtilitiesError):
    """Exception class for all Polygon utilities errors.

    """
    pass


class PolygonUtilities(EthereumUtilities):
    """Class for Polygon-specific utilities.

    """
    @classmethod
    def get_blockchain(cls) -> Blockchain:
        # Docstring inherited
        return Blockchain.POLYGON

    @classmethod
    def get_error_class(cls) -> type[BlockchainUtilitiesError]:
        # Docstring inherited
        return PolygonUtilitiesError
