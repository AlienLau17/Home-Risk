# Create your views here.
from django.shortcuts import render
import pandas as pd
import json

def index(request):
    return render(request, 'homepage.html')

def gohome(request):

    return render(request, 'homepage.html')

def report(request):
    if request.method == 'POST':
        input_id = int(request.POST.get('user_id'))

        user_file = pd.read_csv('/home/jl5175/AdvBigdata/web/advbigdata/homerisk/test_info.csv')
        length = len(user_file)
        major_index = {}
        # build a major_index dictionary
        for i in range(0, length):
           uid = user_file['SK_ID_CURR'][i]
           major_index[uid] = i

        if input_id in major_index.keys():
            # 1. get info
            info_row = user_file.iloc[major_index[input_id]]
            data1 = json.loads(info_row.to_json())

            # 2. get bureau
            bureau_file = pd.read_csv('/home/jl5175/AdvBigdata/web/advbigdata/homerisk/test_bureau1.csv')
            bureau_rows = bureau_file.loc[bureau_file['SK_ID_CURR'] == input_id]
            bureau_rows = bureau_rows.drop('SK_ID_CURR', axis=1)
            bureau_cols = list(bureau_rows.columns.values)
            bureau_dict = {}
            for i in bureau_cols:
                bureau_dict[i] = []

            for j in range(len(bureau_rows)):
                temp_val = list(bureau_rows.iloc[j])
                #     print(temp_val)
                for k in range(len(bureau_cols)):
                    key = bureau_cols[k]
                    #         print(key)
                    bureau_dict[key].append(temp_val[k])
            data2 = {**data1, **bureau_dict}

            # 3. get credit
            credit_file = pd.read_csv('/home/jl5175/AdvBigdata/web/advbigdata/homerisk/test_credit.csv')
            credit_rows = credit_file.loc[credit_file['SK_ID_CURR'] == input_id]
            credit_rows = credit_rows.drop('SK_ID_CURR', axis=1)
            prev_id = credit_file['SK_ID_PREV'].iloc[0]
            data2['SK_ID_PREV_CREDIT'] = prev_id
            credit_rows = credit_rows.drop('SK_ID_PREV', axis=1)

            cols = list(credit_rows.columns.values)
            credit_dict = {}
            for i in cols:
                credit_dict[i] = []

            for j in range(len(credit_rows)):
                temp_val = list(credit_rows.iloc[j])
                #     print(temp_val)
                for k in range(len(cols)):
                    key = cols[k]
                    #         print(key)
                    credit_dict[key].append(temp_val[k])
            data = {**data2, **credit_dict}

        else:
            return render(request, 'homepage.html')

    return render(request, 'report.html', data)

# data = {'uid': temp_row['SK_ID_CURR'],# e.g 100001
#         'sex': temp_row['CODE_GENDER'],# e.g F
#         'loan_type': temp_row['NAME_CONTRACT_TYPE'],# e.g Cash loans
#         'flag_car': temp_row['FLAG_OWN_CAR'],# e.g Y
#         'flag_reality': temp_row['FLAG_OWN_REALTY'],# e.g
#         'num_children': temp_row['CNT_CHILDREN'],# e.g
#         'total_income': temp_row['AMT_INCOME_TOTAL'],# e.g
#         'total_credit': temp_row['AMT_CREDIT'],# e.g
#         'repay_annuity': temp_row['AMT_ANNUITY'],# e.g
#         'good_price': temp_row['AMT_GOODS_PRICE'],# e.g
#         'age': int(-temp_row['DAYS_BIRTH'] / 365),# e.g
#         'education': temp_row['NAME_EDUCATION_TYPE']}


# Data columns (total 40 columns):
# SK_ID_CURR                    48744 non-null int64
# NAME_CONTRACT_TYPE            48744 non-null object
# CODE_GENDER                   48744 non-null object
# FLAG_OWN_CAR                  48744 non-null object
# FLAG_OWN_REALTY               48744 non-null object
# CNT_CHILDREN                  48744 non-null int64
# AMT_INCOME_TOTAL              48744 non-null float64
# AMT_CREDIT                    48744 non-null float64
# AMT_ANNUITY                   48720 non-null float64
# AMT_GOODS_PRICE               48744 non-null float64
# NAME_TYPE_SUITE               47833 non-null object
# NAME_INCOME_TYPE              48744 non-null object
# NAME_EDUCATION_TYPE           48744 non-null object
# NAME_FAMILY_STATUS            48744 non-null object
# NAME_HOUSING_TYPE             48744 non-null object
# DAYS_BIRTH                    48744 non-null int64
# DAYS_EMPLOYED                 48744 non-null int64
# DAYS_REGISTRATION             48744 non-null float64
# DAYS_ID_PUBLISH               48744 non-null int64
# OWN_CAR_AGE                   16432 non-null float64
# OCCUPATION_TYPE               33139 non-null object
# CNT_FAM_MEMBERS               48744 non-null float64
# REGION_RATING_CLIENT          48744 non-null int64
# WEEKDAY_APPR_PROCESS_START    48744 non-null object
# HOUR_APPR_PROCESS_START       48744 non-null int64
# ORGANIZATION_TYPE             48744 non-null object
# EXT_SOURCE_1                  28212 non-null float64
# EXT_SOURCE_2                  48736 non-null float64
# EXT_SOURCE_3                  40076 non-null float64
# FONDKAPREMONT_MODE            15947 non-null object
# HOUSETYPE_MODE                25125 non-null object
# WALLSMATERIAL_MODE            24851 non-null object
# EMERGENCYSTATE_MODE           26535 non-null object
# OBS_30_CNT_SOCIAL_CIRCLE      48715 non-null float64
# DEF_30_CNT_SOCIAL_CIRCLE      48715 non-null float64
# OBS_60_CNT_SOCIAL_CIRCLE      48715 non-null float64
# DEF_60_CNT_SOCIAL_CIRCLE      48715 non-null float64
# DAYS_LAST_PHONE_CHANGE        48744 non-null float64
# TARGET                        48744 non-null float64