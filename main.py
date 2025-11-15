import random as rand

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = rand.sample(cards, 2)
user_cards = rand.sample(cards, 2)


def score(hand):
    total = sum(hand)
    if 11 in hand and total > 21:
        total -= 10
    return total


cont = True

while cont:

    computer_score = score(computer_cards)
    user_score = score(user_cards)

    # Blackjack check
    if computer_score == 21:
        print("Dealer wins")
        break
    elif user_score == 21:
        print("User wins")
        break

    print(f"Dealer's score: {computer_score}")
    print(f"User's score: {user_score}")

    continu = input("Do you want another card? y or n: ").lower()

    # -----------------------------------
    # USER HITS (no continue needed)
    # -----------------------------------
    if continu == "y":
        user_card = rand.choice(cards)
        user_cards.append(user_card)
        print(f"You drew: {user_card}")

        user_score = score(user_cards)

        # If user busts → stop game
        if user_score > 21:
            print(f"Your cards: {user_cards}. Your score: {user_score}. You bust. Dealer wins.")
            cont = False
        # Otherwise, loop starts again naturally (no continue needed)


    # -----------------------------------
    # USER STANDS → DEALER PLAYS
    # -----------------------------------
    else:  # user said 'n'
        print(f"Dealer's cards: {computer_cards}")

        while computer_score < 17:
            computer_card = rand.choice(cards)
            computer_cards.append(computer_card)
            computer_score = score(computer_cards)
            print(f"Dealer draws a new card: {computer_card}")

        # Final results
        print(f"\nFinal dealer's score: {computer_score}")
        print(f"Final user's score: {user_score}")

        if computer_score > 21:
            print("Dealer busts. User wins!")
        elif computer_score > user_score:
            print("Dealer wins.")
        elif user_score > computer_score:
            print("User wins.")
        else:
            print("Draw.")

        cont = False  # End game
