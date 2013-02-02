import blackjack

card = blackjack.Card()
assert card.value == 1

deck = blackjack.Deck()
assert len(deck.cards) == 52

cstack = blackjack.CardStack(2)
assert len(cstack.stack) == 104
cstack.draw()
assert len(cstack.stack) == 103

hand = blackjack.Hand()
hand.add_card(card)
assert hand.values[0] == 1
assert hand.values[1] == 11

game = blackjack.Game()
assert len(game.cardstack.stack) == 52 * 8
game.play()
