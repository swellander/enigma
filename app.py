from random import randrange


class Enigma(object):

    num_potential_chars = 95

    def __init__(self):
        rotor_1 = self.__generate_rotor()
        rotor_2 = self.__generate_rotor()
        rotor_3 = self.__generate_rotor()
        self.reflector = self.__generate_rotor()
        self.rotors = (rotor_1, rotor_2, rotor_3)

    def encrypt_text(self, text: str) -> str:
        encrypted_text = ''
        for char in text:
            encrypted_char = self.__encrypt_char(char)
            encrypted_text += encrypted_char

        return encrypted_text

    def decrypt_text(self, text: str) -> str:
        decrypted_text = ''
        for char in text:
            decrypted_text += self.__decrypt_char(char)

        return decrypted_text

    def __encrypt_char(self, char) -> str:
        """
        Pass character forward through rotors.
        """

        return self.__process_char(char)

    def __decrypt_char(self, char) -> str:
        """
        Pass character backward through rotors.
        """

        return self.__process_char(char, reflected=True)

    def __process_char(self, char, reflected=False):
        """
        Passes a character through rotors, changing its value
        for each rotor.
        """

        for rotor in self.rotors:
            char = self.__convert_char(char=char, rotor=rotor)

        char = self.__convert_char(
            char=char, rotor=self.reflector, reflected=reflected)

        for rotor in self.rotors[::-1]:
            char = self.__convert_char(char=char, rotor=rotor, reflected=True)

        return char

    def __convert_char(self, char=None, rotor=None, reflected=False):
        front = 1 if reflected else 0
        back = 0 if reflected else 1

        for mapping in rotor:
            if mapping[front] == char:
                output_char = mapping[back]
                if not output_char:
                    import pdb
                    pdb.set_trace()
                return output_char

    def __generate_random_ascii_char_list(self) -> list:
        """
        Returns a list of ASCII character strings in a randomized order.
        Used for creating rotors.
        """

        ordered_list_of_chars = [chr(i)
                                 for i in range(32, 128) if chr(i)]
        num_potential_chars = len(ordered_list_of_chars)
        rand_list_of_chars = []

        for _ in range(num_potential_chars):
            try:
                j = randrange(len(ordered_list_of_chars))
            except ValueError:
                import pdb
                pdb.set_trace()
            char = ordered_list_of_chars[j]
            rand_list_of_chars.append(char)
            ordered_list_of_chars.remove(char)

        return rand_list_of_chars

    def __generate_rotor(self) -> list:
        """
        Returns a list of tuples representing an enigma rotor,
        where the first value of the tuple is the input (front) and the
        second value is the output (back). https://en.wikipedia.org/wiki/Enigma_rotor_details
        """

        front = self.__generate_random_ascii_char_list()
        back = self.__generate_random_ascii_char_list()
        rotor = []

        for i in range(len(front)):
            try:
                rotor.append((
                    front[i],
                    back[i],
                ))
            except:
                import pdb
                pdb.set_trace()

        return rotor
