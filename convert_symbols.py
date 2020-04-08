from abc import ABC, abstractmethod
import pyperclip
import time
import re

# Seconds to wait between checking if watched files were saved
WATCH_CHECK_DELAY_SECONDS = 1

# List of active replacements
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

class Command(ABC):
    """
    Defines commands to be used in the CLI.
    
    Parameters
    ----------
    name:           used to recognize this command, first token of userInput
                        (ex. '/watch')
    index:          calling `/help` sorts the CLI's commands ordered by this
                        value
    syntax:         user-facing syntax of each command
    effect:         user-facing description of what the command does
    reSyntax:       regex to determine if the command is valid and executable
    reErrorMessage: if the first token of the userInput matches the command
                        name the whole string fails re.match against reSyntax,
                        then calling execute(userInput) prints this string
    """
    def __init__(self, name, index, syntax, effect, reSyntax, reErrorMessage):
        super(Command, self).__init__()
        self.name = name
        self.index = index
        self.syntax = syntax
        self.effect = effect
        self.reSyntax = reSyntax
        self.reErrorMessage = reErrorMessage

    @abstractmethod
    def execute(self, userInput):
        pass

class ReplacementsCmd(Command):
    """Shows a list of active text replacements."""
    name = '/replacements'
    index = 0
    syntax = '/replacements'
    effect = 'Shows a list of active text replacements.'
    reSyntax = '^/replacements$'
    reErrorMessage = 'Incorrect usage.'

    def __init__(self):
        super(ReplacementsCmd, self).__init__(
            ReplacementsCmd.name, 
            ReplacementsCmd.index, 
            ReplacementsCmd.syntax, 
            ReplacementsCmd.effect, 
            ReplacementsCmd.reSyntax, 
            ReplacementsCmd.reErrorMessage
        )

    def execute(self, userInput):
        pass # TODO

class AddCmd(Command):
    """Adds a shortcut to the list of active text replacements."""
    name = '/add'
    index = 1
    syntax = '/add shortcut->symbol [shortcut->symbol ...]'
    effect = 'Adds a shortcut to the list of active text replacements.'
    reSyntax = '^/add[ .*->.*]+$'
    reErrorMessage = 'Incorrect usage.'
    
    def __init__(self):
        super(AddCmd, self).__init__(
            AddCmd.name, 
            AddCmd.index, 
            AddCmd.syntax, 
            AddCmd.effect, 
            AddCmd.reSyntax, 
            AddCmd.reErrorMessage
        )
    
    def execute(self, userInput):
        pass # TODO

class WatchCmd(Command):
    """Starts a background process to watch for changes to .txt files."""
    name = '/watch'
    index = 100
    syntax = '/watch [-c] filename.txt [filename.txt ...]'
    effect = ('Starts a background process to watch for changes to the given '
             'file(s). If the -c flag is incldued then saving the specified '
             'files copies the converted text to the clipboard (checks for an '
             'update every second).')
    reSyntax = '^/watch[ -c]?[ .*.txt]+$'
    reErrorMessage = 'Incorrect usage (only .txt files supported).'
    
    def __init__(self):
        super(WatchCmd, self).__init__(
            WatchCmd.name, 
            WatchCmd.index, 
            WatchCmd.syntax, 
            WatchCmd.effect, 
            WatchCmd.reSyntax, 
            WatchCmd.reErrorMessage
        )

    def execute(self, userInput):
        pass # TODO

class KillWatchCmd(Command):
    """Stops watching the given filenames."""
    name = '/killwatch'
    index = 200
    syntax = '/killwatch [filename.txt ...]'
    effect = ('Stops watching the provided filename. If no filenames are '
             'provided then all active filewatchers are stopped.')
    reSyntax = '^/killwatch[ [a-zA-Z0-9].txt]*$'
    reErrorMessage = f'Incorrect usage. Syntax: {syntax}'
    
    def __init__(self):
        super(KillWatchCmd, self).__init__(
            KillWatchCmd.name, 
            KillWatchCmd.index, 
            KillWatchCmd.syntax, 
            KillWatchCmd.effect, 
            KillWatchCmd.reSyntax, 
            KillWatchCmd.reErrorMessage
        )
    
    def execute(self, userInput):
        pass # TODO

class ExitCmd(Command):
    """Kills all filewatchers and ends the program."""
    name = '/exit'
    index = 9900
    syntax = '/exit'
    effect = 'Kills any filewatchers and ends the program.'
    reSyntax = '^/stop$'
    reErrorMessage = f'Incorrect usage. Syntax: {syntax}'
    
    def __init__(self):
        super(ExitCmd, self).__init__(
            ExitCmd.name, 
            ExitCmd.index, 
            ExitCmd.syntax, 
            ExitCmd.effect, 
            ExitCmd.reSyntax, 
            ExitCmd.reErrorMessage
        )
    
    def execute(self, userInput):
        pass # TODO

class HelpCmd(Command):
    """Shows a help dialog to the user."""
    name = '/help'
    index = 10000
    syntax = '/help'
    effect = 'Shows this help dialog.'
    reSyntax = '^/help$'
    reErrorMessage = f'Incorrect usage. Syntax: {syntax}'
    
    def __init__(self):
        super(HelpCmd, self).__init__(
            HelpCmd.name, 
            HelpCmd.index, 
            HelpCmd.syntax, 
            HelpCmd.effect, 
            HelpCmd.reSyntax, 
            HelpCmd.reErrorMessage
        )

    def execute(self, userInput):
        pass # TODO

class CLI:
    """Sets up a Command Line Interface."""
    def __init__(self, commands, SUFFIX='\n>>> '):
        # TODO: Create a list of command objects that can be looped through each
        #       time user enters input to check if it matches the reSyntax of
        #       any command
        # TODO: Take 'preset=None' as parameter, make ReplacementsManager class
        #       to cherry pick replacements, and create class variable (dict)
        #       that creates ReplacementsManagers for each preset
        self.commands = commands

    def cmdLoop():
        # TODO: All of this
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
                # No user input, handle somehow
                pass

            cont = False # TODO: Remove after this won't be infinite loop

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

\tv2.0 by Jackson Hall
''')

"""Convert the given str expression using the shortcuts in REPLACEMENTS."""
def convert_symbols(expression):
    converted_expression = expression

    for i in REPLACEMENTS:
        converted_expression = converted_expression.replace(i, REPLACEMENTS[i])

    return converted_expression

"""If s matches the reSyntax for a command in COMMANDS, return what command, else False."""
def get_command(s):
    for command in COMMANDS:
        if re.match(command['reSyntax'], command):
            return command

    return False

def main():
    welcome()

    cli = CLI([
        ReplacementsCmd(),
        AddCmd(),
        WatchCmd(),
        KillWatchCmd(),
        ExitCmd(),
        HelpCmd(),
    ])

    print('Nothing to see here yet...')


    # --------
    # OLD CODE
    # --------
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
