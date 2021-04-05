from pymongo import MongoClient;

client = MongoClient()
db = client.restaurant

class Sandwich:
  def __init__(self):

  def describe(self):
    print("Voici la composition de votre sandwich:")
    print("BASE      :")
    print("          : {}".format(self.base))
    print("CONDIMENTS:")
    print("          : {}".format(self.condiments))
    print("SAUCES    :")
    print("          : {}".format(self.sauces))
    print("")

  def cost(self):
    cost = 0
    for k,v in self.condiments.items():
      cost += v.get("price")
    
    for k,v in self.base.items():
      cost += v

    for k,v in self.sauces.items():
      cost += v
    print(cost)
    return cost

kebab = Sandwich()
kebab.base = kebab.base["galette"]
kebab.sauces = kebab.sauces["blanche"]
kebab.describe()
kebab.cost()