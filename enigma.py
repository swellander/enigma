from random import randrange
from math import floor


class Enigma(object):

    num_potential_chars = 95
    num_rotors = 3

    rotor_1 = [
        ("'", '/'),
        ('d', 'D'),
        ('4', '\n'),
        ('\n', 'Q'),
        ('F', 'u'),
        ('s', '}'),
        ('I', 'F'),
        ('3', '&'),
        ('9', 'p'),
        ('[', 'G'),
        ('i', 'X'),
        (',', '\x7f'),
        ('@', 'b'),
        ('D', 'q'),
        (' ', "'"),
        (']', 'a'),
        ('R', ' '),
        ('S', 'o'),
        ('a', '|'),
        ('|', ':'),
        ('t', '^'),
        ('>', '`'),
        ('Q', '0'),
        ('B', '"'),
        ('{', 'B'),
        ('g', '2'),
        ('W', 'J'),
        ('A', '\\'),
        ('Y', 'R'),
        ('(', ','),
        ('X', '*'),
        ('\\', 'v'),
        ('T', '8'),
        ('+', '7'),
        ('O', '-'),
        ('b', 'Z'),
        ('#', '#'),
        ('f', '{'),
        ('/', '1'),
        (';', 'I'),
        ('c', 'K'),
        ('n', '%'),
        ('k', '_'),
        ('=', '@'),
        ('r', '.'),
        ('5', ';'),
        ('}', 'U'),
        ('.', 'S'),
        ('$', '!'),
        ('^', 'g'),
        ('u', 'A'),
        ('J', '9'),
        ('&', 'f'),
        ('L', 'M'),
        ('v', ')'),
        ('G', '['),
        ('y', '?'),
        ('l', 'P'),
        ('%', 'z'),
        ('o', '6'),
        ('7', 'H'),
        ('q', 'i'),
        (':', 'e'),
        ('"', 'j'),
        ('h', 'Y'),
        ('z', 'N'),
        ('M', '3'),
        ('\x7f', 'l'),
        ('V', '4'),
        ('!', '('),
        ('j', '~'),
        ('<', 'L'),
        ('E', 'h'),
        ('U', 'x'),
        ('w', '>'),
        ('e', 'k'),
        ('8', 'm'),
        ('?', 'T'),
        ('2', 'E'),
        ('N', '<'),
        ('`', 'V'),
        ('p', 't'),
        ('0', 'w'),
        ('m', 'O'),
        ('C', 's'),
        ('6', 'W'),
        ('x', '$'),
        ('H', '+'),
        ('1', ']'),
        ('-', 'r'),
        ('Z', 'y'),
        ('K', 'n'),
        ('_', 'C'),
        (')', '='),
        ('P', 'd'),
        ('*', 'c'),
        ('~', '5')
    ]

    rotor_2 = [
        ('h', '*'),
        ('c', '>'),
        ('U', 'm'),
        ('&', ']'),
        ('J', 'z'),
        ('/', 'T'),
        (';', '^'),
        ('%', 'I'),
        (',', ')'),
        ('B', '\n'),
        ('\n', 'F'),
        ('9', '_'),
        ('!', '/'),
        ('C', 'y'),
        ('?', 'b'),
        ('S', '\\'),
        ('L', 'g'),
        ('H', 'L'),
        ('w', '\x7f'),
        ('Z', '!'),
        ('m', '<'),
        ('v', 'U'),
        ('P', '-'),
        ('I', '&'),
        ('+', '.'),
        ('<', 'q'),
        ('7', ','),
        ('i', 'D'),
        ('$', 'C'),
        ('u', '0'),
        ('j', '('),
        ('a', 'f'),
        ('Y', 'E'),
        ('W', '}'),
        ('F', 'e'),
        ('|', '~'),
        ('M', ';'),
        ('^', 'V'),
        ('~', 'O'),
        ('p', 'G'),
        ('T', 'S'),
        ('k', 'N'),
        ('3', '+'),
        ('=', '@'),
        ('#', ' '),
        ('O', '9'),
        ('.', '?'),
        ('5', '2'),
        ('t', 'A'),
        ('r', '#'),
        ('R', '1'),
        ('2', 'p'),
        (']', 'o'),
        ("'", ':'),
        ('\\', 'l'),
        ('D', 'Y'),
        ('_', '7'),
        ('(', '8'),
        ('\x7f', '='),
        ('{', 'r'),
        ('>', '`'),
        ('8', 'J'),
        ('`', '"'),
        ('b', '3'),
        ('"', '['),
        ('d', 'v'),
        ('o', 'M'),
        ('-', '6'),
        ('A', 'P'),
        ('*', '5'),
        ('Q', 'h'),
        ('n', '|'),
        ('0', 'B'),
        ('X', 'n'),
        ('E', '%'),
        ('z', 'c'),
        ('l', 'k'),
        ('q', 'Z'),
        (':', 'X'),
        ('g', '$'),
        ('4', 'H'),
        ('K', '{'),
        ('x', 'u'),
        ('f', 'j'),
        ('6', 'w'),
        ('N', 't'),
        (')', 'a'),
        ('y', 'W'),
        ('s', 'K'),
        ('V', 's'),
        ('1', 'x'),
        ('[', 'Q'),
        (' ', "'"),
        ('}', '4'),
        ('@', 'R'),
        ('G', 'd'),
        ('e', 'i')
    ]

    rotor_3 = [
        ('g', 'k'),
        ('<', '\\'),
        ('M', 'D'),
        ('Q', '0'),
        ('G', 'G'),
        ('.', ']'),
        ('!', '<'),
        ('~', 'd'),
        ('"', 'E'),
        ('X', '\n'),
        ('\n', 'Z'),
        (')', '/'),
        ('E', 'r'),
        ("'", 'W'),
        ('R', 'f'),
        ('F', 'y'),
        ('q', 'b'),
        (';', 'q'),
        (',', 'Q'),
        (':', '-'),
        ('?', '#'),
        ('k', '7'),
        ('*', 'P'),
        ('m', '|'),
        ('>', 'm'),
        ('\\', '*'),
        ('{', 'S'),
        ('z', 'l'),
        ('4', '!'),
        ('c', '3'),
        ('U', 'n'),
        ('A', 'i'),
        ('P', '~'),
        ('l', 'V'),
        ('|', ';'),
        ('6', 'j'),
        ('j', '='),
        ('C', '_'),
        ('I', '4'),
        ('e', ')'),
        ('@', 'B'),
        ('D', '"'),
        ('7', '('),
        ('8', 'C'),
        ('(', '2'),
        ('[', 'R'),
        ('n', '.'),
        ('p', 'J'),
        ('\x7f', '&'),
        ('b', '?'),
        ('w', 'e'),
        ('i', "'"),
        ('H', 'z'),
        (' ', ','),
        ('d', '8'),
        ('f', '}'),
        ('=', '`'),
        ('W', 'p'),
        ('$', '$'),
        ('x', '%'),
        ('0', '9'),
        ('u', 'o'),
        ('J', 'v'),
        ('T', 'T'),
        ('+', 'g'),
        ('Y', '+'),
        ('r', '^'),
        ('}', 't'),
        ('5', 'h'),
        ('-', 'X'),
        ('^', ':'),
        ('&', '1'),
        ('V', 'Y'),
        (']', '6'),
        ('K', 'U'),
        ('y', '{'),
        ('1', 'c'),
        ('s', 'x'),
        ('%', '@'),
        ('v', 'M'),
        ('L', '>'),
        ('o', 'K'),
        ('3', 'A'),
        ('h', 'u'),
        ('#', 'F'),
        ('/', 'w'),
        ('9', 'a'),
        ('Z', 's'),
        ('a', 'N'),
        ('2', 'I'),
        ('N', '5'),
        ('_', 'H'),
        ('S', 'O'),
        ('`', ' '),
        ('t', '['),
        ('O', '\x7f'),
        ('B', 'L')
    ]

    reflector = [
        ('s', 'q'),
        ('C', ','),
        ("'", 'b'),
        ('#', 't'),
        ('X', '['),
        ('I', 'Q'),
        ('p', '3'),
        (';', 'y'),
        ('N', '$'),
        ('[', '6'),
        ('+', '2'),
        ('L', '~'),
        ('4', ']'),
        ('!', '`'),
        ('6', '='),
        ('i', '.'),
        ('_', 's'),
        ('%', '/'),
        ('M', '#'),
        ('0', 'O'),
        ('3', 'r'),
        ('8', 'W'),
        (':', 'o'),
        ('=', 'c'),
        ('U', '%'),
        ('^', 'a'),
        (']', ':'),
        ('c', 'Z'),
        ('y', 'j'),
        ('n', '\n'),
        ('\n', 'w'),
        ('Z', '<'),
        ('j', 'A'),
        ('R', 'e'),
        ('m', 'L'),
        ('7', '&'),
        ('K', '('),
        ('|', 'J'),
        ('w', 'm'),
        ('"', '\\'),
        ('g', '_'),
        ('l', '?'),
        ('Q', 'N'),
        ('x', 'U'),
        ('r', '}'),
        ('{', 'g'),
        ('`', 'V'),
        ('T', '|'),
        ('>', '{'),
        ('O', 'X'),
        ('V', 'h'),
        ('B', 'M'),
        ('t', 'z'),
        ('<', 'u'),
        ('a', '4'),
        ('S', 'C'),
        ('b', 'D'),
        ('?', '!'),
        ('f', 'H'),
        ('&', 'k'),
        ('d', 'I'),
        ('}', '*'),
        ('H', '5'),
        ('v', 'S'),
        ('D', "'"),
        ('(', 'Y'),
        (' ', ';'),
        ('F', 'G'),
        ('G', '7'),
        ('@', '"'),
        ('~', 'F'),
        ('1', 'E'),
        ('9', '\x7f'),
        ('\\', ')'),
        ('A', 'l'),
        ('k', 'd'),
        ('u', 'T'),
        ('E', '-'),
        (')', '8'),
        ('\x7f', 'v'),
        ('W', 'K'),
        (',', 'x'),
        ('h', ' '),
        ('Y', 'P'),
        ('J', '>'),
        ('*', '1'),
        ('5', 'R'),
        ('2', '^'),
        ('z', 'B'),
        ('q', 'n'),
        ('/', 'p'),
        ('e', 'i'),
        ('.', '+'),
        ('$', 'f'),
        ('o', '@'),
        ('P', '9'),
        ('-', '0')
    ]

    def __init__(self, key):
        self.rotors = (self.rotor_1, self.rotor_2, self.rotor_3)

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
