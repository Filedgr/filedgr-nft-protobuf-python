from . import filedgr_nft_pb2 as myNft
from .exceptions.custom_exceptions import SerializationException, DeserializationException


def deserialize(
        message: bytes
) -> (str, str, str):
    """
    Function to deserialize a Filedgr NFT
    :param message: The message to be deserialized.
    :return:
    """
    try:
        pass
    except Exception as exc:
        raise DeserializationException(exc)
