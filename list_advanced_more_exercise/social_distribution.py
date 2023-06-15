population = [int(num) for num in input().split(', ')]
wealth_level = int(input())
distribution_possible = True

while True:
    min_element = min(population)
    max_element = max(population)
    min_element_index = population.index(min_element)
    max_element_index = population.index(max_element)
    if min_element == wealth_level:
        break
    if max_element <= wealth_level and min_element <= wealth_level:
        print('No equal distribution possible')
        distribution_possible = False
        break
    diff = wealth_level - min_element
    population[min_element_index] += diff
    population[max_element_index] -= diff
if distribution_possible:
    print(population)
