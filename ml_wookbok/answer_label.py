def add_name(pred):
    if pred == 0:
        label = '18歳未満'
    elif pred == 1:
        label = '18歳~25歳'
    elif pred == 2:
        label = '26歳 ~ 30歳'
    elif pred == 3:
        label = '30歳 ~ 35歳'
    elif pred == 4:
        label =  '36歳 ~ 40歳'
    elif pred == 5:
        label =  '41歳 ~ 45歳'
    elif pred == 6:
        label =  '46歳 ~ 55歳'
    elif pred == 7:
        label =  '56歳 ~ 65歳'
    elif pred == 8:
        label =  '65歳以上'
    return label
