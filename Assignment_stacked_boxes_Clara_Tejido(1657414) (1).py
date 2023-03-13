import sys
box_size = int(sys.argv[1])
grid_size = int(sys.argv[2])

n= int(box_size/2) #here I define a parameter that it is the half of the box size
l = int((box_size+1)/2) # I define a parameter to obtain an integer number dividing box_size/2, when the box_size is an odd number. 


#UPPER LINE OF THE BOX

if box_size==1:
 print("\n",end="") #when the box_size is 1, I build it with the function to make the bottom line (see below), so I skip it here

else:
 for i in range(0, grid_size): #I define the number of boxes (grid) I want to make in the horizontal axis  
  print("+", end="")
  for minus in range(0, box_size-2): #In the top line there are two "+", so the number of minus I make is the box_size-2
   print("-", end="")
 print("+\n",end="") #To make boxes consecutive, I make each loop with only the "+" at the beggining (so "+----"). 
                     # This last command prints a final "+" when the loop is finished and moves to the next line

# MIDDLE OF THE BOX

for boxes in range (0, grid_size): #Loop for the number of boxes (grid) in the vertical axis. 
                                   #In this loop I print the middle and bottom line parts (the upper line only prints the first line of the horizontal grid axis)
        
 if box_size%2==0: # EVEN NUMBER BOX SIZE
    
# top part of the half of the box  
  for space_side in range(0,n-1): #loop to print the number of elements corresponding to half of the box_size
   space_middle=(n-1)-(space_side+1) #I define that the space in the middle increases as the space on the sides decreases.
   print(("|" + " "*space_side + "\\" + " "*(2*space_middle) + "/" + " "*space_side) * grid_size + "|")
   #I multiply by the grid_size to print the corresponding number of boxes in the horizontal axis

# bottom part of the half of the box 

  for space_middle_2 in range(0,n-1):
   space_side_2=(n-1)-(space_middle_2 + 1) #now I invert the functions of before. So I increase the spaces in the sides as the middle space decreases
   print(("|" + " "*space_side_2 + "/" + " "*(2*space_middle_2) + "\\" + " "*space_side_2) * grid_size + "|")
    
        
 else: #ODD NUMBER BOX SIZE
    
# top part of the half of the box  
  for space_side in range(0,l-2): #I used the same function as before, so it increases one by one the space in the side in a range of half of the box_size-2
   space_middle=(box_size-2)-(space_side +2) #the space in the middle decreases by 2 in everyround of the loop
   print(("|" + " "*space_side + "\\" + " "*(space_middle-space_side) + "/" + " "*space_side) * grid_size + "|")

  if box_size!=1: #with box_size==1 each box should be just a "+", so it is too small to print an "X" in the middle
   print(("|" + " "*(l-2) + "X" + " "*(l-2)) * grid_size + "|")

# bottom part of the half of the box 
  for y in range(0,l-2):
   space_middle_2 = 1 + (y*2) #I define a function so all odd numbers have a +2 increment in the middle space (3,5,7,9 etc)
   space_side_2=(n-1)-(y+1) # the spaces in the sides decrease by one in everyloop
   print(("|" + " "*space_side_2 + "/" + " "*space_middle_2 + "\\" + " "*space_side_2) * grid_size + "|")


#BOTTOM LINE OF THE BOX
 if box_size!=1:
  for i in range(0, grid_size): #I define the number of boxes (grid) I want to make in the horizontal axis
   print("+", end="")
   for minus in range(0, box_size-2): #In the bottom line there are two "+" so I substract 2 to the size to make the minus
    print("-", end="")
  print("+\n",end="")

 else: #the box_size=1 is an special case in which only one "+" (in each horizontal and vertical axis) should be printed per box_grid
  for i in range(0, grid_size): 
   print("+", end="")
  print("\n",end="")


