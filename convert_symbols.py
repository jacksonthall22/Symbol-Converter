import pyperclip
import time

REPLACEMENTS = {
    '===': '≡',     # Logically equivalent
    '!=': '≠',      # Is not equal
    '...': '∴',     # Therefore
    'EE': '∃',      # There exists
    'AA': '∀',      # For all
    '<->': '↔',     # Iff 
    '->': '→',      # Implies
    '=>': '⇒',      # Implies/equals
    '~ee': '∉',     # Is an element of 
    'ee': '∈',      # Is an element of 
    '!': '~',       # Not
    '/\\': '∧',     # And
    '\\/': '∨',     # Or
    'xor': '⊕',     # Xor
    '_0': '°',      # Degrees
    'UU': '𝕌',      # Universal set
    'RR': 'ℝ',      # Real numbers
    'QQ': 'ℚ',      # Rational numbers
    'ZZ': 'ℤ',      # Integers
    'NN': 'ℕ',      # Natural numbers
    'pi': 'π',      # Pi
    '>=': '≥',      # Greater than or equal to
    '<=': '≤',      # Less than or equal to
    '\\sub': '⊆',   # Is a subset of
    '\\sup': '⊇',   # Is a superset of
    '\\psub': '⊊',  # Is a proper subset of
    '\\nsub': '⊄',  # Not a subset
    '\\nsup': '⊅',  # Not a superset
    'uu': '∪',      # Union
    'nn': '∩',      # Intersection
    '': '',         # 
}

def convert_symbols(expression):
    converted_expression = expression

    for i in REPLACEMENTS:
        converted_expression = converted_expression.replace(i, REPLACEMENTS[i])

    return converted_expression

def welcome():
    print("""
 _                 _        _____                 _           _   _____                           _            
| |               (_)      /  ___|               | |         | | /  __ \                         | |           
| |     ___   __ _ _  ___  \ `--. _   _ _ __ ___ | |__   ___ | | | /  \/ ___  _ ____   _____ _ __| |_ ___ _ __ 
| |    / _ \ / _` | |/ __|  `--. \ | | | '_ ` _ \| '_ \ / _ \| | | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
| |___| (_) | (_| | | (__  /\__/ / |_| | | | | | | |_) | (_) | | | \__/\ (_) | | | \ V /  __/ |  | ||  __/ |   
\_____/\___/ \__, |_|\___| \____/ \__, |_| |_| |_|_.__/ \___/|_|  \____/\___/|_| |_|\_/ \___|_|   \__\___|_|   
              __/ |                __/ |                                                                       
             |___/                |___/                                                                        

\tv1.0 by Jackson Hall
""")

def main():
    welcome()

    # Loop while user wants to continue
    expression = None

    while expression != 'done':
        expression = input('Enter text to convert: ')

        # Show list of replacements
        if expression.lower() == 'help':
            print('\tAvailable replacements:')
            print('\t-----------------------')

            for shortcut in REPLACEMENTS:
                # Don't print blank lines
                if shortcut != '':
                    print(f'\t\t{shortcut} : {REPLACEMENTS[shortcut]}')

            print()

            # Reprompt for expression
            continue

        # If user hits enter, use data from convert_symbols.txt
        if expression == '':
            try:
                with open('convert_symbols.txt', 'r') as file:
                    expression = file.read()
            except IOError:
                print('Sorry, convert_symbols.txt doesn\'t exist or can\'t be opened.\n')
                continue

        # Convert the symbols
        converted_expression = convert_symbols(expression)

        # Copy result to clipboard
        pyperclip.copy(converted_expression)

        # Show user converted symbols
        # If there are multiple lines, indent each
        for line in converted_expression.split('\n'):
            print('\t' + line)

        print('\n\t' + 'Copied!')

        # Pause before new prompt
        time.sleep(1)
        print()

if __name__ == '__main__':
    main()
