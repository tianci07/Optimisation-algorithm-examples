import gvxrPython3 as gvxr
import numpy as np

def bone_rotation(angles):

    root_transform = gvxr.getLocalTransformationMatrix('root');
    Thu_Meta_transform = gvxr.getLocalTransformationMatrix('node-Thu_Meta');
    Thu_Prox_transform = gvxr.getLocalTransformationMatrix('node-Thu_Prox');
    Thu_Dist_transform = gvxr.getLocalTransformationMatrix('node-Thu_Dist');
    Lit_Prox_transform = gvxr.getLocalTransformationMatrix('node-Lit_Prox');
    Lit_Midd_transform = gvxr.getLocalTransformationMatrix('node-Lit_Midd');
    Lit_Dist_transform = gvxr.getLocalTransformationMatrix('node-Lit_Dist');
    Thi_Prox_transform = gvxr.getLocalTransformationMatrix('node-Thi_Prox');
    Thi_Midd_transform = gvxr.getLocalTransformationMatrix('node-Thi_Midd');
    Thi_Dist_transform = gvxr.getLocalTransformationMatrix('node-Thi_Dist');
    Mid_Prox_transform = gvxr.getLocalTransformationMatrix('node-Mid_Prox');
    Mid_Midd_transform = gvxr.getLocalTransformationMatrix('node-Mid_Midd');
    Mid_Dist_transform = gvxr.getLocalTransformationMatrix('node-Mid_Dist');
    Ind_Prox_transform = gvxr.getLocalTransformationMatrix('node-Ind_Prox');
    Ind_Midd_transform = gvxr.getLocalTransformationMatrix('node-Ind_Midd');
    Ind_Dist_transform = gvxr.getLocalTransformationMatrix('node-Ind_Dist');

    gvxr.rotateNode('root', angles[0], 1, 0, 0);
    gvxr.rotateNode('root', angles[1], 0, 1, 0);
    #gvxr.rotateNode('root', angles[2], 0, 0, 1);

    gvxr.rotateNode('node-Thu_Meta', angles[3], 1, 0, 0);
    gvxr.rotateNode('node-Thu_Meta', angles[4], 0, 1, 0);
    #gvxr.rotateNode('node-Thu_Meta', angles[5], 0, 0, 1);

    gvxr.rotateNode('node-Thu_Prox', angles[6], 1, 0, 0);
    gvxr.rotateNode('node-Thu_Prox', angles[7], 0, 1, 0);
    #gvxr.rotateNode('node-Thu_Prox', angles[8], 0, 0, 1);

    gvxr.rotateNode('node-Thu_Dist', angles[9], 1, 0, 0);
    gvxr.rotateNode('node-Thu_Dist', angles[10], 0, 1, 0);
    #gvxr.rotateNode('node-Thu_Dist', angles[11], 0, 0, 1);

    gvxr.rotateNode('node-Lit_Prox', angles[12], 1, 0, 0);
    gvxr.rotateNode('node-Lit_Prox', angles[13], 0, 1, 0);
    #gvxr.rotateNode('node-Lit_Prox', angles[14], 0, 0, 1);

    gvxr.rotateNode('node-Lit_Midd', angles[15], 1, 0, 0);
    gvxr.rotateNode('node-Lit_Midd', angles[16], 0, 1, 0);
    #gvxr.rotateNode('node-Lit_Midd', angles[17], 0, 0, 1);

    gvxr.rotateNode('node-Lit_Dist', angles[18], 1, 0, 0);
    gvxr.rotateNode('node-Lit_Dist', angles[19], 0, 1, 0);
    #gvxr.rotateNode('node-Lit_Dist', angles[20], 0, 0, 1);

    gvxr.rotateNode('node-Thi_Prox', angles[21], 1, 0, 0);
    gvxr.rotateNode('node-Thi_Prox', angles[22], 0, 1, 0);
    #gvxr.rotateNode('node-Thi_Prox', angles[23], 0, 0, 1);

    gvxr.rotateNode('node-Thi_Midd', angles[24], 1, 0, 0);
    gvxr.rotateNode('node-Thi_Midd', angles[25], 0, 1, 0);
    #gvxr.rotateNode('node-Thi_Midd', angles[26], 0, 0, 1);

    gvxr.rotateNode('node-Thi_Dist', angles[27], 1, 0, 0);
    gvxr.rotateNode('node-Thi_Dist', angles[28], 0, 1, 0);
    #gvxr.rotateNode('node-Thi_Dist', angles[29], 0, 0, 1);

    gvxr.rotateNode('node-Mid_Prox', angles[30], 1, 0, 0);
    gvxr.rotateNode('node-Mid_Prox', angles[31], 0, 1, 0);
    #gvxr.rotateNode('node-Mid_Prox', angles[32], 0, 0, 1);

    gvxr.rotateNode('node-Mid_Midd', angles[33], 1, 0, 0);
    gvxr.rotateNode('node-Mid_Midd', angles[34], 0, 1, 0);
    #gvxr.rotateNode('node-Mid_Midd', angles[35], 0, 0, 1);

    gvxr.rotateNode('node-Mid_Dist', angles[36], 1, 0, 0);
    gvxr.rotateNode('node-Mid_Dist', angles[37], 0, 1, 0);
    #gvxr.rotateNode('node-Mid_Dist', angles[38], 0, 0, 1);

    gvxr.rotateNode('node-Ind_Prox', angles[39], 1, 0, 0);
    gvxr.rotateNode('node-Ind_Prox', angles[40], 0, 1, 0);
    #gvxr.rotateNode('node-Ind_Prox', angles[41], 0, 0, 1);

    gvxr.rotateNode('node-Ind_Midd', angles[42], 1, 0, 0);
    gvxr.rotateNode('node-Ind_Midd', angles[43], 0, 1, 0);
    #gvxr.rotateNode('node-Ind_Midd', angles[44], 0, 0, 1);

    gvxr.rotateNode('node-Ind_Dist', angles[45], 1, 0, 0);
    gvxr.rotateNode('node-Ind_Dist', angles[46], 0, 1, 0);
    #gvxr.rotateNode('node-Ind_Dist', angles[47], 0, 0, 1);

    x_ray_image = gvxr.computeXRayImage();
    image = np.array(x_ray_image);

    gvxr.setLocalTransformationMatrix('root', root_transform);
    gvxr.setLocalTransformationMatrix('node-Thu_Meta', Thu_Meta_transform);
    gvxr.setLocalTransformationMatrix('node-Thu_Prox', Thu_Prox_transform);
    gvxr.setLocalTransformationMatrix('node-Thu_Dist', Thu_Dist_transform);

    gvxr.setLocalTransformationMatrix('node-Lit_Prox', Lit_Prox_transform);
    gvxr.setLocalTransformationMatrix('node-Lit_Midd', Lit_Midd_transform);
    gvxr.setLocalTransformationMatrix('node-Lit_Dist', Lit_Dist_transform);

    gvxr.setLocalTransformationMatrix('node-Thi_Prox', Thi_Prox_transform);
    gvxr.setLocalTransformationMatrix('node-Thi_Midd', Thi_Midd_transform);
    gvxr.setLocalTransformationMatrix('node-Thi_Dist', Thi_Dist_transform);

    gvxr.setLocalTransformationMatrix('node-Mid_Prox', Mid_Prox_transform);
    gvxr.setLocalTransformationMatrix('node-Mid_Midd', Mid_Midd_transform);
    gvxr.setLocalTransformationMatrix('node-Mid_Dist', Mid_Dist_transform);

    gvxr.setLocalTransformationMatrix('node-Ind_Prox', Ind_Prox_transform);
    gvxr.setLocalTransformationMatrix('node-Ind_Midd', Ind_Midd_transform);
    gvxr.setLocalTransformationMatrix('node-Ind_Dist', Ind_Dist_transform);

    return image
