import re
import itertools as it
import click

f_str = '/usr/share/dict/words'
def get_5_letter_words():
    with open(f_str, 'r') as f:
        dict_words = f.read().splitlines()
    dict_words_5 = [x.lower() for x in dict_words if len(x) == 5]
    print(len(dict_words_5))
    return dict_words_5

def main(fixed, variable):    
    dict_words_5 = get_5_letter_words()
    potentials = basic(dict_words_5, fixed, variable )
    print_potentials(potentials)

 
def create_regex_str(fixed, variable):

    # '*A*IT'
    if fixed:
        for indx, val in enumerate(fixed):
            print(indx, val)

        fixed = fixed.lower().replace('*', '.')
        len_fixed_chars = len(fixed) - fixed.count('*')
    else:
        len_fixed_chars = 5  # no fixed chars

    if variable:

        product_vals = list(set(list(it.product(variable.lower() + '.', repeat=len_fixed_chars))))
        print(product_vals)

        ls_vals = [''.join(x) for x in product_vals]
        print(ls_vals)

    ls_vals.append(fixed)
    print(ls_vals)







    ls = [x for x in list(set(list(it.combinations_with_replacement('CAT.', 5)))) if  all((c in chars) for c in ''.join(x))]
    return ls_vals

def basic(dict_words_5, fixed, variable):
    # Test *A*IT->Tacit
    regex_str_ls = create_regex_str(fixed, variable)
    #fudge
    # regex_str = r'''.a.it'''
    potentials = []
    for regex_str in regex_str_ls:
        potentials.extend([x for x in dict_words_5 if re.match(regex_str, x)])
    return potentials

def print_potentials(potentials):
    for word in potentials:
        print(word)

@click.command()
@click.option("--fixed", "-f",
              help="Text used to separate numbers (default: \\n)")
@click.version_option(version="1.0.0")
@click.option("--variable", "-v",
              help="Text used to separate numbers (default: \\n)")
def seq(variable, fixed):
   
    main(fixed, variable)
 
if __name__ == "__main__":
    fixed, variable = seq()
 
 
 