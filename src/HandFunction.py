import gvxrPython3 as gvxr
from ObjectiveFunction import *
import random

def setXRayParameters(SOD, SDD):
    # Compute the source position in 3-D from the SOD
    gvxr.setSourcePosition(SOD,  0.0, 0.0, "cm");
    gvxr.setDetectorPosition(SOD - SDD, 0.0, 0.0, "cm");
    gvxr.usePointSource();

def objectiveFunction(aSolution):

    SOD = aSolution[0];
    SDD = aSolution[1];

    angle = len(aSolution)-2;
    angle_list = np.zeros(angle);

    for i in range(angle):

        angle_list[i] = aSolution[i+2];

    setXRayParameters(SOD, SDD);

    pred_image = bone_rotation(angle_list);

    RMSE = root_mean_squared_error(target_image, pred_image);

    return RMSE


class HandFunction(objectiveFunction):

    def __init__(self):
        number_of_dimensions = 50;

        boundaries = [];
        boundaries.append([0.7, 0.95]);
        boundaries.append([10, 1000]);
        for i in range(number_of_dimensions-2):
            boundaries.append([-90, 90]);

        super().__init__(number_of_dimensions,
                         boundaries,
                         objectiveFunction,
                         1);


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
