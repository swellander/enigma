from random import randrange


class Enigma(object):

    def __generate_random_ascii_char_list(self) -> list:
        """
        Returns a list of ASCII character strings in a randomized order.
        Used for creating scramblers.
        """

        ordered_list_of_chars = [chr(i)
                                 for i in range(127)]  # ASCII codes 0-127
        rand_list_of_chars = []

        for _ in range(127):
            j = randrange(len(ordered_list_of_chars))
            char = ordered_list_of_chars[j]
            rand_list_of_chars.append(char)
            ordered_list_of_chars.remove(char)

        return rand_list_of_chars
