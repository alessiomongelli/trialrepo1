import git

# Imposta il percorso locale della repository
repo = git.Repo("https://github.com/OpenVirtualizedNetworks2023/python_basics_set1-alessiomongelli.git")

# Visualizza l'elenco dei file modificati
diff = repo.index.diff(None)
for item in diff:
    print(item)

# Aggiungi tutti i file modificati al commit
repo.index.add(diff)

# Esegui un commit
repo.index.commit("Messaggio del commit")

# Push delle modifiche sulla repository remota
origin = repo.remote(name='origin')
origin.push()

# ahahahahahaha