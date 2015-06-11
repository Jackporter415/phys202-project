
# coding: utf-8

# In[1]:

import numpy as np
import random
from ipythonblocks import BlockGrid as BG
from IPython.html import widgets


# In[2]:

def make_num_grid(width,height,Red_perc,Blue_perc):
    grid = np.random.choice((0,1,2),size = (height,width), p = [1.00-((Red_perc+Blue_perc)/100),Red_perc/100,Blue_perc/100])
    return grid


# In[3]:

def near_me_num(grid,percent):

    i = 0
    j = 0
    moving_array = []
    moving_ZERO_array = []
    moving_ONE_array = []
    moving_TWO_array = []
    height = grid.shape[0]
    width = grid.shape[1]
    for row in range(0,height):
        for col in range(0,width):
            if grid[row,col] == 1:     
                    
                
                #Every row but first and last
                if (row != 0 and row != height-1) and (col != 0 and col != width-1) and (height !=2 and width != 2):
                    if grid[row-1,col] == 2:
                        i+=1
                    if grid[row+1,col] == 2:
                        i+=1
                    if grid[row,col+1] == 2:
                        i+=1
                    if grid[row,col-1] == 2:
                        i+=1
                    if grid[row+1,col+1] == 2:
                        i+=1
                    if grid[row+1,col-1] == 2:
                        i+=1
                    if grid[row-1,col+1] == 2:
                        i+=1
                    if grid[row-1,col+1] == 2:
                        i+=1
                        
                    if i/8 >= percent/100:
                        moving_ONE_array.append((row,col))

                    i = 0
                    
                #Upper Left Corner        
                if row == 0 and col == 0:
                    if grid[row+1,col] == 2:
                        i+=1
                    if grid[row+1,col+1] == 2:
                        i+=1
                    if grid[row,col+1] == 2:
                        i+=1
                        
                    if i/3 >= percent/100:
                        moving_ONE_array.append((row,col))

                    i = 0
                    
                #Lower Left Corner        
                if row == height-1 and col == 0:
                    if grid[row-1,col] == 2:
                        i+=1
                    if grid[row-1,col+1] == 2:
                        i+=1
                    if grid[row,col+1] == 2:
                        i+=1
                        
                    if i/3 >= percent/100:
                        moving_ONE_array.append((row,col))
                    i = 0
                    
                #Upper Right Corner        
                if col == width-1 and row == 0:
                    if grid[row+1,col] == 2:
                        i+=1
                    if grid[row+1,col-1] == 2:
                        i+=1
                    if grid[row,col-1] == 2:
                        i+=1
                        
                    if i/3 >= percent/100:
                        moving_ONE_array.append((row,col))
                    i = 0   
                    
                #Lower Right Corner
                if col == width-1 and row == height-1:
                    if grid[row-1,col] == 2:
                        i+=1
                    if grid[row-1,col-1] == 2:
                        i+=1
                    if grid[row,col-1] == 2:
                        i+=1
                        
                    if i/3 >= percent/100:
                        moving_ONE_array.append((row,col))
                    i = 0    
                    
                #First col, no corners        
                if col == 0 and (row!= 0 and row!= height-1):
                    if grid[row+1,col] == 2:
                        i+=1
                    if grid[row+1,col+1] == 2:
                        i+=1
                    if grid[row,col+1] == 2:
                        i+=1
                    if grid[row-1,col+1] == 2:
                        i+=1
                    if grid[row-1,col] == 2:
                        i+=1
                        
                    if i/5 >= percent/100:
                        moving_ONE_array.append((row,col))
                    i = 0    
                    
                #Bottom row, no corners
                if row == height-1 and (col != 0 and col != width-1):
                    if grid[row,col-1] == 2:
                        i+=1
                    if grid[row-1,col-1] == 2:
                        i+=1
                    if grid[row-1,col] == 2:
                        i+=1
                    if grid[row-1,col+1] == 2:
                        i+=1
                    if grid[row,col+1] == 2:
                        i+=1
                        
                    if i/5 >= percent/100:
                        moving_ONE_array.append((row,col))
                    i = 0    
                    
                #Last col, no corners
                if col == width-1 and (row != 0 and row != height-1):
                    if grid[row+1,col] == 2:
                        i+=1
                    if grid[row+1,col-1] == 2:
                        i+=1
                    if grid[row,col-1] == 2:
                        i+=1
                    if grid[row-1,col-1] == 2:
                        i+=1
                    if grid[row-1,col] == 2:
                        i+=1
                        
                    if i/5 >= percent/100:
                        moving_ONE_array.append((row,col))
                    i = 0  
                    
                #First row, no corners
                if row == 0 and (col != 0 and col != width-1):
                    if grid[row,col-1] == 2:
                        i+=1
                    if grid[row+1,col-1] == 2:
                        i+=1
                    if grid[row+1,col] == 2:
                        i+=1
                    if grid[row+1,col+1] == 2:
                        i+=1
                    if grid[row,col+1] == 2:
                        i+=1
                        
                    if i/5 >= percent/100:
                        moving_ONE_array.append((row,col))
                    i = 0

                
                
            if grid[row,col] == 2:

                
                #Every row but first and last
                if (row != 0 and row != height-1) and (col != 0 and col != width-1) and (height !=2 and width != 2):
                    if grid[row-1,col] == 1:
                        j+=1
                    if grid[row+1,col] == 1:
                        j+=1
                    if grid[row,col+1] == 1:
                        j+=1
                    if grid[row,col-1] == 1:
                        j+=1
                    if grid[row+1,col+1] == 1:
                        j+=1
                    if grid[row+1,col-1] == 1:
                        j+=1
                    if grid[row-1,col+1] == 1:
                        j+=1
                    if grid[row-1,col+1] == 1:
                        j+=1
                        
                    if j/8 >= percent/100:
                        moving_TWO_array.append((row,col))
                    j = 0    
                    
                #Upper Left Corner        
                if row == 0 and col == 0:
                    if grid[row-1,col] == 1:
                        j+=1
                    if grid[row-1,col+1] == 1:
                        j+=1
                    if grid[row,col+1] == 1:
                        j+=1
                        
                    if j/3 >= percent/100:
                        moving_TWO_array.append((row,col))
                    j = 0    
                    
                #Lower Left Corner        
                if row == height-1 and col == 0:
                    if grid[row-1,col] ==1:
                        j+=1
                    if grid[row-1,col+1] == 1:
                        j+=1
                    if grid[row,col+1] == 1:
                        j+=1
                        
                    if j/3 >= percent/100:
                        moving_TWO_array.append((row,col))
                    j = 0    
                    
                #Upper Right Corner        
                if col == width-1 and row == 0:
                    if grid[row-1,col] == 1:
                        j+=1
                    if grid[row-1,col-1] == 1:
                        j+=1
                    if grid[row,col-1] == 1:
                        j+=1
                        
                    if j/3 >= percent/100:
                        moving_TWO_array.append((row,col))
                    j = 0   
                    
                #Lower Right Corner
                if col == width-1 and row == height-1:
                    if grid[row-1,col] == 1:
                        j+=1
                    if grid[row-1,col-1] == 1:
                        j+=1
                    if grid[row,col-1] == 1:
                        j+=1
                        
                    if j/3 >= percent/100:
                        moving_TWO_array.append((row,col))
                    j = 0    
                    
                #First col, no corners        
                if col == 0 and (row!= 0 and row!= height-1):
                    if grid[row+1,col] == 1:
                        j+=1
                    if grid[row+1,col+1] ==1:
                        j+=1
                    if grid[row,col+1] == 1:
                        j+=1
                    if grid[row-1,col+1] == 1:
                        j+=1
                    if grid[row-1,col] == 1:
                        j+=1
                        
                    if j/5 >= percent/100:
                        moving_TWO_array.append((row,col))
                    j = 0  
                    
                #Bottom row, no corners
                if row == height-1 and (col != 0 and col != width-1):
                    if grid[row,col-1] == 1:
                        j+=1
                    if grid[row-1,col-1] == 1:
                        j+=1
                    if grid[row-1,col] == 1:
                        j+=1
                    if grid[row-1,col+1] == 1:
                        j+=1
                    if grid[row,col+1] == 1:
                        j+=1
                        
                    if j/5 >= percent/100:
                        moving_TWO_array.append((row,col))
                    j = 0  
                    
                #Last col, no corners
                if col == width-1 and (row != 0 and row != height-1):
                    if grid[row+1,col] == 1:
                        j+=1
                    if grid[row+1,col-1] == 1:
                        j+=1
                    if grid[row,col-1] == 1:
                        j+=1
                    if grid[row-1,col-1] == 1:
                        j+=1
                    if grid[row-1,col] == 1:
                        j+=1
                        
                    if j/5 >= percent/100:
                        moving_TWO_array.append((row,col))
                    j = 0   
                    
                #First row, no corners
                if row == 0 and (col != 0 and col != width-1):
                    if grid[row,col-1] == 1:
                        j+=1
                    if grid[row+1,col-1] == 1:
                        j+=1
                    if grid[row+1,col] == 1:
                        j+=1
                    if grid[row+1,col+1] == 1:
                        j+=1
                    if grid[row,col+1] == 1:
                        j+=1
                        
                    if j/5 >= percent/100:
                        moving_TWO_array.append((row,col))
                    j = 0    
            if grid[row,col] == 0:
                moving_ZERO_array.append((row,col))

    
    return grid, moving_ZERO_array, moving_ONE_array, moving_TWO_array


