import numpy as np
import pandas as pd
import shap
import joblib
import os.path
from os import path
from csv import writer

top_feat = ['happy',
 'Avg. # of Ment.Unhealth. Days',
 'anxiety_increase',
 'work_hrs',
 'age',
 'stress_future',
 'stress_home',
 'satisfied',
 'gender',
 'children']

explainer_path = r'C:\Users\etb4205\Desktop\projects\hackathon\humana_hackathon_2021\resources\model\explainer_final.joblib'
model_path = r'C:\Users\etb4205\Desktop\projects\hackathon\humana_hackathon_2021\resources\model\model_final.joblib'
output_path = r'C:\Users\etb4205\Desktop\projects\hackathon\humana_hackathon_2021\output\output.csv'

def get_model_output(
               name_input: str,
               happy: int,
               Unhealth_Days: int,
               anxiety_increase: int,
               work_hrs: int,
               age: int,
               stress_future: int,
               stress_home: int,
               satisfied: int,
               gender: int,
               children: int
):
    prediction_output = None
    test_df = pd.DataFrame({
        'happy': [happy],
        'Avg. # of Ment.Unhealth. Days': [Unhealth_Days],
        'anxiety_increase': [anxiety_increase],
        'work_hrs': [work_hrs], 'age': [age],
        'stress_future': [stress_future],
        'stress_home': [stress_home],
        'satisfied': [satisfied],
        'gender': [gender],
        'children': [children]
    })

    rfr = joblib.load(model_path)
    try:
        click_value = rfr.predict(test_df)
    except:
        return 0

    if click_value >= 1:
        output = click_value
        prediction_output = output
        # if output <= 1:
        #     output_category = "low"
        #     category_suggestions = "" \
        #                            "Because your mental health risk score is low, it is suggested that you to " \
        #                            "continue to take care of yourself in the same manner. Should anything change, " \
        #                            "feel free to complete the assessment again."
        # elif output <= 3:
        #     output_category = "moderate"
        #     category_suggestions = "" \
        #                            "Because your mental health score is moderate, it is suggested that you "
        # elif output <= 6:
        #     output_category = "high"
        #     category_suggestions = "" \
        #                            "Because your mental health risk score is high, "
        # else:
        #     output_category = "very high"
        #     category_suggestions = "" \
        #                            "Because your mental health risk score is very high, "
      #   return u'''
      #     {}, your mental health risk score is: {}, which is considered {} on our scale. Please check our
      #     resources tab for more information on ways to improve your mental health and get help during the pandemic.
      #     {}
      # '''.format(name_input, output, output_category, category_suggestions)
    top_factor_1, top_factor_2, top_factor_3, top_factor_val_1, top_factor_val_2, top_factor_val_3 = generate_explanations(test_df.values)
    test_df_values = test_df.values[0].tolist()
    extra_factors_values = [top_factor_1, top_factor_2, top_factor_3, top_factor_val_1, top_factor_val_2,
                            top_factor_val_3, prediction_output[0]]

    csv_row = test_df_values + extra_factors_values
    save_data(csv_row)
    return int(prediction_output[0])

def generate_explanations(input_arr: np.array):
    explainer = joblib.load(explainer_path)
    shap_values = explainer.shap_values(input_arr[0])
    abs_shap_values = np.abs(shap_values)
    shap_feature_dict = dict(zip(top_feat, abs_shap_values))
    sorted_dict = {k: v for k, v in sorted(shap_feature_dict.items(), key=lambda item: item[1])}
    sorted_dict_vals = list(sorted_dict.values())
    sorted_dict_keys = list(sorted_dict.keys())
    top_factor_1, top_factor_2, top_factor_3 = sorted_dict_keys[-3:]
    top_factor_val_1, top_factor_val_2, top_factor_val_3 = sorted_dict_vals[-3:]



    return top_factor_1, top_factor_2, top_factor_3, top_factor_val_1, top_factor_val_2, top_factor_val_3

def save_data(csv_row, output_path=output_path):
    exists_path = path.exists(output_path)
    if exists_path:
        df = pd.read_csv(output_path)
        df.loc[len(df)-1, :] = csv_row
    else:
        df = pd.DataFrame(columns=['happy', 'Avg. # of Ment.Unhealth. Days', 'anxiety_increase',
       'work_hrs', 'age', 'stress_future', 'stress_home', 'satisfied',
       'gender', 'children', 'top_factor_1', 'top_factor_2', 'top_factor_3', 'top_factor_val_1', 'top_factor_val_2', 'top_factor_val_3', 'prediction_output'])
        df.loc[0, :] = csv_row
        df.to_csv(output_path)



# if __name__ == '__main__':
#     output_ = get_model_output('eshan', 1, 20, 1, 1, 10, 30, 1, 0, 0, 1)
#     print(output_[0])