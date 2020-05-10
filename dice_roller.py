import random

def main():
  dice_size =int(input('How many dice would you like to throw?'))
  dice_sum =0
  for i in range(0,dice_size):  
    roll=random.randint(1,6)
    dice_sum+=roll
    if(roll==1):
      print(f'You rolled a {roll}! Critical Fail!')
    elif(roll==dice_size):
      print(f'You rolled a {roll}! Critical Sucess!')
    else: 
      print(f'You rolled a {roll}')
  print(f'The sum is {dice_sum}')

if __name__== "__main__":
  main()
