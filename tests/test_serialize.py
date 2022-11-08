from unittest import TestCase

from filedgr_nft_protobuf.exceptions.custom_exceptions import SerializationException
from filedgr_nft_protobuf.serialize import serialize


class Test(TestCase):
    def test_serialize_happy_path(self):
        expected_value = b'\n$4ecebcf6-f22e-454d-ada2-79f5a1fc5a5b\x12$1f2e00ee-65a5-494c-a0d3-5a5917c134d2\x1aUhttps://bafybeigopd6f4l6f3czhhblqyoas666bqjrhaipl4s3fgb5ubcqniquzja.ipfs.filedgr.com/'
        result = serialize(
            nft_id='4ecebcf6-f22e-454d-ada2-79f5a1fc5a5b',
            campaign='1f2e00ee-65a5-494c-a0d3-5a5917c134d2',
            uri="https://bafybeigopd6f4l6f3czhhblqyoas666bqjrhaipl4s3fgb5ubcqniquzja.ipfs.filedgr.com/"
        )
        self.assertEqual(
            expected_value,
            result
        )

    def test_serialize_exception(self):
        with self.assertRaises(SerializationException):
            result = serialize(
                nft_id='4ecebcf6-f22e-454d-ada2-79f5a1fc5a5b',
                campaign='1f2e00ee-65a5-494c-a0d3-5a5917c134d2',
                uri=None
            )
