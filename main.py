import action
# Huy Kieu

# 52 cards
CARD = [
    ("Ace of Hearts", 11), ("Ace of Spades", 11), ("Ace of Diamonds", 11), ("Ace of Clubs", 11),
    ("2 of Hearts", 2), ("2 of Spades", 2), ("2 of Diamonds", 2), ("2 of Clubs", 2),
    ("3 of Hearts", 3), ("3 of Spades", 3), ("3 of Diamonds", 3), ("3 of Clubs", 3),
    ("4 of Hearts", 4), ("4 of Spades", 4), ("4 of Diamonds", 4), ("4 of Clubs", 4),
    ("5 of Hearts", 5), ("5 of Spades", 5), ("5 of Diamonds", 5), ("5 of Clubs", 5),
    ("6 of Hearts", 6), ("6 of Spades", 6), ("6 of Diamonds", 6), ("6 of Clubs", 6),
    ("7 of Hearts", 7), ("7 of Spades", 7), ("7 of Diamonds", 7), ("7 of Clubs", 7),
    ("8 of Hearts", 8), ("8 of Spades", 8), ("8 of Diamonds", 8), ("8 of Clubs", 8),
    ("9 of Hearts", 9), ("9 of Spades", 9), ("9 of Diamonds", 9), ("9 of Clubs", 9),
    ("10 of Hearts", 10), ("10 of Spades", 10), ("10 of Diamonds", 10), ("10 of Clubs", 10),
    ("Jack of Hearts", 10), ("Jack of Spades", 10), ("Jack of Diamonds", 10), ("Jack of Clubs", 10),
    ("Queen of Hearts", 10), ("Queen of Spades", 10), ("Queen of Diamonds", 10), ("Queen of Clubs", 10),
    ("King of Hearts", 10), ("King of Spades", 10), ("King of Diamonds", 10), ("King of Clubs", 10)
]


def main():
    play = True
    while play:
        # Construct new game
        print("Welcome to Blackjack!")
        player_hand = []
        player_score = 0
        dealer_hand = []
        dealer_score = 0

        # player draws two cards
        player_hand.append(action.draw_a_card(CARD))
        player_hand.append(action.draw_a_card(CARD))
        player_score = action.calculate_total_score(player_hand)
        print("Your cards are: " + action.card_in_words(player_hand))
        print("Your score is: " + str(player_score))
        is_blackjack = False
        if player_score == 21:
            is_blackjack = True
            print("Blackjack!!! Congratulation, you won!")

        # start game
        play_game = True
        win = None
        while play_game and not is_blackjack:
            print("Would you like to [H]it or [S]tand?  ")
            keep_going = input()
            # if the player chooses to hit
            if keep_going == "Hit" or keep_going == "hit" or keep_going == "H" or keep_going == "h":
                player_hand.append(action.draw_a_card(CARD))
                player_score = action.calculate_total_score(player_hand)
                if player_score > 21:
                    print("Your cards are: " + action.card_in_words(player_hand))
                    print("Your current score is: " + str(player_score))
                    print('')
                    print("You went bust! You lose!")
                    win = False
                    play_game = False
                elif len(player_hand) > 4:
                    print("You got a 5 Card Charlie'! You Win!")
                    win = True
                    play_game = False
                else:
                    print("Your cards are: " + action.card_in_words(player_hand))
                    print("Your current score is: " + str(player_score) + "\n")
            # if the player chooses to stay, then the dealer draws cards
            elif keep_going == "Stand" or keep_going == "stand" or keep_going == "S" or keep_going == "s":
                print("Dealer's turn!")
                dealer_hand.append(action.draw_a_card(CARD))
                dealer_hand.append(action.draw_a_card(CARD))
                dealer_score = action.calculate_total_score(dealer_hand)
                while dealer_score < 15:
                    dealer_hand.append(action.draw_a_card(CARD))
                    dealer_score = action.calculate_total_score(dealer_hand)
                print("The dealer's hand is: " + action.card_in_words(dealer_hand))
                print("The dealer's score is: " + str(dealer_score))
                print('')
                if dealer_score == 21:
                    print("The dealer got blackjack! You lose!")
                    break
                elif dealer_score > 21:
                    print("The dealer went bust! You win!")
                    win = True
                    play_game = False
                elif len(dealer_hand) > 4:
                    print("The dealer got a 5 Card Charlie'. You lose!")
                    win = False
                    play_game = False
                elif dealer_score > player_score:
                    print("The dealer's score is higher'! You lose!")
                    win = False
                    play_game = False
                elif dealer_score == player_score:
                    print("It's a tie!")
                    win = False
                    play_game = False
                else:
                    print("Your score is higher! You win!")
                    win = True
                    play_game = False

        # checks if the player plays again
        keep_playing = input("\nKeep playing? [Y/N]  ")
        if keep_playing == "No" or keep_playing == "no" or keep_playing == "N" or keep_playing == "n":
            print("Thank you for playing! Have a nice day!")
            play = False
        elif keep_playing == "Yes" or keep_playing == "yes" or keep_playing == "Y" or keep_playing == "y":
            print('\n***** NEW GAME *****\n')
        else:
            print('Sorry, I don\'t understand!')
            play = False


if __name__ == "__main__":
    main()
