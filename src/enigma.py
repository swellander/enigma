from random import randrange
from math import floor

from rotors import rotors


class Enigma(object):

    def __init__(self, key):
        try:
            self.rotors = rotors[:-1]
            self.reflector = rotors[-1]
        except:
            raise ValueError('You need to run `enigma init` first.')

        self.initial_step = self.curr_step = self._get_initial_step(key)

    def encrypt_text(self, text: str) -> str:
        encrypted_text = ''
        for char in text:
            encrypted_text += self._encrypt_char(char)
            self.curr_step += 1

        self._reset_curr_step()
        return encrypted_text

    def decrypt_text(self, text: str) -> str:
        decrypted_text = ''
        for char in text:
            decrypted_text += self._decrypt_char(char)
            self.curr_step += 1

        self._reset_curr_step()
        return decrypted_text

    def _reset_curr_step(self):
        """
        Resets the settings of the machine back to their initial state.
        To be used after encrypting an entire message.
        """

        self.curr_step = self.initial_step

    def _encrypt_char(self, char: str) -> str:
        """
        Pass character forward through rotors.
        """

        return self._process_char(char)

    def _decrypt_char(self, char: str) -> str:
        """
        Pass character backward through rotors.
        """

        return self._process_char(char, reflected=True)

    def _process_char(self, char: str, reflected=False) -> str:
        """
        Passes a character through rotors, changing its value
        for each rotor.
        """
        rotor_listing = [(idx, rotor) for idx, rotor in enumerate(self.rotors)]
        for rotor_num, rotor in rotor_listing:
            char = self._convert_char(
                char=char,
                rotor=rotor,
                rotor_num=rotor_num,
                reverse=reflected)

        char = self._convert_char(
            char=char,
            rotor=self.reflector,
            reflected=reflected,
            rotor_num=len(rotor_listing),
            reverse=reflected)

        for rotor_num, rotor in rotor_listing[::-1]:
            char = self._convert_char(
                char=char,
                rotor=rotor,
                reflected=True,
                rotor_num=rotor_num,
                reverse=reflected)

        return char

    def _convert_char(self, *, char: str, rotor: list, rotor_num: int, reverse: bool, reflected=False) -> str:
        """ Passes char through an individual rotor"""

        front = 1 if reflected else 0
        back = 0 if reflected else 1
        rotor_length = len(rotor)
        shift = floor(self.curr_step / rotor_length**rotor_num)

        for idx, input_mapping in enumerate(rotor):
            if input_mapping[front] == char:
                if reverse:
                    total_shift = idx - shift
                else:
                    total_shift = idx + shift

                output_mapping_idx = total_shift % rotor_length
                output_char = rotor[output_mapping_idx][back]
                return output_char

    def _get_initial_step(self, key: str) -> int:
        return int(key.encode().hex(), 16)
