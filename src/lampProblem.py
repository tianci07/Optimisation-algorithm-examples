

room_width = 0;
room_height = 0;
lamp_radius = 0;

image_counter = 0;

def getArea():
    return room_width * room_height;

def areaEnlightened(aSetOfLamps):
    global image_counter;

    # print the position of all the lamps

    # Create a black image (float, greyscale) of room_width x room_height pixels

    # Draw circles corresponding to the lamps

    # Copy the image into a temp image for debug
    # Plot the center of all the lamp (small radius) in black
    # Save the image (use image_counter in the file name)
    filename = "lamp_" + str(image_counter) + ".png";
    image_counter += 1;


    return 0;

def areaOverlap(aSetOfLamps):
    return 0;

def fitnessFunction(aSetOfLamps, W):
    return (areaEnlightened(aSetOfLamps) / getArea()) - W * (areaOverlap(aSetOfLamps) / getArea());
