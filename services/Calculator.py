# -> list "Anotación de tipo retorno (retorna una lista en tuplas)"

def projectSalary(initialSalary:float, years:int, percentIncrease:float)-> list:
    projection = []
    currentSalary = initialSalary
    
    for year in range(1, years + 1):
        currentSalary *= (1 + percentIncrease / 100)
        projection.append((year, round(currentSalary, 2)))
    return projection