import matplotlib.pyplot as plt
import random

# random name generation
names = ["alf", "ons", "br", "ut", "cyr", "il", "do", "ra", "el", "sa", "fra",
         "nta", "gert", "ruda", "ha", "nz", "iv", "eta", "jo", "sef", "ka",
         "rel", "lou", "da", "mou", "rek", "no", "ra", "or", "paj", "da", "qui",
         "do", "ras", "tik", "ur", "za", "va", "sil"]

# function name generation

def r_name():
  return f"{random.choice(names).capitalize()}{random.choice(names)}"


#l list of character races
races = ["elf", "troll", "velociraptor"]

# function race generation


def r_race():
  return random.choice(races)


# list of characters from selected
training = ["mage", "warrior"]

# function defense / attack


def r_trained():
  return random.choice(training)


# list weapons
weapons = ["axe", "broadsword", "dagger"]

# function of generating weapons


def r_weapon():
  return random.choice(weapons)


# list armor
armours = ["leather", "plate", "ring"]

# funciton of generating armor


def r_armour():
  return random.choice(armours)

# function d roll attacking magic


def roll_d20_magic():
  roll = random.randint(1, 20)
  if roll == 1:
    return 0.5
  elif roll < 8:
    return 1
  elif roll < 14:
    return 1.5
  elif roll < 20:
    return 2
  else:
    return 2.5

# function d roll attacking magic attack of defennse 


def roll_d20_attack_defense():
  roll = random.randint(1, 20)
  if roll == 1:
    return 0.75
  elif roll < 8:
    return 0.95
  elif roll < 14:
    return 1
  elif roll < 20:
    return 1.05
  else:
    return 1.25


class Hero:

  def __init__(self, team, r_name, r_race, r_trained, r_weapon, r_armour):
    self.team = team
    self.dead = False
    self.name = r_name

    self.race = r_race
    if self.race == "elf":
      self.intel = 10
      self.spd = 7
      self.stre = 4
      self.life = 180
    elif self.race == "troll":
      self.intel = 4
      self.spd = 4
      self.stre = 10
      self.life = 240
    elif self.race == "velociraptor":
      self.intel = 2
      self.spd = 10
      self.stre = 7
      self.life = 110

    self.weapon = r_weapon
    if self.weapon == "axe":
      self.weapon_attack = 6
      self.weapon_spd = 1.5
    elif self.weapon == "broadsword":
      self.weapon_attack = 8
      self.weapon_spd = 1
    elif self.weapon == "dagger":
      self.weapon_attack = 4
      self.weapon_spd = 2

    self.armour = r_armour
    if self.armour == "leather":
      self.armour_def = 4
      self.armour_spd = 2
    elif self.armour == "plate":
      self.armour_def = 9
      self.armour_spd = 0.75
    elif self.armour == "ring":
      self.armour_def = 7
      self.armour_spd = 1

    self.trained = r_trained

    self.info = (f"{self.team.capitalize()} {self.name}: {self.race}"
                 f" {self.trained} with {self.weapon} and {self.armour} armour")

# definition of listed life attack and defense
  def show_life(self):
    print(f"{self.team.capitalize()} {self.name}:{self.life}")

  def attack(self):
      if self.trained == "mage":
        return round(self.intel * 7 * roll_d20_magic())
      elif self.trained == "warrior":
        return round((self.stre + self.weapon_attack) *
                     (self.spd * self.weapon_spd) * roll_d20_attack_defense())

  def defense(self, hit):
      if hit > round(self.armour_def * (self.spd * self.armour_spd)):
        self.life = self.life - round(hit - (self.armour_def *
                                             (self.spd * self.armour_spd)))
        if self.life < 1:
          self.dead = True


# emptz hero
blue_heroes = []
red_heroes = []

