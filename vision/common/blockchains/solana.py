"""Module for Solana-specific utilities and errors.

"""
import typing

from vision.common.blockchains.base import BlockchainUtilities
from vision.common.blockchains.base import BlockchainUtilitiesError
from vision.common.blockchains.base import NodeConnections
from vision.common.blockchains.base import UnhealthyNode
from vision.common.blockchains.base import VersionedContractAbi
from vision.common.blockchains.enums import Blockchain
from vision.common.entities import TransactionStatus
from vision.common.types import BlockchainAddress

M = typing.TypeVar('M')


class SolanaUtilitiesError(BlockchainUtilitiesError):
    """Exception class for all Solana utilities errors.

    """
    pass


class SolanaUtilities(BlockchainUtilities):
    """Class for Solana-specific utilities.

    """
    def __init__(self, blockchain_node_urls: list[str],
                 fallback_blockchain_node_urls: list[str],
                 average_block_time: int,
                 required_transaction_confirmations: int,
                 transaction_network_id: typing.Optional[int],
                 default_private_key: typing.Optional[tuple[str, str]] = None,
                 celery_tasks_enabled: bool = False):
        # Docstring inherited
        super().__init__(blockchain_node_urls, fallback_blockchain_node_urls,
                         average_block_time,
                         required_transaction_confirmations,
                         transaction_network_id,
                         default_private_key=default_private_key,
                         celery_tasks_enabled=celery_tasks_enabled)

    def get_address(self, private_key: str) -> str:
        # Docstring inherited
        raise NotImplementedError  # pragma: no cover

    def get_balance(
            self, account_address: str,
            token_address: typing.Optional[str] = None,
            node_connections: typing.Optional[NodeConnections] = None) -> int:
        # Docstring inherited
        raise NotImplementedError  # pragma: no cover

    @classmethod
    def get_blockchain(cls) -> Blockchain:
        # Docstring inherited
        return Blockchain.SOLANA

    @classmethod
    def get_error_class(cls) -> type[BlockchainUtilitiesError]:
        # Docstring inherited
        return SolanaUtilitiesError

    def is_valid_address(self, address: str) -> bool:
        # Docstring inherited
        raise NotImplementedError  # pragma: no cover

    def is_equal_address(self, address_one: str, address_two: str) -> bool:
        # Docstring inherited
        raise NotImplementedError  # pragma: no cover

    def is_protocol_version_supported_by_contract(
            self, contract_address: BlockchainAddress,
            versioned_contract_abi: VersionedContractAbi,
            node_connections: NodeConnections | None = None) -> bool:
        # Docstring inherited
        raise NotImplementedError  # pragma: no cover

    def get_unhealthy_nodes(
            self, blockchain_nodes: list[str],
            timeout: float | tuple | None = None) -> list[UnhealthyNode]:
        # Docstring inherited
        raise NotImplementedError  # pragma: no cover

    def _get_transaction_method_names(self) -> list[str]:
        # Docstring inherited
        raise NotImplementedError  # pragma: no cover

    def decrypt_private_key(self, encrypted_key: str, password: str) -> str:
        # Docstring inherited
        raise NotImplementedError  # pragma: no cover

    def read_transaction_status(
            self, transaction_id: str,
            node_connections: typing.Optional[NodeConnections] = None) \
            -> TransactionStatus:
        # Docstring inherited
        raise NotImplementedError  # pragma: no cover

    def get_number_of_confirmations(
        self, transaction_id: str,
        node_connections: typing.Optional[NodeConnections] = None
    ) -> tuple[TransactionStatus, int]:
        # Docstring inherited
        raise NotImplementedError

    def submit_transaction(
            self, request: BlockchainUtilities.TransactionSubmissionRequest,
            node_connections: typing.Optional[NodeConnections] = None) \
            -> BlockchainUtilities.TransactionSubmissionResponse:
        # Docstring inherited
        raise NotImplementedError  # pragma: no cover

    def _create_single_node_connection(
            self, blockchain_node_url: str,
            timeout: typing.Optional[typing.Union[float, tuple]] = None,
            node_connections_middlewares: list[M] = []) -> typing.Any:
        # Docstring inherited
        raise NotImplementedError  # pragma: no cover
