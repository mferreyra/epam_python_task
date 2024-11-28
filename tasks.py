### Solutions to Python tasks ###


##### Task 1 #####

class Dictionary():
    """Add words to Dictionary and their entries"""

    def __init__(self):
        self.words = {}

    def newentry(self, key:str, value:str):
        self.words[key] = value

    def look(self, key:str):
        if key in self.words:
            return self.words[key]
        else:
            return f"Can´t find entry for {key}"


##### Task 2 #####

def get_total_cost(costs:dict, items:list, tax:float) -> float:
    """Input: Dictionary of items and their costs, list of items bought, tax.
        Note: If the item doesn´t exitst in the given cost values, the item is ignored.
        Output: Total costs of the items plus tax, rounded to two decimal places."""
    
    total_cost = 0
    for item in items:
        if item in costs:
            total_cost += costs[item]  
    total_cost = total_cost + total_cost * tax

    return round(total_cost, 2)


##### Task 3 #####

def word_from_list(words:list) -> str:
    """Input: list of strings
       Output: new string with the n th letter from each input string"""
    
    new_word = ""
    for index in range(len(words)):
        new_word += words[index][index]
    
    return new_word
