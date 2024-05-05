import matplotlib.pyplot as plt

# Data for the plots
years = ['2022', '2023']
debt_to_equity_ratios = [42.6, 42.0]  # Percentages from the image
debt_ratios = [29.9, 29.6]  # Percentages from the image

# Creating the figure and a set of subplots
fig, ax = plt.subplots()

# Adding the Debt to Equity Ratio bars
ax.bar([x for x in years], debt_to_equity_ratios, width=0.4, label='Debt to Equity Ratio (%)', align='center')

# Adding the Debt Ratio bars
ax.bar([x for x in years], debt_ratios, width=0.4, label='Debt Ratio (%)', align='edge')

# Adding titles and labels
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('Solvency Ratios for Google (2022 & 2023)')
ax.legend()

# Display the plot
plt.show()
