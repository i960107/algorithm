from typing import List


class Habitat:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


width = 1001
height = 1001


def get_species_in_area(habitats: List[Habitat]) -> List[List[int]]:
    species = [[0] * width for _ in range(height)]
    for habitat in habitats:
        for i in range(habitat.y1, habitat.y2):
            for j in range(habitat.x1, habitat.x2):
                species[i][j] += 1

    return species


def soluiton(n: int, k: int, habitats: List[Habitat]):
    species = get_species_in_area(habitats)
    print(species)
    competition = 0
    for i in range(height):
        for j in range(width):
            if species[i][j] == k:
                competition += 1
    return competition


n, k = map(int, input().split())
habitats = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    habitats.append(Habitat(x1, y1, x2, y2))
print(soluiton(n, k, habitats))
