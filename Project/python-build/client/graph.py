import matplotlib.pyplot as plt
import numpy as np
import asyncio
import random
import numpy as np
plt.style.use('ggplot') # use ggplot style for more sophisticated visuals


async def live_plotter(x_vec,y1_data,line1,identifier='',pause_time=0.1):
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
        line1, = ax.plot(x_vec,y1_data,'-o',alpha=0.8)        
        #update plot label/title
        plt.ylabel('Y Label')
        plt.title('Title: {}'.format(identifier))
        plt.show()
    
    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(y1_data)
    # adjust limits if new data goes beyond bounds
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)
    
    # return line so we can update it again in the next iteration
    return line1



# ----------------------------------------- #
async def get_old_data():
    size = 100
    old_data = np.random.randn(size)
    return old_data

async def get_new_data():
    new_data = np.random.randn(1)
    return new_data


async def generate_random_point(a=-1,b=1):
    x = random.uniform(a, b)
    y = random.uniform(a, b)
    return x, y

async def generate_random_points(num_points=100,a=-1,b=1): 
    points = []
    for _ in range(num_points):
        x,y = await generate_random_point(a=a,b=b)
        points.append((x, y))
    return points

async def get_graph_dims():
    y_vec  = await get_old_data()
    size = y_vec.size
    x_vec = np.linspace(0,1,size+1)[0:-1]
    return x_vec,y_vec


async def generate_graph_from_dims():
    x_vec,y_vec = await get_graph_dims()
    line1 = []
    while True:
        rand_val = await get_new_data()
        y_vec[-1] = rand_val
        line1 = await live_plotter(x_vec,y_vec,line1)
        y_vec = np.append(y_vec[1:],0.0)
# ----------------------------------------- #





# ----------------------------------------- #
async def get_old_points():
    old_points = await generate_random_points(num_points=100)
    return old_points

async def get_new_point():
    new_point = await generate_random_point()
    return new_point

async def get_points_graph_dims():
    points = await get_old_points()
    size = len(points)
    x_vec = np.linspace(0, 1, size + 1)[:-1]
    y_vec = [point[1] for point in points]
    return x_vec, y_vec

async def generate_graph_from_points():
    x_vec, y_vec = await get_points_graph_dims()
    line1 = []
    while True:
        rand_point = await get_new_point()
        y_vec[-1] = rand_point[1]
        line1 = await live_plotter(x_vec, y_vec, line1)
        y_vec = np.append(y_vec[1:], 0.0)
# ----------------------------------------- #



async def main():
    await generate_graph_from_dims()



if __name__ == "__main__":
    asyncio.run(main())