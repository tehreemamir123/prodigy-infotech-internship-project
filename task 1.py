import matplotlib.pyplot as plt

# Data for age groups and their counts
age_groups = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60+']
counts = [150, 300, 450, 600, 550, 400, 300]

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(age_groups, counts, color='skyblue')

# Adding titles and labels
plt.title('Distribution of Ages in a Population')
plt.xlabel('Age Groups')
plt.ylabel('Number of People')

# Display the plot
plt.show()
