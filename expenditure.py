days = int(input("please enter the number of days that you are going to stay for {in numbers}  :  "))
total_hotel_cost= 7200*days

print("we have two options  available: press 1  for Dubai and 2 for Kochin ")
choice = input()
total_plane_cost= 0 
if choice=="1" :
    total_plane_cost=1800097088797
else: 
    total_plane_cost=7787878787878
print("total cost is " , total_hotel_cost+total_plane_cost)
 