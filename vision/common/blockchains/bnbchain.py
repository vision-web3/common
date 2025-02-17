"""Module for BNB-Chain-specific utilities and errors. Since the BNB
Smart Chain is Ethereum-compatible, the utilities implementation
inherits from the vision.common.blockchains.ethereum module.

"""
from vision.common.blockchains.base import BlockchainUtilitiesError
from vision.common.blockchains.enums import Blockchain
from vision.common.blockchains.ethereum import EthereumUtilities
from vision.common.blockchains.ethereum import EthereumUtilitiesError


class BnbChainUtilitiesError(EthereumUtilitiesError):
    """Exception class for all BNB Chain utilities errors.

    """
    pass


class BnbChainUtilities(EthereumUtilities):
    """Class for BNB-Chain-specific utilities.

    """
    @classmethod
    def get_blockchain(cls) -> Blockchain:
        # Docstring inherited
        return Blockchain.BNB_CHAIN

    @classmethod
    def get_error_class(cls) -> type[BlockchainUtilitiesError]:
        # Docstring inherited
        return BnbChainUtilitiesError
