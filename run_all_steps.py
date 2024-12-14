import os

print('\n*** Step 1. Prepare Data 🌏 ***')
os.chdir('step1_prepare')
print(os.path.basename(__file__), f'os.getcwd(): {os.getcwd()}')
import step1_prepare.step1_1_download_data
#import step1_prepare.step1_2_preprocess_data

# Step 1.3 Split Data
import step1_prepare.step1_3_split_data
step1_prepare.step1_3_split_data.split_multiple_files(input_directory='.')


print('\n*** Step 2. Train Model 🌏🚀 ***')
#os.chdir('../step2_train')
#print(os.path.basename(__file__), f'os.getcwd(): {os.getcwd()}')
# TODO

print('\n*** Step 3. Make Prediction 🌏 🚀✨ ***')
#os.chdir('../step3_predict')
#print(os.path.basename(__file__), f'os.getcwd(): {os.getcwd()}')
# TODO
