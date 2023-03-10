letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter: point for letter, point in zip(letters, points)}

letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for letter in word.upper():
    if letter_to_points.get(letter):
      point_total += letter_to_points[letter]
  return point_total

brownie_points = score_word("BROWNIE")

player_to_words = {"BLUE": ["earth", "ERAsER", "ZAP"], "TENNIS": ["EYES", "BELLY", "COMA"], "EXIT": ["MACHINE", "HUSKY", "PERIOD"]}

player_to_points = {}
for i, j in player_to_words.items():
  player_points = 0
  for word in j:
    player_points += score_word(word)
  player_to_points[i] = player_points

print(player_to_points)

def update_point_totals(player):
  player_points = 0
  for i in player_to_words[player]:
    player_points += score_word(i)
  return player_points

def play_word(player, word):
  player_to_words[player].append(word)

print(update_point_totals("BLUE"))




