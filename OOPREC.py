class record():
    def __init__(self , a , cols_name , cols_point):
        self.list_student = a
        self.name = cols_name
        self.point = cols_point
        self.list_name_point = []
    def throw_vals(self):
        for i in range(len(self.list_student)):
            self.list_in_loop = []
            for y in range(3):
                if self.list_student[i][y] == self.list_student[i][self.name]:
                    self.list_in_loop.append(self.list_student[i][y])
                elif self.list_student[i][y] == self.list_student[i][self.point]:
                    self.list_in_loop.append(self.list_student[i][y])
                    self.list_name_point.append(self.list_in_loop)
        print("ADD NAME AND POINT =>  ",self.list_name_point)
    def cal_grade(self):
        for i in range(len(self.list_name_point)):
            for y in range(2):
                if self.list_name_point[i][y] == self.list_name_point[i][1]:
                    if self.list_name_point[i][1] >= 60:
                        print("{} PASS BY SCORE {}".format(self.list_name_point[i][0] ,self.list_name_point[i][1]))
                    else:
                        print("{} NOT PASS BY SCORE {}".format(self.list_name_point[i][0] ,self.list_name_point[i][1]))
if __name__ == '__main__':
    rec = [["student1" , "Math" , 300] ,["student2" , "Math" , 20] , ["student3" , "Math" , 0] ,["student4" , "Math" , 1] ,["student5" , "Math" , 2] , ["student6" , "Math" , 3]]
    use = record(rec , 0 , 2)
    use.throw_vals()
    use.cal_grade()