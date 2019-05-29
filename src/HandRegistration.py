import numpy as np
from Metrics import *
from RotateBones import bone_rotation
from DisplayMetrics import display_metrics
import PureRandomSearch as PRS
import gvxrPython3 as gvxr
import random
import matplotlib.pyplot as plt
from SimulatedAnnealing import *
import time

def setXRayParameters(SOD, SDD):
    # Compute the source position in 3-D from the SOD
    gvxr.setSourcePosition(SOD,  0.0, 0.0, "cm");
    gvxr.setDetectorPosition(SOD - SDD, 0.0, 0.0, "cm");
    gvxr.usePointSource();

def objectiveFunction(params):

    SOD = params[0];
    SDD = params[1];
    angle = len(params)-2;
    angle_list = np.zeros(angle);

    for i in range(angle):

     angle_list[i] = params[i+2];

    setXRayParameters(SOD, SDD);

    pred_image = bone_rotation(angle_list);

    RMSE = root_mean_squared_error(target_image, pred_image);
    #SSIM = structural_similarity(pred_image, ground_truth_image);
    #ZNCC = zero_mean_normalised_cross_correlation(ground_truth_image, pred_image);
    #RE = relative_error(ground_truth_image, pred_image);
    #MAE = mean_absolute_error(ground_truth_image, pred_image);

    return RMSE

target_SOD = 100;
target_SDD = 140;
target_angles_pa = [-90, 20, 0, -10, 0, 0,
                    5, 0, 0, 5, 0, 0,
                    0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0
                    ];
target = [];
target.append(target_SOD);
target.append(target_SDD);
for i in range(48):
    target.append(target_angles_pa[i]);

gvxr.createWindow();
gvxr.setWindowSize(512, 512);

#gvxr.usePointSource();
gvxr.setMonoChromatic(80, "MeV", 1000);

gvxr.setDetectorUpVector(0, 0, -1);
gvxr.setDetectorNumberOfPixels(1536, 1536);
gvxr.setDetectorPixelSize(0.5, 0.5, "mm"); # 5 dpi
setXRayParameters(target_SOD, target_SDD);

gvxr.loadSceneGraph("/home/ti/Documents/gvxr-python3-gui/hand.dae", "m");
node_label_set = [];
node_label_set.append('root');

# The list is not empty
while (len(node_label_set)):

    # Get the last node
    last_node = node_label_set[-1];

    # Initialise the material properties
    # print("Set ", label, "'s Hounsfield unit");
    # gvxr.setHU(label, 1000)
    Z = gvxr.getElementAtomicNumber("H");
    gvxr.setElement(last_node, gvxr.getElementName(Z));

    # Change the node colour to a random colour
    gvxr.setColour(last_node, random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), 1.0);

    # Remove it from the list
    node_label_set.pop();

    # Add its Children
    for i in range(gvxr.getNumberOfChildren(last_node)):
        node_label_set.append(gvxr.getChildLabel(last_node, i));

gvxr.moveToCentre('root');
gvxr.disableArtefactFiltering();

target_image = bone_rotation(target_angles_pa);
plt.imsave("./posterior-anterior/RMSE/target.png", target_image, cmap='Greys_r');

bounds = [];
bounds.append([0.7, 0.95]);
bounds.append([10, 1000]);
for i in range(48):
    bounds.append([-90, 90]);

for j in range(10):

    start = time.time();
    optimiser = PRS.PureRandomSearch(50, bounds, objectiveFunction, 0, 500);
    end = time.time();
    computing_time = end-start;
    pred_image = display_metrics(optimiser.best_solution, target_angles_pa, computing_time);

    plt.imsave("./posterior-anterior/RMSE/prediction-rs-%d.png" % j, pred_image, cmap='Greys_r');

# df.to_csv('./posterior-anterior/RMSE/results_PRS.csv');
