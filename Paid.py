import random

# Define the probability of a user being a paid user
paid_user_probability = 0.578

# Simulate whether a user is a paid user
is_paid_user = random.choices(['Paid', 'UnPaid'], weights=[paid_user_probability, 1 - paid_user_probability])[0]

print(is_paid_user)
