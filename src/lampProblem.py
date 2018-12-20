
import numpy as np
import cv2

room_width = 100;
room_height = 100;
lamp_radius = 10;

image_counter = 0;

def getArea():
    return room_width * room_height;

def areaEnlightened(aSetOfLamps):
    
    global image_counter;
    
    number_of_lamps = int(len(aSetOfLamps) / 3);
    
    # Create a black image (float, greyscale) of room_width x room_height pixels
    overlay_image = np.zeros((room_height, room_width, 1), np.float32)
    
    
    
    # print the position of all the lamps
    for i in range(number_of_lamps):
        x = int(aSetOfLamps[     i * 3 + 0])
        y = int(aSetOfLamps[     i * 3 + 1])
        on_off = aSetOfLamps[i * 3 + 2];
        
        if on_off > 0.5:
            # Draw circles corresponding to the lamps
            black_image = np.zeros((room_height, room_width, 1), np.float32)
            cv2.circle(black_image, (x,y), lamp_radius, (1,1,1), -1)
            np.add(overlay_image, black_image, overlay_image);

    # Copy the image into a temp image for debug
    temp_image = np.copy(overlay_image);

    for i in range(number_of_lamps):
        x = int(aSetOfLamps[     i * 3 + 0])
        y = int(aSetOfLamps[     i * 3 + 1])
        on_off = aSetOfLamps[i * 3 + 2];
        
        if on_off > 0.5:
            # Plot the center of all the lamp (small radius) in black
            cv2.circle(temp_image, (x,y), 2, (0,0,0), -1)

    # Save the image (use image_counter in the file name)
    filename = "lamp_" + str(image_counter) + ".png";
    image_counter += 1;
    cv2.imwrite(filename, temp_image)
    
    cv2.imshow("Window", overlay_image)
    cv2.imshow("Window1", temp_image)

    overlay_image = np.array(overlay_image)

    areaEnlight = 0
    for i in range(room_width):
        for j in range(room_height):

            if (overlay_image[i,j] > 0):
                areaEnlight += min(overlay_image[i,j], 1)

    print(areaEnlight)
    cv2.waitKey(0)
    
    return 0;

def areaOverlap(aSetOfLamps):
    return 0;

def fitnessFunction(aSetOfLamps, W=1):
    
    return (areaEnlightened(aSetOfLamps) / getArea()) - W * (areaOverlap(aSetOfLamps) / getArea());
