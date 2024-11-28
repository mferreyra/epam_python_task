import pytest
from tasks import Dictionary, get_total_cost, word_from_list


def test_Dictionary_new_entry():
    d = Dictionary()
    d.newentry("Apple", "A fruit that grows on trees")
    assert(d.look("Apple") == "A fruit that grows on trees")
 

def test_Dictionary_lookup_no_entry():
    d = Dictionary()
    d.newentry("Apple", "A fruit that grows on trees")
    assert(d.look("Banana") == "Can't find entry for Banana")


def test_dictionary_empty_lookup():
    d = Dictionary()
    assert(d.look() == "Please input a key for lookup")


def test_get_total_cost():
    costs = {"socks":5, "shoes":60, "sweater":30}
    assert(get_total_cost(costs, ["socks", "shoes", "other_item", "----------"], 0.09) == 70.85)


def test_get_total_cost_no_items():
    costs = {"socks": 5, "shoes": 60, "sweater": 30}
    assert(get_total_cost(costs, [], 0.09) == 0.00)


def test_word_from_list():
    my_list = ["yoda", "best", "has"]
    assert(word_from_list(my_list) == "yes")
