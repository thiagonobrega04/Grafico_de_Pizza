# Topic Overview and Actualization
# In today's lesson, we dive into the world of Pie Charts in Python. Pie charts enable you to depict proportions visually, illustrating populations by continents where each slice represents a part of the total, for instance. Today, you'll learn to create and customize pie charts in Python using Matplotlib.

# Pie charts are a type of graphic where the circle (the "pie") is divided into "slices," each of which represents a different category. Imagine a pizza where each slice is a fruit type - apples, oranges, bananas, and grapes. The size of each slice corresponds to the quantity of each fruit. To create interactive pie charts, we'll be using the well-established Python data visualization library: Matplotlib.

# Your First Pie Chart: Dataset
# Let's create a pie chart depicting the favorite fruits of a group of people, which could represent consumer preferences in a market survey. We will use this dataset:

import matplotlib.pyplot as plt
import pandas as pd

# Dataframe for plotting
df = pd.DataFrame({'Fruits': ['Apples', 'Bananas', 'Cherries', 'Dates'],
                   'Counts': [15, 30, 45, 10]})
labels = df['Fruits']
sizes = df['Counts']

# Your First Pie Chart: Sharing the Pie
# Let's start crafting a pie chart for this dataset.

# Pie Chart Components:

# . Slices: Portions of each fruit preference.
# . Labels: Names of the fruits.
# Crafting a Pie Chart: With the Matplotlib library, we can create an informative and appealing pie chart. It takes the data array and labels for it. We will also pass the startangle parameter, which rotates the graph, to make its layout fancier.

plt.pie(sizes, labels=labels, startangle=20)
plt.title('Fruits Preferences')
plt.axis('equal')  # ensures the pie chart is a perfect circle
plt.show()

# This chart helps us visualize the division of preferences, much like how market shares are illustrated in business.

# Using 'explode' to Highlight a Slice
# To highlight a specific slice in a pie chart, we slightly separate it from the rest of the pie, a process referred to as "exploding" the slice.

# Consider an array or a tuple you pass to explode. Typically, most of the values are zero, except for the slice we want to highlight. For example:

explode = (0.1, 0, 0, 0)

# Here, we are exploding the first slice, i.e., moving it out slightly. Let's see what that looks like in a full code bloc:

explode = (0.1, 0, 0, 0)  # "explode" the first slice

plt.pie(sizes, labels=labels, explode=explode, startangle=20)
plt.title('Fruits Preferences')
plt.axis('equal')  # ensures the pie chart is a perfect circle
plt.show()

# Now our pie chart highlights the apples, or the first slice in our pie.

# Assigning Custom Colors
# Our pie charts can become even more visually appealing with custom colors. Matplotlib allows us to give each slice of our pie a specific color. To achieve this, we provide an array of color names to the colors parameter in the plt.pie() function.

# Let's look at a full example with the previous explode feature and the new colors feature:

explode = (0.1, 0, 0, 0)  # "explode" the first slice
colors = ['lightgreen', 'yellow', 'pink', 'skyblue']  # array of custom colors

plt.pie(sizes, labels=labels, explode=explode, colors=colors, startangle=20)
plt.axis('equal')  # Ensures the pie chart is a perfect circle
plt.show()

# On top of highlighting the apple slice, we have now added distinct colors to each slice of our pie chart!

# Displaying Percentages with autopct
# The autopct parameter allows us to promptly add the percentage value to each slice of a pie chart. This can be beneficial when you want to visually convey the proportions at a glance.

# To use it, we add the autopct parameter to the plt.pie() function. We typically represent the number as a floating-point percentage.

# Now, let's put it all together:

explode = (0.1, 0, 0, 0)  # "explode" the first slice
colors = ['lightgreen', 'yellow', 'pink', 'skyblue']  # array of custom colors

plt.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', startangle=20)
plt.axis('equal')  # Ensures the pie chart is a perfect circle
plt.show()

# The format string '%1.1f%%' means the number will be displayed as a floating point with at least one digit before and exactly one digit after the decimal point. The two percentage signs at the end of the format string are needed because the first acts as an escape character, making the second display a literal character on the pie slices.

# With this full code, we have a pie chart that highlights apples, uses custom colors for each slice, and shows the percentage of each slice.