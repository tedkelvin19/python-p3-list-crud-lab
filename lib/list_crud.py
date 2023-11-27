def create_an_empty_list():
    # Create an empty list
    empty_list = []
    
    # Return the empty list
    return empty_list

def create_a_list():
    my_list = []

    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    return my_list

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l[0]=element
    return l 

def remove_element_from_end_of_list(l):
    l.pop()
    return l

def remove_element_from_start_of_list(l):
    l.pop(0)
    return l

def retrieve_first_element_from_list(l):
    a = l[0] 
    return a

def retrieve_element_from_index(l, index):
    element = l[index]
    return element

def retrieve_last_element_from_list(l):
    last = l[-1]
    return last
