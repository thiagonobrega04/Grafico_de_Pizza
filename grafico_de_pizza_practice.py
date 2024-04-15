# Imagine that a space tech company has conducted market research to understand consumer preferences for various gadgets. The provided code represents the results using a pie chart, which shows the percentage popularity for each gadget type. Click Run to visualize the consumer preferences as a pie chart!

import matplotlib.pyplot as plt

# Market research data: preferences for different types of electronics
products = ['Smartphones', 'Tablets', 'Laptops', 'Desktops']
popularity = [45, 25, 20, 10]

plt.pie(popularity, labels=products, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Consumer Electronics Preferences')
plt.show()

# Stellar Navigator, let's give this pie chart a new spin! Change the code to highlight the 'Electronics' slice. Add the explode parameter to make the 'Electronics' slice stand out. After this, let's change the autopct parameter to display two decimal places, making the graph more informative.

sizes = [3557, 2413, 1915, 1915]
labels = ['Toys', 'Books', 'Clothing', 'Electronics']
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = (0, 0, 0, 0.1)  # Emphasize the 'Electronics' slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%')
plt.title('Consumer Electronics Preferences')
plt.axis('equal')
plt.show()

# Great progress, Space Voyager! Let's see if you can add more detail to our pie chart. A few lines are missing that will make our chart both informative and visually pleasing. Go ahead and complete the code.

# Consumer preferences for ice cream flavors
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint']
votes = [50, 35, 15, 25]
colors = ['beige', 'saddlebrown', 'lightcoral', 'lightgreen']
explode = (0.1, 0, 0, 0)  # highlight the largest share

# TODO: Use the plt.pie function to create a pie chart with the given data
plt.pie(votes, explode=explode, labels=flavors, colors=colors, autopct= '%1.1f%%')

# Ensure the chart shows percentage for each slice, and is drawn as an equal circle.
plt.axis('equal')

# Ensure the chart has a title
plt.title("Ice Cream Flavor Preferences")
plt.show()

# Craft a pie chart that showcases consumer preferences with labels and a burst of color. Don't forget to use the explode feature to highlight Pizza, and make the important percentages stand out! To wrap up, display your chart as the grand finale of your data storytelling.

sizes = [215, 130, 245, 210]
labels = ['Pizza', 'Burgers', 'Salads', 'Tacos']
# TODO: Assign a color to each label
colors = ['blue', 'gray', 'red', 'yellow']

# TODO: Configure the 'explode' feature to highlight the Pizza category
explode = (0.1, 0, 0, 0)

# TODO: Use the pie function to make a pie chart that includes labels, colors, explode feature, and displays percentages
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

# TODO: Include a title
plt.title( "Favorite Food Category" )

# TODO: Ensure the pie chart is displayed as a perfect circle
plt.axis( 'equal' )

# TODO: Display the pie chart using the appropriate function
plt.show()