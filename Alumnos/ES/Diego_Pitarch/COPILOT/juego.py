import random

# Initialize counters
rock_wins = 0
paper_wins = 0
scissors_wins = 0
lizard_wins = 0
spock_wins = 0
rock_losses = 0
paper_losses = 0
scissors_losses = 0
lizard_losses = 0
spock_losses = 0
ties = 0

# Define the game function
def juego():
    global rock_wins, paper_wins, scissors_wins, lizard_wins, spock_wins, rock_losses, paper_losses, scissors_losses, lizard_losses, spock_losses, ties
    jugada1 = random.randint(1, 5)  # Random choice for the first machine
    jugada2 = random.randint(1, 5)  # Random choice for the second machine
    if jugada1 == jugada2:
        ties += 1
    elif (jugada1 == 1 and jugada2 in [3, 4]) or (jugada1 == 2 and jugada2 in [1, 5]) or (jugada1 == 3 and jugada2 in [2, 4]) or (jugada1 == 4 and jugada2 in [2, 5]) or (jugada1 == 5 and jugada2 in [1, 3]):
        if jugada1 == 1:
            rock_wins += 1
        elif jugada1 == 2:
            paper_wins += 1
        elif jugada1 == 3:
            scissors_wins += 1
        elif jugada1 == 4:
            lizard_wins += 1
        elif jugada1 == 5:
            spock_wins += 1
        if jugada2 == 1:
            rock_losses += 1
        elif jugada2 == 2:
            paper_losses += 1
        elif jugada2 == 3:
            scissors_losses += 1
        elif jugada2 == 4:
            lizard_losses += 1
        elif jugada2 == 5:
            spock_losses += 1
    else:
        if jugada1 == 1:
            rock_losses += 1
        elif jugada1 == 2:
            paper_losses += 1
        elif jugada1 == 3:
            scissors_losses += 1
        elif jugada1 == 4:
            lizard_losses += 1
        elif jugada1 == 5:
            spock_losses += 1
        if jugada2 == 1:
            rock_wins += 1
        elif jugada2 == 2:
            paper_wins += 1
        elif jugada2 == 3:
            scissors_wins += 1
        elif jugada2 == 4:
            lizard_wins += 1
        elif jugada2 == 5:
            spock_wins += 1

# Run the game 1000 times
for _ in range(1000):
    juego()

# Print final results
print("Rock wins:", rock_wins)
print("Paper wins:", paper_wins)
print("Scissors wins:", scissors_wins)
print("Lizard wins:", lizard_wins)
print("Spock wins:", spock_wins)
print("Rock losses:", rock_losses)
print("Paper losses:", paper_losses)
print("Scissors losses:", scissors_losses)
print("Lizard losses:", lizard_losses)
print("Spock losses:", spock_losses)
print("Ties:", ties)



import unittest

class TestGame(unittest.TestCase):
    def setUp(self):
        # Reset all counters before each test
        global rock_wins, paper_wins, scissors_wins, lizard_wins, spock_wins, rock_losses, paper_losses, scissors_losses, lizard_losses, spock_losses, ties
        rock_wins = 0
        paper_wins = 0
        scissors_wins = 0
        lizard_wins = 0
        spock_wins = 0
        rock_losses = 0
        paper_losses = 0
        scissors_losses = 0
        lizard_losses = 0
        spock_losses = 0
        ties = 0

    def test_game(self):
        # Run the game 1000 times
        for _ in range(1000):
            juego()

        # Check that the total number of games is correct
        self.assertEqual(rock_wins + paper_wins + scissors_wins + lizard_wins + spock_wins + ties, 1000)

        # Check that the total number of losses is correct
        self.assertEqual(rock_losses + paper_losses + scissors_losses + lizard_losses + spock_losses + ties, 1000)

if __name__ == '__main__':
    unittest.main()


from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/play', methods=['GET'])
def play_game():
    # Run the game 1000 times
    for _ in range(1000):
        juego()

    # Return the results as a JSON response
    return jsonify({
        "rock_wins": rock_wins,
        "paper_wins": paper_wins,
        "scissors_wins": scissors_wins,
        "lizard_wins": lizard_wins,
        "spock_wins": spock_wins,
        "rock_losses": rock_losses,
        "paper_losses": paper_losses,
        "scissors_losses": scissors_losses,
        "lizard_losses": lizard_losses,
        "spock_losses": spock_losses,
        "ties": ties
    })

if __name__ == '__main__':
    app.run(debug=True)