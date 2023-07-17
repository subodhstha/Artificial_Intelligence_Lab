eats(tiger, meat).
eats(cow, vegetables).
eats(human, meat).
eats(human, vegetables).

carnivore(X) :- eats(X, meat).
omnivore(X) :- eats(X, meat), eats(X, vegetables).
herbivore(X) :- eats(X, vegetables)