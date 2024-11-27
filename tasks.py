### Solutions to Python tasks ###


##### Task 1 #####

class Dictionary():
    def __init__(self):
        self.words = {}

    def newentry(self, key:str, value:str):
        self.words[key] = value

    def look(self, key:str):
        if key in self.words:
            return self.words[key]
        else:
            return f"Can´t find entry for {key}"


#d = Dictionary()
#d.newentry('Apple', 'A fruit that grows on trees')
#print(d.look('Apple')) #output: A fruit that grows on trees
#print(d.look('Banana')) #output: Can´t find entry for Banana



##### Task 2 #####

def get_total_cost(costs:dict, items:list, tax:float):
    total_cost = 0
    for item in items:
        if item in costs:
            total_cost += costs[item]  
    total_cost = total_cost + total_cost * tax

    return total_cost


#costs = {'socks':5, 'shoes':60, 'sweater':30}
#print(get_total_cost(costs, ['socks', 'shoes', 'asdf'], 0.09))



##### Task 3 #####

def word_from_list(words:list):
    new_word = ""
    for index in range(len(words)):
        new_word += words[index][index]
    
    return new_word


#my_list = ["yoda", "best", "has"]
#print(word_from_list(my_list))
