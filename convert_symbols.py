import pyperclip
import time
import re

REPLACEMENTS = {
    '===': '≡',     # Logically equivalent
    '!=': '≠',      # Is not equal
    '...': '∴',     # Therefore
    'EE': '∃',      # There exists
    'AA': '∀',      # For all
    '<->': '↔',     # Iff 
    '->': '→',      # Implies
    '=>': '⇒',      # Implies/equals
    '~ee': '∉',     # Is not an element of 
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

COMMANDS = {
    '/replacements': {
        'index':    0, # TODO: Sort commands by this value when displayed using /help
        'syntax':   '/replacements'
        'effect':   'Shows a list of active text replacements.'
        'reSyntax': '^/replacements$'
        'reErrMsg': f'Incorrect usage. Syntax: {COMMANDS['/replacements']['syntax']}'
    },
    '/add': {
        'index':    1,
        'syntax':   '/add shortcut->symbol[ shortcut->symbol ...]',
        'effect':   'Adds a shortcut to the list of active text replacements.',
        'reSyntax': '^/add[ ]->[*]$'
    }
    '/watch': {
        'index':    100,
        'syntax':   '/watch [-c] filename.txt[ filename.txt ...]',
        'effect':   'Starts a background process to watch for changes to the given file(s). If the '
                    '-c flag is incldued then saving the specified files copies the converted text '
                    'to the clipboard (checks for an update every second).',
        'reSyntax': '^/watch[ -c]?[ [a-zA-Z0-9_]+.txt]+$',
        'reErrMsg': f'Incorrect usage (only .txt files supported). Syntax: {COMMANDS['/watch']['syntax']}',
    },
    '/killwatch': {
        'index':    200,
        'syntax':   '/killwatch [filename.txt[ filename.txt ...]]',
        'effect':   'Stops watching the provided filename. If no files are provided then all '
                    'filewatchers are stopped.',
        'reSyntax': '^/killwatch[ [a-zA-Z0-9].txt]*$',
        'reErrMsg': f'Incorrect usage. Syntax: {COMMANDS['/killwatch']['syntax']}',
    },
    '/stop': {
        'index':    9900,
        'syntax':   '/stop',
        'effect':   'Kills any filewatchers and ends the program.',
        'reSyntax': '^/stop$',
        'reErrMsg': f'Incorrect usage. Syntax: {COMMANDS['/stop']['syntax']}',
    },
    '/help': {
        'index':    10000,
        'syntax':   '/help',
        'effect':   'Shows this help dialog.',
        'reSyntax': '^/help$',
        'reErrMsg': f'Incorrect usage. Syntax: {COMMANDS['/watch']['syntax']}',
    }
}

WATCH_CHECK_DELAY_SECONDS = 1

"""Print a welcome message when the program runs."""
def welcome():
    print('''
 _____                 _           _   _____                           _
/  ___|               | |         | | /  __ \                         | |
\ `--. _   _ _ __ ___ | |__   ___ | | | /  \/ ___  _ ____   _____ _ __| |_ ___ _ __
 `--. \ | | | '_ ` _ \| '_ \ / _ \| | | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
/\__/ / |_| | | | | | | |_) | (_) | | | \__/\ (_) | | | \ V /  __/ |  | ||  __/ |
\____/ \__, |_| |_| |_|_.__/ \___/|_|  \____/\___/|_| |_|\_/ \___|_|   \__\___|_|
        __/ |
       |___/

\tv1.0 by Jackson Hall
''')

"""Convert the given str expression using the shortcuts in REPLACEMENTS."""
def convert_symbols(expression):
    converted_expression = expression

    for i in REPLACEMENTS:
        converted_expression = converted_expression.replace(i, REPLACEMENTS[i])

    return converted_expression

"""If s matches the reSyntax for a command in COMMANDS, return what command, else False."""
def get_command(s->str):
    for command in COMMANDS:
        if re.match(command['reSyntax'], command):
            return command

    return False

def main():
    welcome()

    # Loop while user wants to continue
    cont = True
    while cont:
        userInput = input('Enter text to convert, or type "/help" for more info: ').lower().strip()

        # Filter blank input
        if userInput:
            command = get_command(userInput)

            if command:
                # Execute the command
                pass
            else:
                # Convert symbols, print result, copy to clipboard
                pass
        else:
            # No user input, handle accordingly
            pass



    # expression = None
    # while expression != 'done':
    #     expression = input('Enter text to convert: ')
    #     command = get_command(expression)

    #     # Show list of replacements
    #     if expression.lower() == 'help':
    #         print('\tAvailable replacements:')
    #         print('\t-----------------------')

    #         for shortcut in REPLACEMENTS:
    #             # Don't print blank lines
    #             if shortcut != '':
    #                 print(f'\t\t{shortcut} : {REPLACEMENTS[shortcut]}')

    #         print()

    #         # Reprompt for expression
    #         continue

    #     # If user hits enter, use data from convert_symbols.txt
    #     if expression == '':
    #         try:
    #             with open('convert_symbols.txt', 'r') as file:
    #                 expression = file.read()
    #         except IOError:
    #             print('Sorry, convert_symbols.txt doesn\'t exist or can\'t be opened.\n')
    #             continue

    #     # Convert the symbols
    #     converted_expression = convert_symbols(expression)

    #     # Copy result to clipboard
    #     pyperclip.copy(converted_expression)

    #     # Show user converted symbols
    #     # If there are multiple lines, indent each
    #     for line in converted_expression.split('\n'):
    #         print('\t' + line)

    #     print('\n\t' + 'Copied!')

    #     # Pause before new prompt
    #     time.sleep(1)
    #     print()

if __name__ == '__main__':
    main()