# In[4]:

test_grid = np.array([[1,1,1],[2,2,2],[1,1,1]])
print (test_grid)
near_test = near_me_num(test_grid,50)
assert near_test[3][0] == (1,0)
assert near_test[3][1] == (1,1)
assert near_test[2][0] == (0,0)
assert near_test[2][1] == (0,1)


# In[5]:

def Meathead_Movers(newgrid, array0, array1, array2):
    i = 0
    j = 0
    k = 0
    np.random.shuffle(array0)
    np.random.shuffle(array1)
    np.random.shuffle(array2)
    LEN_A0 = len(array0)
    LEN_A1 = len(array1)
    LEN__A1 = len(array1)-1
    LEN_A2 = len(array2)
    if LEN_A1 < LEN_A2 and LEN_A0 != 0:

        while i <= LEN_A1-1:
        
            newgrid[array1[i]] = 2
            newgrid[array2[k]] = 1

            #print ("MOVED",array1[i],1,array2[k],2)
            i+=1
            k+=1
        while i >= LEN_A1 and i < LEN_A2:
        
            newgrid[array0[j]] = 2
            newgrid[array2[i]] = 0
            #print ("MOVED",array2[i],0)

            i+=1
            j+=1
    if LEN_A1 > LEN_A2 and LEN_A0 != 0:

        while i <= LEN_A2-1:

            newgrid[array1[i]] = 2
            newgrid[array2[k]] = 1
            #print ("MOVED",array1[i],1,array2[i],2)
            i+=1
            k+=1
            
        while LEN__A1 > LEN_A1:
            
            if LEN_A0 == 0:
                break
            newgrid[array0[j]] = 1
            newgrid[array1[LEN__A1-1]] = 0
            #print ("MOVED",array1[LEN__A1-1],1,array0[j],0)
            yy -=1
            j+=1

    if LEN_A2 == LEN_A1:
        np.random.shuffle(array1)

        while i < LEN_A2:

            newgrid[array1[i]] = 2
            newgrid[array2[i]] = 1
            #print ("MOVED",array1[i],1,array2[i],2)
            i+=1
    if LEN_A0 == 0:
        if LEN_A1 < LEN_A2:

            while i <= LEN_A1-1:

                newgrid[array1[i]] = 2
                newgrid[array2[i]] = 1

                #print ("MOVED",array1[i],1,array2[k],2)
                i+=1
                k+=1
        if LEN_A1>=LEN_A2:

            while i <= LEN_A2-1:
                
                newgrid[array1[i]] = 2
                newgrid[array2[i]] = 1
                #print ("MOVED",array1[i],1,array2[i],2)
                i+=1
                k+=1
                
    return newgrid


# In[6]:

meat_time = Meathead_Movers(*near_test)
print (meat_time)
assert meat_time[1,0] != 2
assert meat_time[1,1] != 2
assert meat_time[1,2] != 2


# In[7]:

def colorful(grid):
    f = BG(grid.shape[1],grid.shape[0],fill=(0, 0, 0),block_size=4)
    for row in range(f.height):
        for col in range(f.width):
            sq = f[row,col]
            
            if grid[row,col] == 1:
                sq.blue = 900000000
            if grid[row,col] == 2:
                sq.red = 900000000
    return f


# In[ ]:



