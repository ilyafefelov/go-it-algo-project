import random
import matplotlib.pyplot as plt
import pandas as pd
import collections


def monte_carlo_simulation(num_rolls):
    """
    Simulates rolling two dice multiple times and calculates the probabilities of each possible sum.
    Parameters:
    - num_rolls (int): The number of times to roll the dice.
    Returns:
    - probabilities (dict): A dictionary containing the probabilities of each possible sum.
                           The keys are the sums of the two dice, and the values are the corresponding probabilities.
    """
    
    results = collections.defaultdict(int)

    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll_sum = roll1 + roll2
        results[roll_sum] += 1
    # Calculate probabilities from counts and total number of rolls - num_rolls (int) 
    prob_factor = 1 / num_rolls
    probabilities = {s: count * prob_factor for s, count in results.items()}
    return probabilities


# Run Monte Carlo simulation
num_rolls = 100000
simulation_results = monte_carlo_simulation(num_rolls)
print("Monte Carlo simulation results:")
for sum, probability in simulation_results.items():
    print(f"Sum: {sum}, Probability: {probability}")

# Analytical probabilities table (as percentages)
analytical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}

# Convert simulation results to percentages
simulation_results_percent = {
    key: value * 100 for key, value in simulation_results.items()
}

# Prepare data for plotting
sums = list(analytical_probabilities.keys())
analytical_probs = [analytical_probabilities[sum] for sum in sums]
simulation_probs = [simulation_results_percent[sum] for sum in sums]

# Create a comparison DataFrame
comparison_data = {
    "Sum": sums,
    "Analytical P (%)": analytical_probs,
    "Simulation P (%)": simulation_probs,
    "Difference": [
        simulation_probs[i] - analytical_probs[i] for i in range(len(sums))
    ],
}
comparison_df = pd.DataFrame(comparison_data)


# Set display options to show more columns
pd.set_option("display.max_columns", 6)

# Display the comparison table
print(comparison_df)

# Plot the results
plt.figure(figsize=(10, 8))
plt.plot(
    sums,
    analytical_probs,
    marker="o",
    linestyle="-",
    color="blue",
    label="Analytical Probabilities",
)
plt.plot(
    sums,
    simulation_probs,
    marker="x",
    linestyle="--",
    color="red",
    label="Simulation Probabilities",
)
plt.xlabel("Sum of Dice Rolls")
plt.ylabel("Probability (%)")
plt.title("Comparison of Analytical and Simulation Probabilities")
plt.legend()
plt.grid(True)
plt.show()

comparison_df
