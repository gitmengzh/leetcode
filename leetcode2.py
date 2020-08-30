'''
被围绕的区域
'''

def solution(mult_list):
    if not mult_list or len(mult_list)<3 or mult_list[0]<3:
        return mult_list
    else:
        for i in range(1,len(mult_list)-2):
            for i in mult_list[i]:
                pass






if __name__ == "__main__":
    list0 = []
    list1 = [['X','O'],['O','X']]
    list2 = [['X','X','X'],
             ['X','O','X'],
             ['O','X','O']]
    print(solution(list0))