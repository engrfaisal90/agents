
import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Colorful Geometric Spiral")
screen.bgcolor("black")  # Black background makes colors pop

# Create and configure the turtle
artist = turtle.Turtle()
artist.speed(0)          # 0 is the fastest animation speed
artist.pensize(2)        # Set line thickness

# Define a list of vibrant colors to loop through
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# Draw the spiral pattern
for x in range(360):
    # Change color dynamically based on the current loop iteration
    artist.pencolor(colors[x % len(colors)])
    
    # Move forward a bit more each time to expand the spiral
    artist.forward(x)
    
    # Turn left by 59 degrees (slightly under 60 creates the twisted geometric effect)
    artist.left(59)

# Keep the window open until you click on it
screen.exitonclick()