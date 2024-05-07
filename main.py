import requests
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

url = 'http://135.181.0.186:1114/api/v1/contractInfo/plot'

sniped = []
ratio = []
active = []

def fetch_data():
    # Perform a GET request to fetch the data
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # print(data)
        return data
    else:
        # Handle request error (e.g., print error status and message)
        print('Error:', response.status_code, response.text)
        return None
    
def update():
    global sniped, ratio, active
    # Fetch new data
    data = fetch_data()

    if data is not None:
        # Extract the relevant data for plotting, e.g., x and y values
        sniped = data['sniped'].copy()
        ratio = data['ratio'].copy()
        active = data['active'].copy()
        
update()

active_points = [(s, min(200, r)) for s, r, a in zip(sniped, ratio, active) if a == 1]
inactive_points = [(s, min(200, r)) for s, r, a in zip(sniped, ratio, active) if a == 0]

# Unpack the points into x and y coordinates for plotting
active_x, active_y = zip(*active_points)
inactive_x, inactive_y = zip(*inactive_points)


# Plot inactive points
plt.scatter(inactive_x, inactive_y, c='red', label='Inactive:353', s=5)
# Plot active points
plt.scatter(active_x, active_y, c='green', label='Active:109', s=5)
# Set the background color of the axes (plot area)
plt.gca().set_facecolor('black')

# Set the background color of the figure (outside the plot area)
plt.gcf().set_facecolor('gray')

# Add labels and legend
plt.xlabel('sniped')
plt.ylabel('ratio')
plt.title('Active States of (sniped, ratio) Points')
plt.legend()

# Show the plot
plt.show()