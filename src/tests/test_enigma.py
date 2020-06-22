from unittest import TestCase, mock

from enigma import Enigma


class TestEnigma(TestCase):

    def setUp(self):
        self.key = 'secret_key'
        self.enigma = Enigma(self.key)
        self.mock_rotor = [
            ('a', 'b'),
            ('b', 'a'),
        ]

    def test__get_initial_step_returns_an_int(self):
        returned_val = self.enigma._get_initial_step(self.key)
        assert type(returned_val) is int

    def test__get_initial_step_returns_encoded_int_value_of_key(self):
        expected_val = int(self.key.encode().hex(), 16)
        returned_val = self.enigma._get_initial_step(self.key)
        assert returned_val == expected_val

    def test__convert_char_returns_a_string(self):
        returned_val = self.enigma._convert_char(
            char='a',
            rotor=self.mock_rotor,
            rotor_num=0,
            reverse=False)
        assert type(returned_val) is str

    def test__process_char_returns_a_string(self):
        returned_val = self.enigma._process_char('a')
        assert type(returned_val) is str

    def test__decrypt_char_returns_a_string(self):
        returned_val = self.enigma._decrypt_char('a')
        assert type(returned_val) is str

    @mock.patch.object(Enigma, '_process_char')
    def test__decrypt_char_calls_process_char_with_reflected_true(self, mock_process_char):
        self.enigma._decrypt_char('a')
        mock_process_char.assert_called_with('a', reflected=True)

    def test__encrypt_char_returns_a_string(self):
        returned_val = self.enigma._encrypt_char('a')
        assert type(returned_val) is str

    @mock.patch.object(Enigma, '_process_char')
    def test__encrypt_char_calls_process_char_with_reflected_true(self, mock_process_char):
        self.enigma._encrypt_char('a')
        mock_process_char.assert_called_with('a')

    def test__reset_curr_step_sets_curr_step_to_inital_step(self):
        assert self.enigma.curr_step == self.enigma.initial_step

        self.enigma.curr_step += 33
        assert self.enigma.curr_step != self.enigma.initial_step

        self.enigma._reset_curr_step()
        assert self.enigma.curr_step == self.enigma.initial_step

    def test_encrypt_text_returns_a_string(self):
        return_val = self.enigma.encrypt_text('secret message')

        assert type(return_val) is str

    @mock.patch.object(Enigma, '_reset_curr_step')
    def test_encrypt_text_calls_reset_curr_step(self, mock_reset_curr_step):
        self.enigma.encrypt_text('secret message')
        mock_reset_curr_step.assert_called_once()

    def test_encrypt_text_encrypts_consistently(self):
        msg_to_encrypt = 'secret message'
        first_encrypted_msg = self.enigma.encrypt_text(msg_to_encrypt)
        second_encrypted_msg = self.enigma.encrypt_text(msg_to_encrypt)

        assert first_encrypted_msg == second_encrypted_msg

    def test_encrypt_text_does_not_return_original_text(self):
        msg_to_encrypt = 'secret message'
        encrypted_msg = self.enigma.encrypt_text(msg_to_encrypt)

        assert encrypted_msg != msg_to_encrypt

    def test_decrypt_text_returns_a_string(self):
        return_val = self.enigma.decrypt_text('jfsd#jd0')

        assert type(return_val) is str

    @mock.patch.object(Enigma, '_reset_curr_step')
    def test_decrypt_text_calls_reset_curr_step(self, mock_reset_curr_step):
        self.enigma.decrypt_text('jfsd#jd0')
        mock_reset_curr_step.assert_called_once()

    def test_decrypt_text_decrypts_consistently(self):
        msg_to_decrypt = 'jfsd#jd0'
        first_decrypted_msg = self.enigma.decrypt_text(msg_to_decrypt)
        second_decrypted_msg = self.enigma.decrypt_text(msg_to_decrypt)

        assert first_decrypted_msg == second_decrypted_msg

    def test_decrypt_text_does_not_return_original_text(self):
        msg_to_decrypt = 'jfsd#jd0'
        decrypted_msg = self.enigma.decrypt_text(msg_to_decrypt)

        assert decrypted_msg != msg_to_decrypt
