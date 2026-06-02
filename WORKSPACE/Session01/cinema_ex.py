day = "Saturday"
film = "A.I. Artificial Intelligence"
print(f"Today is {day}, and the film showing is {film}.")

n_capacity = 210
n_minor = 81
n_adult = 66
price_minor = 5.99
price_adult = 10.49

total_tickets_sold = n_minor + n_adult
seats_remaining = n_capacity - total_tickets_sold
revenue_tickets = n_minor*price_minor + n_adult*price_adult
print(f"We have sold {total_tickets_sold} tickets.")
print(f"The ticket revenue is £{revenue_tickets}.")
print(f"There are still {seats_remaining} tickets available.")
