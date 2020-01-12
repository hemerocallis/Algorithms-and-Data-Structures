from collections import deque

graph = {}
graph["Lili"] = ["Iren", "Thom", "Ostin", "Elly"]
graph["Iren"] = ["Sam", "Lui"]
graph["Thom"] = []
graph["Ostin"] = []
graph["Elly"] = ["Petra", "Nino", "Liliya"]
graph["Petra"] = []
graph["Liliya"] = []
graph["Sam"] = []
graph["Lui"] = ["Billy", "Liliya"]
graph["Billy"] = []
graph["Nino"] = ["Ostina", "Serge"]
graph["Ostina"] = []
graph["Serge"] = ["Ivan"]
graph["Ivan"] = ["Liliana"]
graph["Liliana"] = []

def subStringCheck(name1, name2):
    if len(name1) >= name2:
        return False
    else:
        if name1 in name2:
            return True
        else:
            return False

def breadthFirstSearch(name):
    search_queue = deque()
    search_queue.extend(graph[name])
    checked = []
    while search_queue:
        person = search_queue.popleft()
        if not person in checked:
            if subStringCheck(name, person):
                print(name + " is clothest sub-string of " + person + ".")
                return True
            else:
                search_queue.extend(graph[person])
                checked.append(person)
    return False

breadthFirstSearch("Lili")
