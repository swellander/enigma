from random import randrange


class Enigma(object):
    num_potential_chars = 128

    def __generate_random_ascii_char_list(self) -> list:
        """
        Returns a list of ASCII character strings in a randomized order.
        Used for creating rotors.
        """

        ordered_list_of_chars = [chr(i)
                                 for i in range(self.num_potential_chars)]
        rand_list_of_chars = []

        for _ in range(self.num_potential_chars):
            j = randrange(len(ordered_list_of_chars))
            char = ordered_list_of_chars[j]
            rand_list_of_chars.append(char)
            ordered_list_of_chars.remove(char)

        return rand_list_of_chars

    def __generate_rotor(self) -> list:
        """
        Returns a list of tuples representing an enigma rotor,
        where the first value of the tuple is the input and the
        second value is the output. https://en.wikipedia.org/wiki/Enigma_rotor_details
        """
        front = self.__generate_random_ascii_char_list()
        back = self.__generate_random_ascii_char_list()
        rotor = []

        for i in range(self.num_potential_chars):
            rotor.append((
                front[i],
                back[i],
            ))

        return rotor