print("""
\n\n  
        ______________________________________________________
        [[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]
        .-.`| `-/-.__/.-'\_.-._,'/`-._'\_.-._`-'_/-._.'|/.-'\-
        \_.-`./`-._'\__.-`-.__.-`--._/--.`-._\`-._\__.-)`-'._/
        `._-'.\_.---._-.\_`-..`\_.---._`-.__.-`'._.--./`-'._,'
        __/`.-/       `.'_`./`.'       '.\__.-`.'    (_.-\_,-.
        `._-/'          |._.-|           |.'`.|       `(_.`-._
        .-',`)          | /`.|           |`-/`|         ;.-'_/
        `\,-/           |\.-'|           |\-'`|          ;\_,-
         -./`._        [[[[[[[[         [[[[[[[[         .',-'
         `.`--.~~-^_~-/.`-._`-.\^~-_~-^/`-.'-,.'\^~-~_^"'`-.'_
         -,.'"-"~^-~_~- - - _- -~^-_.~ - -_ - - -~- . "'"-"-""
         ""-'"-""-"~- _~.^-~-^.-^_.- .^~.-  ~-. ~^_-""-""-"'-"
         jgs ""-'"-"    ~- ^. - ~ -~^ - ~  ^~- ~     ""-"'-'



     88                     88          88                         
     88                     ""          88                         
     88                                 88                         
     88,dPPYba,  8b,dPPYba, 88  ,adPPYb,88  ,adPPYb,d8  ,adPPYba,  
     88P'    "8a 88P'   "Y8 88 a8"    `Y88 a8"    `Y88 a8P,,,,,88  
     88       d8 88         88 8b       88 8b       88 8PP 
     88b,   ,a8" 88         88 "8a,   ,d88 "8a,   ,d88 "8b,   ,aa  
     8Y"Ybbd8"'  88         88  `"8bbdP"Y8  `"YbbdP"Y8  `"Ybbd8"'  
                                            aa,    ,88             
                                             "Y8bbdP"              

        8b      db      d8 ,adPPYYba, 8b,dPPYba, ,adPPYba,
        `8b    d88b    d8' ""     `Y8 88P'   "Y8 I8[    ""
         `8b  d8'`8b  d8'  ,adPPPPP88 88         `"Y8ba,
          `8bd8'  `8bd8'   88,    ,88 88         aa    ]8I 
            YP      YP     `"8bbdP"Y8 88         `"YbbdP"'  \n\n\n                               
""")

team_size = int(input("Choose the size of teams:\n\n"))

print("\nHere comes the blue team!\n")


for n in range(1, (team_size + 1)):
  blue_heroes.append(Hero("blue", r_name(), r_race(), r_trained(),
                          r_weapon(), r_armour()))
for obj in blue_heroes:
    print(obj.info)

print("\n\nAnd this is the red team!\n")

for n in range(1, (team_size + 1)):
  red_heroes.append(Hero("red", r_name(), r_race(), r_trained(),
                         r_weapon(), r_armour()))
for obj in red_heroes:
    print(obj.info)

print("\n\nLet the fight begin!!!\n")

# kill counter
killed_blue = 0
killed_blue_progress = [team_size]
killed_red = 0
killed_red_progress = [team_size]

# function in runinng whole team is discharged
while killed_blue < team_size and killed_red < team_size:

  # function in running vhole hero is discharged
  while True:
    blue = blue_heroes[0]
    red = red_heroes[0]

    blue.show_life()
    red.show_life()
    print("\n")

    if blue.dead:
      print(f"{blue.team.capitalize()} {blue.name} is dead!")
      print("Blue team lost a hero!\n")
      killed_blue += 1
      killed_blue_progress.append(team_size - killed_blue)
      killed_red_progress.append(team_size - killed_red)
      del blue_heroes[0]
      break
    elif red.dead:
      print(f"{red.team.capitalize()} {red.name} is dead!")
      print("Red team lost a hero!\n")
      killed_red += 1
      killed_blue_progress.append(team_size - killed_blue)
      killed_red_progress.append(team_size - killed_red)

      del red_heroes[0]
      break
    else:
      if random.choice([True, False]):
        blue.defense(red.attack())
      else:
        red.defense(blue.attack())

# the elimination of one and the victory of the other team
if killed_blue == team_size:
  print("Everyone on the blue team is dead, red team wins!!!")
  print(f"{killed_red} heroes from the red team was killed.\n\n\n")

if killed_red == team_size:
  print("Everyone on the red team is dead, blue team wins!!!")
  print(f"{killed_blue} heroes from the red team was killed.\n\n\n")

#import knihovny pro tvorbu grafu

ax = plt.axes()
ax.set_facecolor("grey")

plt.plot(killed_blue_progress, c="blue")
plt.plot(killed_red_progress, c="red")
plt.xlabel("rounds", fontweight="bold")
plt.ylabel("heroes alive", fontweight="bold")
#plt.yticks(range(0,12,2))

plt.show()
