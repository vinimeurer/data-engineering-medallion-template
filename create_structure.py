"""
create_structure.py

Cria a estrutura de projeto:

project_root/
├── config/
│   └── settings.py
├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── logs/
├── scripts/
│   ├── extract/
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── requirements.txt
├── .env
├── .gitignore
└── README.md
"""

import os
from pathlib import Path

# Defina aqui a raiz do projeto (pode ser . ou outro caminho)
ROOT = Path(__file__).parent.resolve()

# Diretórios a criar, relativos a ROOT
DIRS = [
    'config',
    'data/raw',
    'data/bronze',
    'data/silver',
    'data/gold',
    'logs',
    'scripts/extract',
    'scripts/bronze',
    'scripts/silver',
    'scripts/gold',
]

# Arquivos a criar (vazios ou com conteúdo), relativos a ROOT
FILES = [
    'requirements.txt',
    '.env',
    'README.md',
    'config/settings.py',
    '.gitignore',
]

# Conteúdo inicial para .gitignore
GITIGNORE_CONTENT = '''\
# Byte-compiled / optimized / DLL files
__pycache__/
config/__pycache__/
scripts/__pycache__/
scripts/extract/__pycache__/
scripts/bronze/__pycache__/
scripts/silver/__pycache__/
scripts/gold/__pycache__/

*.py[cod]
*$py.class

# Env / Virtualenv
.env
venv/
.env/
env/
.venv/

# Data folders
data/
data/raw/
data/bronze/
data/silver/
data/gold/

# Logs
logs/

# IDEs
.vscode/
.idea/
'''

def main():
    # Cria diretórios
    for d in DIRS:
        path = ROOT / d
        path.mkdir(parents=True, exist_ok=True)
        print(f"Dir criado: {path}")

    # Cria arquivos
    for f in FILES:
        path = ROOT / f
        if path.exists():
            print(f"Arquivo já existe: {path}")
            continue

        # Se for o .gitignore, escreve o conteúdo padrão
        if f == '.gitignore':
            with open(path, 'w', encoding='utf-8') as fp:
                fp.write(GITIGNORE_CONTENT)
            print(f".gitignore criado com conteúdo padrão: {path}")
        else:
            # apenas cria arquivo vazio (.env, README.md, requirements.txt, settings.py)
            path.touch()
            print(f"Arquivo criado: {path}")

if __name__ == '__main__':
    main()