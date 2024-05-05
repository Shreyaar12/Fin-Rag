
import matplotlib.pyplot as plt

def plot_financial_ratios():
    # Ask the user for the type of ratio they want to plot
    ratio_type = input("Enter the type of ratio to plot (solvency, liquidity, efficiency, profitability): ").lower()
    
    # Initialize variables
    years = []
    ratios = []
    label = ""
    
    # Collect data based on user input
    if ratio_type == 'solvency':
        years = input("Enter the years separated by comma (e.g., 2022,2023): ").split(',')
        ratios = list(map(float, input("Enter the solvency ratios for these years separated by comma (e.g., 42.6,42.0): ").split(',')))
        label = 'Solvency Ratio (%)'
    elif ratio_type == 'liquidity':
        years = input("Enter the years separated by comma (e.g., 2022,2023): ").split(',')
        ratios = list(map(float, input("Enter the liquidity ratios for these years separated by comma (e.g., 1.5,1.6): ").split(',')))
        label = 'Liquidity Ratio'
    elif ratio_type == 'efficiency':
        years = input("Enter the years separated by comma (e.g., 2022,2023): ").split(',')
        ratios = list(map(float, input("Enter the efficiency ratios for these years separated by comma (e.g., 88,90): ").split(',')))
        label = 'Efficiency Ratio (%)'
    elif ratio_type == 'profitability':
        years = input("Enter the years separated by comma (e.g., 2022,2023): ").split(',')
        ratios = list(map(float, input("Enter the profitability ratios for these years separated by comma (e.g., 15,16): ").split(',')))
        label = 'Profitability Ratio (%)'
    else:
        print("Invalid ratio type entered.")
        return

    # Plotting the data
    fig, ax = plt.subplots()
    ax.bar(years, ratios, color='skyblue')
    ax.set_xlabel('Year')
    ax.set_ylabel('Ratio Value')
    ax.set_title(f'{label} for Google')
    ax.set_xticks(years)
    ax.set_xticklabels(years)

    plt.show()

# Run the function
plot_financial_ratios()
