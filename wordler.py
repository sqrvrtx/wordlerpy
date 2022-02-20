import re
import itertools as it
import click

f_str = "/usr/share/dict/words"


def get_5_letter_words():
    with open(f_str, "r") as f:
        dict_words = f.read().splitlines()
    dict_words_5 = [x.lower() for x in dict_words if len(x) == 5]

    return dict_words_5


def main(fixed, variable):
    dict_words_5 = get_5_letter_words()
    potentials = basic(dict_words_5, fixed, variable)
    print_potentials(potentials)


def create_regex_str(fixed, variable):
    if fixed:
        fixed = fixed.lower().replace("*", ".")
        len_fixed_chars = len(fixed) - fixed.count("*")
    else:
        len_fixed_chars = 5  # no fixed chars

    return fixed


def basic(potentials, fixed, variable):
    # Test *A*IT->Tacit
    print(f"Fixed {fixed}, Variable {variable}")
    if fixed:
        regex_str = create_regex_str(fixed, variable)
        potentials = [x for x in potentials if re.match(regex_str, x)]

    if variable:
        potentials = [
            x for x in potentials if all(y in x for y in list(variable.lower()))
        ]

    return potentials


def print_potentials(potentials):
    for word in potentials:
        print(word)
    print("Length of potentials: ", len(potentials))


@click.command()
@click.option("--fixed", "-f", help="Text used to separate numbers (default: \\n)")
@click.version_option(version="1.0.0")
@click.option("--variable", "-v", help="Text used to separate numbers (default: \\n)")
def seq(variable, fixed):
    main(fixed, variable)


if __name__ == "__main__":
    fixed, variable = seq()
