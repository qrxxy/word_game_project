

def create_graph(startingWord, targetWord):

    with open("data/four_letter_words.txt", "r") as file:
        words = set(file.read().splitlines())

    graph = {}
    graph[startingWord] = set()
    queue = [startingWord]
    visited = set()
    visited.add(startingWord)
    while queue:
        sWord = queue.pop(0)
        for j in range(len(sWord)):
            for i in range(ord("a"), ord("z") + 1):
                letter = chr(i)
                word = sWord[:j] + letter + sWord[j+1:]
                if word in words and word != sWord:

                    if word not in visited:
                        queue.append(word)
                        graph[word]= set()
                        visited.add(word)

                    graph[sWord].add(word)
                    graph[word].add(sWord)

    return graph

graph = create_graph("word", "word")

print(graph["word"])
print(len(graph))





