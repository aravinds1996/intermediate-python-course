import random

def main():
  number_dice =2
  dice_sum =0
  for i in range(0,number_dice):  
    roll=random.randint(1,6)
    dice_sum+=roll
    if(roll==1):
      print(f'You rolled a {roll}! Critical Fail!')
    elif(roll==6):
      print(f'You rolled a {roll}! Critical Sucess!')
    else: 
      print(f'You rolled a {roll}')
  print(f'The sum is {dice_sum}')

if __name__== "__main__":
  main()
