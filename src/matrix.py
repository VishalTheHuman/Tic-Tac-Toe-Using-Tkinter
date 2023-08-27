class matrix:
    def __init__(self):
        self.matrix = [[None for y in range(3)] for x in range(3)]
        self.x_score = 0
        self.o_score = 0
    
    def __str__(self):
        ret_str = ""
        for r in self.matrix:
            for c in r:
                if c is None:
                    ret_str+="_ "
                elif c == 0:
                    ret_str+="O "
                elif c == 1:
                    ret_str+="X "
            ret_str+='\n'
        return ret_str
    
    
    def check(self,row,col):
        return self.matrix[row][col] == None
    
    def set_X(self,row,col):
        if self.check(row,col):
            self.matrix[row][col] = 1
            return True
        else:
            return False
    
    def set_O(self,row,col):
        if self.check(row,col):
            self.matrix[row][col] = 0
            return True
        else:
            return False
    
    def remove(self,row,col):
        self.matrix[row][col] = None
    
    def reset(self):
        self.matrix = [[None for y in range(3)] for x in range(3)]
        self.print()
    
    def check_X_Win(self):
        count = 0
        count1 = 0
        # Diagonal
        for x in range(3):
            if self.matrix[x][x] == 1:
                count+=1
            if self.matrix[x][2-x] == 1:
                count1+=1
        if count==3:
            return True
        if count1==3:
            return True
        
        # Row and Column
        for x in range(3):
            count = 0
            count1 = 0
            for y in range(3):
                if self.matrix[x][y] == 1:
                    count+=1
                if self.matrix[y][x] == 1:
                    count1+=1
            if count==3 or count1==3:
                return True
        return False
    
    def check_O_Win(self):
        count = 0
        count1 = 0
        # Diagonal
        for x in range(3):
            if self.matrix[x][x] == 0:
                count+=1
            if self.matrix[x][2-x] == 0:
                count1+=1
        if count==3:
            return True
        if count1==3:
            return True
        
        # Row and Column
        for x in range(3):
            count = 0
            count1 = 0
            for y in range(3):
                if self.matrix[x][y] == 0:
                    count+=1
                if self.matrix[y][x] == 0:
                    count1+=1
            if count==3 or count1==3:
                return True
        return False
    
    def check_win(self):
        if self.check_X_Win():
            return 1
        elif self.check_O_Win():
            return 0
        else:
            return None
    
    def check_draw(self):
        if not(self.check_O_Win() or self.check_X_Win()):
            count = 0
            for x in range(3):
                for y in range(3):
                    if self.matrix[x][y] is None or self.matrix[x][y]==-1:
                        count+=1
            return count==0
        else:
            return False
    
    def set_neg_one(self):
        for x in range(3):
            for y in range(3):
                self.matrix[x][y]=-1
    
    def print(self):
        print(self)