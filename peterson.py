def main():
    # write model
    # make correspondance between vertices and variables
    vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    variables = []
    for vertice in vertices:
        variables.append(vertice*3+1)
        variables.append(vertice * 3 + 2)
        variables.append(vertice * 3 + 3)
    edges = [
        (1,0),
        (1,5),
        (1,2),
        (0,4),
        (0,7),
        (5,6),
        (5,8),
        (4,3),
        (3,2),
        (8,9),
        (9,2),
        (7,9),
        (7,6),
        (7,6),
        (4,6),
        (6,3),
        (3,8),
        (8,4)
    ]
    clauses = []
    for edge in edges:
        clauses = mergeClauses(clauses, findClausesAdjacent(edge[0],edge[1],variables))
    print(clauses)
    writeCNF(clauses, variables) #120 solutions (Feasible Solutions : 96 (37 non-trivial feasible subtrees)

def findClausesAdjacent(vertice_i,vertice_j, variables):
    clauses = []
    variables_i = variables[vertice_i*3:vertice_i*3+3]
    variables_j = variables[vertice_j*3:vertice_j*3+3]
    # x1 ou x2 ou x3
    clauses.append(str(variables_i[0]) + ' ' + str(variables_i[1]) + ' ' + str(variables_i[2]))
    # one vertice = one color
    clauses.append('-'+str(variables_i[0]) + ' ' + '-'+str(variables_i[1]))
    clauses.append('-'+str(variables_i[1]) + ' ' + '-'+str(variables_i[2]))
    clauses.append('-'+str(variables_i[0]) + ' ' + '-'+str(variables_i[2]))
    # adjacent vertice of different colors
    clauses.append('-'+str(variables_i[0]) + ' ' + '-'+str(variables_j[0]))
    clauses.append('-'+str(variables_i[1]) + ' ' + '-'+str(variables_j[1]))
    clauses.append('-'+str(variables_i[2]) + ' ' + '-'+str(variables_j[2]))
    return clauses

def mergeClauses(clauses1, clauses2):
    return set(list(clauses1)+list(clauses2))

def writeCNF(clauses, variables):
    file = open("peterson.cnf", "w")

    file.write("c peterson.cnf\n")
    file.write("c\n")
    file.write("p cnf "+str(len(variables))+" "+str(len(clauses))+"\n")
    for clause in clauses:
        file.write(clause + " 0\n")
    file.close()

main()