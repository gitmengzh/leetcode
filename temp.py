def diffDicts2(dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        if not dict1 and not dict2:
            return None, None, None
        elif not dict1:
            return None, dict2, dict2
        elif not dict2:
            return dict1, None, dict1
        else:
            only_dict1_has = {}
            only_dict2_has = {}
            all_dict = {}
            for i in dict1.keys():
                if i not in dict2.keys():
                    only_dict1_has[i] = dict1[i]
                else:
                    pass



    else:
        return "类型不正确"







if __name__ == "__main__":
    # dict1 = {1: 'A', 3: 'C'}
    dict1 = []
    dict2 = {1: 'A', 2: 'B'}
    res = diffDicts2(dict1, dict2)
    print(res)