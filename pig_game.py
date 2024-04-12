#PIG dice game
import random

#generating player
class Player:
  def __init__(self, name):
    self.points = []
    self.total_score = 0
    self.name = name

#roll method
  def roll(self):
    roll = random.randint(1, 6)
    print(f'{self.name} rolled {roll}')
    if roll == 1:
      self.points.clear()
      return roll
    else:
      self.points.append(roll)
      return roll

  #decision method
  def decision(self):
    possible_answers = ('y', 'n')
    while True:
      print(f'Round score: {sum(self.points)}')
      decision = input(f'{self.name}, do you want to roll the dice again? (y/n)')
      if decision in possible_answers:
        return decision

  #round for one player
  def round(self):
    decision = 'y'
    while decision == 'y' and (self.total_score + sum(self.points)) < winning_sum:
        print(self.points)
        roll_result = self.roll()
        if roll_result == 1:
          print('Round points cleared :( ')
          print(f'Total score: {self.total_score}')
          break
        else:
          decision = self.decision()
          if decision == 'n':
            self.total_score += sum(self.points)
            self.points.clear()
            print(f'Total score: {self.total_score}')
            break

#generating players
Maja = Player('Maja')
Antoni = Player('Antoni')


#The game
#player wins if sum of points >= winning_sum
winning_sum = 20
while True:
    Maja.round()
    print(f"{Maja.name} total score: {Maja.total_score}, current round points: {sum(Maja.points)}")
    if (Maja.total_score + sum(Maja.points)) >= winning_sum:
        print(f"{Maja.name} wins!")
        break

    Antoni.round()
    print(f"{Antoni.name} total score: {Antoni.total_score}, current round points: {sum(Antoni.points)}")
    if Antoni.total_score + sum(Antoni.points) >= winning_sum:
        print(f"{Antoni.name} wins!")
        break