import pytholog as pl
parentesco = pl.KnowledgeBase("pai")


parentesco([
    "pai(joao, pedro).",
    "pai(pedro, lucas).",
    "mae(maria, pedro).",
    "mae(ana, lucas).",
    "avo(X, Y) :- pai(X, Z), pai(Z, Y).",
    "avo(X, Y) :- mae(X, Z), mae(Z, Y)."
])
print(parentesco.query(pl.Expr("pai(X, pedro).")))
print(parentesco)





