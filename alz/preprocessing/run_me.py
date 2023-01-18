
from preprocessing.preprocess import Preprocess

'''
Initialize the below variable to your desired locations

initial_path -> path where the 3D brain image is present. For eg : '/content/drive/brain.nii'

path_to_store_stripped_skull -> mention the path where you would like to store the result of skull stripping process

path_to_store_bias_corrected -> mention the path where you would like to store the result of bias correction process

path_to_store_segmented_img-> mention the path where you would like to store the result of segmentation process

destination_path -> path where you would like to store the final result of preprocess phase.

'''
input_image = Preprocess()
input_image.strip_the_skull("C:\\Users\\anany\Downloads\ADNI1_Complete 2Yr 3T-003\\ADNI","C:\\Users\\anany\Downloads\\ADNI1_Complete 2Yr 3T-003\Processed\\1")
input_image.get_noiseless_image("C:\\Users\\anany\Downloads\\ADNI1_Complete 2Yr 3T-003\Processed\\1","C:\\Users\\anany\Downloads\\ADNI1_Complete 2Yr 3T-003\Processed\\2")
input_image.do_segmentation("C:\\Users\\anany\Downloads\\ADNI1_Complete 2Yr 3T-003\Processed\\2","C:\\Users\\anany\Downloads\\ADNI1_Complete 2Yr 3T-003\Processed\\3")
input_image.return_2D_image("C:\\Users\\anany\Downloads\\ADNI1_Complete 2Yr 3T-003\Processed\\3","C:\\Users\\anany\Downloads\\ADNI1_Complete 2Yr 3T-003\Processed\\4")
