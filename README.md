Assignment Title: Bayesian Analysis

Description:
This Python script generates visualizations for Bayesian inference using the beta distribution given the intial data. It plots the posterior probability distribution function for given parameters `a` and `b`, along with key statistics such as mean and standard deviation.

Requirements:
- Python 3.x
- NumPy
- Plotly

Usage:
1. Ensure Python 3.x is installed on your system.
2. Install required dependencies by running:
3. Run the script `BayesianAnalysis.py`.
4. The script will generate a plot displaying the posterior distribution along with key statistics.

Parameters:
- `r`: Number of heads in the observed data.
- `n`: Total number of trials in the observed data.
- `a`: List of shape parameters for the prior beta distribution.
- `b`: List of shape parameters for the prior beta distribution.

Output:
The script generates a plot displaying the posterior probability distribution function (PDF) for each set of provided parameters `a` and `b`. It also highlights key statistics such as the maximum posterior probability and the mean with standard deviation intervals.

Example:
To visualize Bayesian inference for multiple sets of parameters, modify the `a` and `b` lists accordingly and run the script.