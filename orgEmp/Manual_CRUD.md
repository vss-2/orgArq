# Python e SQLite3
## Criando banco e tabelas
```conector = sqlite3.connect('empresa.db')```<br>
```cursor   = conector.cursor()```<br><br>
```cursor.execute("""CREATE TABLE empregados (```<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ```      nome       text,```<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ```		salario    real,```<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ```		admissao   text,```<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ```		demissao   text```<br>
```		)""")```

## Jeito errado de implementar inserção usando .format, suscetível a SQL Injection (quebrar o banco)
```cursor.execute("INSERT INTO empresa VALUES ('{}', {}, '{}', '{}')".format('Joao Silva', 1030.0, '23/10/2019', ''))```

# 2 Alternativas evitando SQL Injection:
## Usando Tuplas:
```cursor.execute("INSERT INTO empresa VALUES (?, ?, ?, ?)", ('Joao Silva', 1030.0, '23/10/2019', ''))```
## Usando Dicionários:
```cursor.execute("INSERT INTO empresa VALUES (:nome, :salario, :admissao, :demissao)", {'nome': 'Joao Silva', 'salario': 1030.0, 'admissao': '23/10/2019', 'demissao': ''})```