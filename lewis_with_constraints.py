#!/usr/bin/env python3

import CentraleSupelec
import sys

# chaque attribut est une variable
varnames = [
    ["norvégien", "anglais",  "espagnol",  "ukrainien", "japonais"],
    ["bleue",     "rouge",    "verte",     "jaune",     "blanche"],
    ["lait",      "café",     "thé",       "vin",       "eau"],
    ["kools",     "cravens",  "old golds", "gitanes",   "chesterfields"],
    ["chien",     "escargot", "renard",    "cheval",    "zèbre"]
]

# les maisons sont numérotés de 1 à 5
DOM = set([1,2,3,4,5])
EQUAL = set((u,u) for u in DOM)
DIFF = set((u,v) for u in DOM for v in DOM if u != v)
SUCC = set((u, u+1) for u in [1,2,3,4])
PREC = set((u+1, u) for u in [1,2,3,4])
NEXT = SUCC | PREC

var = {}
i = 0
for categorie in varnames:
    for name in categorie:
        var[name] = i
        i += 1

# attention : chaque variable doit avoir son propre domaine
#             ne pas utiliser le même objet ensemble pour plusieurs variables
domains = [set(range(1, 6)) for _ in range(len(var))]


# norvégien = 1
domains[var["norvégien"]] = set([1])

# lait = 3
domains[var["lait"]] = set([3])

P = CentraleSupelec.CSP(domains)

# tout différent
for categorie in varnames:
    for a in categorie:
        for b in categorie:
            if a < b:
                P.addConstraint(var[a], var[b], DIFF)

# bleue = norvégien + 1
P.addConstraint(var["bleue"], var["norvégien"], PREC)

# anglais = rouge
P.addConstraint(var["anglais"], var["rouge"], EQUAL)

# verte = café
P.addConstraint(var["verte"], var["café"], EQUAL)

# jaune = kools
P.addConstraint(var["jaune"], var["kools"], EQUAL)

# blanche = verte + 1
P.addConstraint(var["blanche"], var["verte"], PREC)

# espagnol = chien
P.addConstraint(var["espagnol"], var["chien"], EQUAL)

# ukrainien = thé
P.addConstraint(var["ukrainien"], var["thé"], EQUAL)

# japonais = cravens
P.addConstraint(var["japonais"], var["cravens"], EQUAL)

# old golds = escargot
P.addConstraint(var["old golds"], var["escargot"], EQUAL)

# gitanes = vin
P.addConstraint(var["gitanes"], var["vin"], EQUAL)

# (chesterfields = renard + 1) ou (chesterfields = renard - 1)
P.addConstraint(var["chesterfields"], var["renard"], NEXT)

# (kools = cheval + 1) ou (kools = cheval - 1)
P.addConstraint(var["kools"], var["cheval"], NEXT)

# P.print_tree = True

for sol in P.solve():
    for maison in DOM:
        print(maison, end=":  ")
        for categorie in varnames:
            for name in categorie:
                if sol[var[name]] == maison:
                    print("%-15s" % name, end="")
        print()
