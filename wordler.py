import re

import click


f_str = "/usr/share/dict/words"


def get_5_letter_words():
    with open(f_str, "r") as f:
        dict_words = f.read().splitlines()
    dict_words_5 = [x.lower() for x in dict_words if len(x) == 5]

    return dict_words_5


def get_potential_words(potentials, fixed, variable, used):
    if fixed:
        regex_str = fixed.lower().replace("*", ".")
        potentials = [x for x in potentials if re.match(regex_str, x)]

    if variable:
        potentials = [
            x for x in potentials if all(y in x for y in list(variable.lower()))
        ]

    if used:

        # remove letters already defined under -v and  -f
        used = used.lower()

        intersect_set1 = set(list(used.lower())) & set(list(fixed.lower()))
        if variable:
            intersect_set2 = set(list(used.lower())) & set(list(variable.lower()))
            intersect_set = intersect_set2 | intersect_set1
        else:
            intersect_set = intersect_set1
            
        used_ls = list(used)
        print(intersect_set, used_ls)
        if intersect_set:
            for x in intersect_set:
                used_ls.remove(x)
            print(used_ls)
            used = ''.join(used_ls)


        potentials = [
            x for x in potentials if not any(y in x for y in list(used.lower()))
        ]


    return potentials


def print_potentials(potentials):
    for word in potentials:
        print(word)
    print("\n\nLength of potentials: ", len(potentials))


def main(fixed, variable, used):
    print(f"Fixed {fixed}, Variable {variable} \n\n")
    dict_words_5 = get_5_letter_words()
    potentials = get_potential_words(dict_words_5, fixed, variable, used)
    print_potentials(potentials)


@click.command()
@click.option("--fixed", "-f", help="Text used to separate numbers (default: \\n)")
@click.version_option(version="1.0.0")
@click.option("--variable", "-v", help="Text used to separate numbers (default: \\n)")
@click.option("--used", "-u", help="Text used to separate numbers (default: \\n)")
def cmd_entry(used, variable, fixed):
    main(fixed, variable, used)


if __name__ == "__main__":
    cmd_entry()
