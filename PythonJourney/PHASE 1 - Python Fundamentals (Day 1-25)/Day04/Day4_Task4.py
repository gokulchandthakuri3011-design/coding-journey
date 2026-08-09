"""
### Assignment 4: The Ticket Formatter
1. Create variables: `movie_title` (string), `time` (string), and `ticket_price` (float).
2. Use an **f-string** to create a well-formatted ticket and save it to a variable called `ticket`.
3. Print the `ticket`. 
   *Example Output: `Movie: The Matrix | Time: 8:00 PM | Price: $12.5`*
"""

# The Ticket Formatter

# Creating variables for movie tittle, time and ticket price
movie_title = "Avengers: Endgame"
time = "7:30 PM"
ticket_price = 15.0 # In dollars

# Using an f-string to create a well-formed ticket
ticket = f"Movie: {movie_title} | Time: {time} | Price: ${ticket_price}"

# Printing the ticket
print(ticket)
