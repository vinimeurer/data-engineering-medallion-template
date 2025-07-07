# Data Engineering Medallion Architecture Template

Um template completo para implementação da arquitetura Medallion em projetos de engenharia de dados, seguindo as melhores práticas da indústria.

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Arquitetura Medallion](#arquitetura-medallion)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Como Usar](#como-usar)
- [Camadas de Dados](#camadas-de-dados)
- [Scripts de Processamento](#scripts-de-processamento)
- [Contribuição](#contribuição)
- [Licença](#licença)

## 🚀 Sobre o Projeto

Este template implementa a **Arquitetura Medallion** (Bronze, Silver, Gold) para projetos de engenharia de dados. A arquitetura Medallion é um padrão de design amplamente usado em lakehouse que organiza dados em três camadas distintas para melhorar a qualidade dos dados gradualmente à medida que eles fluem através de cada camada.

### Principais Características:

- 🏗️ **Estrutura padronizada** seguindo boas práticas de engenharia de dados
- 📊 **Arquitetura em camadas** (Bronze → Silver → Gold)
- 🔧 **Scripts modulares** para cada etapa do pipeline
- 📝 **Configuração centralizada** para facilitar manutenção
- 🔍 **Sistema de logs** integrado
- 🌱 **Ambiente de desenvolvimento** pré-configurado

## 🏛️ Arquitetura Medallion

### Bronze Layer (Camada de Bronze)
- **Propósito**: Armazenamento de dados brutos/raw
- **Características**: Dados sem transformação, formato original
- **Qualidade**: Dados "sujos", sem validação

### Silver Layer (Camada de Prata)
- **Propósito**: Dados limpos e validados
- **Características**: Transformações básicas, padronização de formatos
- **Qualidade**: Dados estruturados e confiáveis

### Gold Layer (Camada de Ouro)
- **Propósito**: Dados prontos para análise e relatórios
- **Características**: Agregações, métricas de negócio, dados modelados
- **Qualidade**: Dados otimizados para consumo

## 📁 Estrutura do Projeto

```
project_root/
├── config/                    # Configurações do projeto
│   └── settings.py            # Configurações centralizadas
├── data/                      # Armazenamento de dados
│   ├── raw/                   # Dados brutos/originais
│   ├── bronze/                # Camada Bronze - dados sem processamento
│   ├── silver/                # Camada Silver - dados limpos
│   └── gold/                  # Camada Gold - dados para análise
├── logs/                      # Arquivos de log
├── scripts/                   # Scripts de processamento
│   ├── extract/               # Scripts de extração de dados
│   ├── bronze/                # Scripts de processamento Bronze
│   ├── silver/                # Scripts de processamento Silver
│   └── gold/                  # Scripts de processamento Gold
├── requirements.txt           # Dependências Python
├── .env                       # Variáveis de ambiente
├── .gitignore                 # Arquivos ignorados pelo Git
├── README.md                  # Este arquivo
└── create_structure.py        # Script para criar estrutura do projeto
```

## 🛠️ Instalação

### Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- Git (opcional, para controle de versão)

### Passos de Instalação

1. **Clone ou baixe este template:**
   ```bash
   git clone <url-do-repositorio>
   cd data-engineering-medallion-template
   ```

2. **Execute o script de criação da estrutura:**
   ```bash
   python create_structure.py
   ```

3. **Crie um ambiente virtual (recomendado):**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuração

### 1. Variáveis de Ambiente

Edite o arquivo `.env` e configure as variáveis necessárias:

```env
# Configurações do banco de dados
DB_HOST=localhost
DB_PORT=5432
DB_NAME=data_warehouse
DB_USER=seu_usuario
DB_PASSWORD=sua_senha

# Configurações de APIs
API_KEY=sua_api_key
API_URL=https://api.exemplo.com

# Configurações de processamento
BATCH_SIZE=1000
MAX_RETRIES=3
```

### 2. Configurações do Projeto

Edite `config/settings.py` para definir configurações específicas do seu projeto:

```python
# Exemplo de configurações
DATABASE_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

PROCESSING_CONFIG = {
    'batch_size': int(os.getenv('BATCH_SIZE', 1000)),
    'max_retries': int(os.getenv('MAX_RETRIES', 3))
}
```

## 🚀 Como Usar

### 1. Desenvolvimento do Pipeline

1. **Extração de Dados**: Implemente scripts em `scripts/extract/`
2. **Processamento Bronze**: Desenvolva transformações em `scripts/bronze/`
3. **Processamento Silver**: Crie limpeza de dados em `scripts/silver/`
4. **Processamento Gold**: Implemente agregações em `scripts/gold/`

### 2. Exemplo de Fluxo de Trabalho

```python
# 1. Extrair dados
python scripts/extract/extract_data.py

# 2. Processar para Bronze
python scripts/bronze/process_bronze.py

# 3. Limpar para Silver
python scripts/silver/process_silver.py

# 4. Agregar para Gold
python scripts/gold/process_gold.py
```

## 📊 Camadas de Dados

### Bronze Layer
- **Entrada**: Dados raw de diversas fontes
- **Processamento**: Mínimo ou nenhum
- **Formato**: Mantém formato original (JSON, CSV, XML, etc.)
- **Uso**: Backup histórico, auditoria

### Silver Layer
- **Entrada**: Dados da camada Bronze
- **Processamento**: Limpeza, validação, padronização
- **Formato**: Formato estruturado (Parquet, Delta)
- **Uso**: Análises exploratórias, desenvolvimento

### Gold Layer
- **Entrada**: Dados da camada Silver
- **Processamento**: Agregações, métricas de negócio
- **Formato**: Otimizado para consultas
- **Uso**: Relatórios, dashboards, ML

## 📜 Scripts de Processamento

### Estrutura Recomendada para Scripts

```python
# Exemplo de estrutura para scripts
import logging
from config.settings import CONFIG

def setup_logging():
    """Configura sistema de logs"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/process.log'),
            logging.StreamHandler()
        ]
    )

def extract_data():
    """Função de extração de dados"""
    pass

def transform_data(data):
    """Função de transformação de dados"""
    pass

def load_data(data, destination):
    """Função de carregamento de dados"""
    pass

def main():
    """Função principal"""
    setup_logging()
    logging.info("Iniciando processamento...")
    
    # Implementar lógica do pipeline
    
    logging.info("Processamento concluído!")

if __name__ == "__main__":
    main()
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📋 Próximos Passos

Após configurar o template, considere implementar:

- [ ] Scripts de extração de dados específicos da sua fonte
- [ ] Validações de qualidade de dados
- [ ] Testes unitários para os pipelines
- [ ] Orquestração com Apache Airflow ou similar
- [ ] Monitoramento e alertas
- [ ] Documentação de dados (data catalog)
- [ ] CI/CD pipeline

## 📞 Suporte

Se você encontrar problemas ou tiver dúvidas:

1. Verifique a [documentação](#)
2. Procure por [issues existentes](#)
3. Abra uma nova [issue](#) se necessário

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE). Veja o arquivo `LICENSE` para mais detalhes.

---

⭐ **Dica**: Este template é um ponto de partida. Adapte-o às necessidades específicas do seu projeto e organização!