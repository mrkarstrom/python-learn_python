customer_name = 'Magnus'
num_passes = 3
tokens_per_pass = 2
price_per_pass = 30.5
tokens_per_game = 3

total_tokens = num_passes * tokens_per_pass
total_cost = num_passes * price_per_pass
games_available = total_tokens // tokens_per_game

print("Arcade Day Pass Summary")
print("-----------------------")
print(f"Customer Name: {customer_name}")
print(f"Passes bought: {num_passes}")
print(f"Total amount of tokens: {total_tokens}")
print(f"Total cost: {total_cost}")
print(f"Games available: {games_available}")
