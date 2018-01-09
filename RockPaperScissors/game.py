#Imports
import random
import os

# 0 = Rock, 1 = Paper, 2 = Scissors
__results = {(0, 0): 'Draw', (0, 1): 'Computer Wins (Paper covers rock)',
(0, 2): 'You Win! (Rock smashes Scissors)', (1, 0): 'You Win! (Paper covers rock)',
(1, 1): 'Draw', (1, 2): 'Computer Wins (Scissors cut paper)',
(2, 0): 'Computer Wins (Rock smashes Scissors)',
(2, 1): 'You win! (Scissors cut paper)', (2, 2): 'Draw'}

def clearScreen():
    unused_var = os.system('cls')   # Windows

# Response Variables and Functions =============================================

#The valid response lists should be private
__main_reponses = ['Start', 'Help', 'Quit', 's', 'S', 'start', 'START', 'h', 'H',
'help', 'HELP', 'q', 'Q', 'quit', 'QUIT']

__game_responses = ['Rock', 'Paper', 'Scissors', 'r', 'R', 'p', 'P', 's', 'S',
'rock', 'ROCK', 'paper', 'PAPER', 'scissors', 'scissor', 'Scissor', 'SCISSOR',
'SCISSORS', 'q', 'Q', 'quit', 'Quit', 'QUIT']

def CheckMainReponse(string):
    """Check if the parameter string is a valid response in the main menu"""
    for response in __main_reponses:
        if response == string:
            if response[0] == 's' or response[0] == 'S':
                return 0
            elif response[0] == 'h' or response[0] == 'H':
                return 1
            else: return -1
    return 2

def CheckGameResponse(string):
    """Checks if the parameter string is valid response during the game"""
    for response in __game_responses:
        if response == string:
            if response[0] == 'r' or response[0] == 'R':
                return 0
            elif response[0] == 'p' or response[0] == 'P':
                return 1
            elif response[0] == 's' or response[0] == 'S':
                return 2
            else: return -1
    return 3

# Game Stat Variables and  Functions ==========================================
class Data:
    def __init__(self):
        self.r_count, self.p_count, self.s_count = 0, 0, 0
        self.w_count, self.d_count, self.l_count = 0, 0, 0
    def getChoicePercentages():
        pass
    def getWDLPercentages():
        pass
human = Data()
computer = Data()

def updateStats(game_result):
    """Updates the statistics about the human and computer, and returns a string response about the winnner"""
    human_choice, computer_choice = game_result # Get the results

    # Update the choice counts
    if human_choice == 0:
        human.r_count += 1
    elif human_choice == 1:
        human.p_count += 1
    else:
        human.s_count += 1
    if computer_choice == 0:
        computer.r_count += 1
    elif computer_choice == 1:
        computer.p_count += 1
    else:
        computer.s_count += 1

    # Update the WDL counts
    winner = __results[(human_choice, computer_choice)]
    if winner[0] == 'Y':
        human.w_count += 1
        computer.l_count += 1
    elif winner[0] == 'C':
        human.l_count += 1
        computer.w_count += 1
    else:
        human.d_count += 1
        computer.d_count += 1

    return winner # Return the string for the win response


def viewStats():
    """Shows statistics about the session"""
    #Choice Counts, Choices Means, Win/Draw/Loss Counts, Win/Draw/Loss Percentages
    pass


# The Rock, Paper, Scissors Game ==============================================

def Run():
    """The main method that runs the game"""
    while True:
        computer_index = random.randint(0, 2)

        human_index = CheckGameResponse(input('Type your choice: Rock, Paper, or Scissors -->  '))
        if human_index > 2:
            print('Not a valid choice. Try again ...')
            continue
        elif human_index < 0:
            break;

        tup = human_index, computer_index
        print("\t{0:8} vs. {1:8}\n".format(__game_responses[human_index].rjust(8), __game_responses[computer_index]))

        print(updateStats(tup))
        print('\n\n')

# Main Menu ===================================================================
def printMainMenu():
    """Prints the Main Menu"""
    clearScreen()
    print('\n       Welcome to the Rock, Paper, Scissors game!')
    print('    You will be challenging the computer for this game\n')
    print('\tType "Start" or "s" to start a new game')
    print(' Type "help" or "h" to see all the options and settings')
    print('     Type "quit" or "q" at anytime to exit the game\n\n')

if __name__ == '__main__':
    printMainMenu()

    choice = 0
    while choice >= 0:
        choice = CheckMainReponse(input('-->  '))

        if choice < 0: #Quit
            continue
        elif choice > 1:
            print('Invalid option. Try again ...')
        elif choice == 0:
            Run()
            printMainMenu()
        elif choice == 1:
            # Help Stuff
            pass

    print('Exiting the game')
