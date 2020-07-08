# Python e SQLite3
## Criando banco e tabelas

```
conector = sqlite3.connect('empresa.db')
cursor   = conector.cursor()

cursor.execute("""CREATE TABLE empregados (
        nome       text,
        salario    real,
        admissao   text,
	demissao   text
)""") 
```

### Jeito errado de implementar inserção usando .format, suscetível a SQL Injection (quebrar o banco)
```cursor.execute("INSERT INTO empresa VALUES ('{}', {}, '{}', '{}')".format('Joao Silva', 1030.0, '23/10/2019', ''))```

# 2 Alternativas evitando SQL Injection:
### Usando Tuplas:
```cursor.execute("INSERT INTO empresa VALUES (?, ?, ?, ?)", ('Joao Silva', 1030.0, '23/10/2019', ''))```
### Usando Dicionários:
```cursor.execute("INSERT INTO empresa VALUES (:nome, :salario, :admissao, :demissao)", {'nome': 'Joao Silva', 'salario': 1030.0, 'admissao': '23/10/2019', 'demissao': ''})```