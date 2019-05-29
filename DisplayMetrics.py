from skimage.measure import compare_ssim
from sklearn.metrics import mean_absolute_error, mean_squared_error
from RotateBones import bone_rotation
from Metrics import*
import pandas as pd
import matplotlib.pyplot as plt

def display_metrics(Prediction, Target, computingTime):
    global pred_image;

    prediction = Prediction;
    target = Target;
    angles = np.zeros(48);

    for i in range(len(prediction)-2):
        angles[i] = prediction[i+2];

    pred_image = bone_rotation(angles);
    target_image = bone_rotation(target);
    diff = [];

    for i in range(2):
        diff.append(abs(prediction[i]-target[i]));
    SSIM = structural_similarity(pred_image, target_image);
    MAE = mean_absolute_error(target_image, pred_image);
    RMSE = root_mean_squared_error(target_image, pred_image);
    RE = relative_error(target_image, pred_image);
    ZNCC = zero_mean_normalised_cross_correlation(target_image, pred_image);
    computing_time = computingTime;

    print('Prediction:' , prediction);
    print('Target: ', target);
    print('SOD and SDD errors: ', diff);
    print('Metrics: \n SSIM: %.8f \t MAE: %.8f \t RMSE: %.8f \t RE: %.8f \t ZNCC: %.8f'
            %(SSIM, MAE, RMSE, RE, ZNCC));

    # df = pd.DataFrame();
    #
    # row = [[prediction[0], diff[0], prediction[1], diff[1], angles,
    #         SSIM, MAE, RMSE, RE, ZNCC, computing_time]];
    #
    # df2 = pd.DataFrame(row, columns=['SOD', 'SOD Error','SDD',
    #                                 'SDD Error', 'Rotating Angles','SSIM',
    #                                 'MAE', 'RMSE','Relative Error', 'ZNCC',
    #                                 'Time']);
    #
    #
    # #save(image, "./posterior-anterior/SSIM/prediction-rs-%d.mha" % i);
    # df = df.append(df2, ignore_index=True);
    return pred_image
