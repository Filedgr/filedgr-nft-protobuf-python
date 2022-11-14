from unittest import TestCase

from filedgr_nft_protobuf.deserialize import deserialize
from filedgr_nft_protobuf.exceptions.custom_exceptions import DeserializationException


class Test(TestCase):
    def test_deserialize_happy_path(self):
        input = b'\n$4ecebcf6-f22e-454d-ada2-79f5a1fc5a5b\x12$1f2e00ee-65a5-494c-a0d3-5a5917c134d2\x1aUhttps://bafybeigopd6f4l6f3czhhblqyoas666bqjrhaipl4s3fgb5ubcqniquzja.ipfs.filedgr.com/'
        id, campaign, uri = deserialize(
            input
        )
        self.assertEqual(id, "4ecebcf6-f22e-454d-ada2-79f5a1fc5a5b")
        self.assertEqual(campaign, "1f2e00ee-65a5-494c-a0d3-5a5917c134d2")
        self.assertEqual(uri, "https://bafybeigopd6f4l6f3czhhblqyoas666bqjrhaipl4s3fgb5ubcqniquzja.ipfs.filedgr.com/")

    def test_serialize_exception(self):
        input = None
        with self.assertRaises(DeserializationException):
            id, campaign, uri = deserialize(
                input
            )
