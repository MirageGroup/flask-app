# flask-app
Teste de aplicação web com Flask

Crie o ambiente virtual venv:

Linux:
```bash
python3 -m venv venv
```
Windows:
```bash
python -m venv venv
```

Inicie o ambiente virtual venv: 

Linux:
```bash
. venv/bin/activate
```
Windows:
```bash
venv\Scripts\activate
```

Instale as dependências de desenvolvimento:
```bash
pip install -r requirements.txt
```

Inicie o servidor de desenvolvimento:

Linux:
```bash
flask --app app/main --debug run
```

Windows:
```bash
python app/main.py
```
