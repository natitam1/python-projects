from random import choice

"""This project demonstrates how to simulate winning a lottery"""
lottery_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd']

my_ticket = [1, 2, 3, 4]
num = 0
winner = []

while sorted(winner) != sorted(my_ticket):
    winner = [choice(lottery_list) for _ in range(4)]
    num += 1

print("🎉 Your ticket won!")
print("Winning ticket:", winner)
print(f"It took {num} tries to win.")
