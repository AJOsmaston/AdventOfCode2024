from collections import deque

def plutonian_pebbles(file_text):
    initial_queue = get_initial_queue(file_text)
    
    
def get_initial_queue(file_text):
    numbers = file_text.split(" ")
    initial_queue = deque()
    for number in numbers:
        initial_queue.append(number)
    return initial_queue
    
