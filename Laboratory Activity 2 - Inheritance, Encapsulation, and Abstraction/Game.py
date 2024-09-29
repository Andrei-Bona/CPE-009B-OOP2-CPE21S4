import random
from Novice import Novice
from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss

def choose_role(username, is_boss=False):
    if is_boss:
        return Boss(username)
    else:
        print("Choose a role:")
        print("1. Swordsman")
        print("2. Archer")
        print("3. Magician")
        choice = int(input("Enter the number of your choice: "))
        if choice == 1:
            return Swordsman(username)
        elif choice == 2:
            return Archer(username)
        elif choice == 3:
            return Magician(username)
            
            print("Invalid choice, defaulting to Novice.")
            return Novice(username)

def player_turn(attacker, defender):
    print(f"\n{attacker.getUsername()}'s turn!")
    print("Choose an action:")
    print("1. Basic Attack")
    if isinstance(attacker, Swordsman):
        print("2. Slash Attack")
    elif isinstance(attacker, Archer):
        print("2. Ranged Attack")
    elif isinstance(attacker, Magician):
        print("2. Magic Attack")
        print("3. Heal")
    
    choice = int(input("Enter the number of your choice: "))
    if choice == 1:
        attacker.basicAttack(defender)
    elif choice == 2:
        if isinstance(attacker, Swordsman):
            attacker.slashAttack(defender)
        elif isinstance(attacker, Archer):
            attacker.rangedAttack(defender)
        elif isinstance(attacker, Magician):
            attacker.magicAttack(defender)
    elif choice == 3 and isinstance(attacker, Magician):
        attacker.heal()
    else:
        print("Invalid choice, performing Basic Attack.")
        attacker.basicAttack(defender)

def play_match(player1, player2):
    while player1.getHp() > 0 and player2.getHp() > 0:
        if random.choice([True, False]):
            player_turn(player1, player2)
        else:
            player_turn(player2, player1)

        print(f"\n{player1.getUsername()} HP: {player1.getHp()}")
        print(f"{player2.getUsername()} HP: {player2.getHp()}")

    if player1.getHp() <= 0:
        print(f"\n{player1.getUsername()} has been defeated!")
        return player2
    else:
        print(f"\n{player2.getUsername()} has been defeated!")
        return player1

def single_player_game():
    player = Novice("Player")
    wins = 0

    while True:
        opponent = Boss("Monster")
        winner = play_match(player, opponent)

        if winner == player:
            wins += 1
            print(f"Congratulations! You have {wins} win(s).")
            if wins == 2:
                print("\nYou can now choose a new role!")
                player = choose_role("Player")
        else:
            print("You lost! Better luck next time.")
            break

def player_vs_player_game():
    player1 = choose_role("Player 1")
    player2 = choose_role("Player 2")
    wins_p1 = 0
    wins_p2 = 0

    while True:
        winner = play_match(player1, player2)

        if winner == player1:
            wins_p1 += 1
            print(f"Player 1 wins! Total wins: {wins_p1}")
        else:
            wins_p2 += 1
            print(f"Player 2 wins! Total wins: {wins_p2}")

        play_again = input("Do you want to play another match? (yes/no): ").lower()
        if play_again != "yes":
            break

def main():
    while True:
        print("Welcome to the Game!")
        print("1. Single Player")
        print("2. Player vs Player")
        print("3. Exit")
        mode = int(input("Enter the number of your choice: "))

        if mode == 1:
            single_player_game()
        elif mode == 2:
            player_vs_player_game()
        elif mode == 3:
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
