import random
from .config import GAConfig

MINIMUM = -3
MAXIMUM = 3

def generate_random_bit_string(config: GAConfig) -> str:
    """
    Creates a random chromosome using the configuration passed to it
    Output:
        str: binary number stored in string
    """
    seed = config.seed
    bits = config.bit_length
    if seed != None:
        random.seed(seed)
    bit_string = ""
    for i in range(bits):
        # generates a random integer between 0 and 1 (inclusive)
        # appends it to the string
        bit_string += str(random.randint(0, 1))
    return bit_string


def decode(bit_string: str) -> int:
    # converts the string of binary to integer base 10
    return int(bit_string, 2)


def encode(number: int) -> str:
    # converts an integer into a binary string
    return format(number, 'b')


def convert_to_range(num: int, bit_length: int, minimum: int, maximum: int) -> float:
    # scales an integer into a different range
    scaling_factor = (maximum - minimum) / ((2 ** bit_length) - 1)
    return (num * scaling_factor) - maximum

def bit_to_num_pipeline(chromosome: str) -> float:
    """
    Converts a chromosome into its corresponding floating point conversion
    Input:
        chromosome: chromosome that is a stringified binary
    Output:
        float: floating point number in the range that is specified
    """
    num = decode(chromosome)
    return convert_to_range(num, len(chromosome), MINIMUM, MAXIMUM)
