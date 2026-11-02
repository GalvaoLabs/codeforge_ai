# CodeForge AI Coder

**Assistente de programação com inteligência artificial, desenvolvido em Python.**

O CodeForge AI Coder é uma aplicação que utiliza inteligência artificial generativa para auxiliar estudantes e desenvolvedores iniciantes no aprendizado de programação, com foco principal na linguagem Python.

Por meio de uma interface interativa desenvolvida com Streamlit, o usuário pode enviar perguntas, receber explicações, consultar exemplos de código e acessar referências para aprofundar seus conhecimentos.

## Funcionalidades

- **Assistente de programação:** respostas voltadas a conceitos, algoritmos, bibliotecas e ferramentas de desenvolvimento.
- **Geração de código:** exemplos em Python acompanhados de explicações.
- **Interface interativa:** chat desenvolvido com Streamlit.
- **Histórico de conversas:** manutenção das mensagens durante a sessão.
- **Integração com IA:** utilização do modelo `openai/gpt-oss-20b` por meio da API da Groq.
- **API Key personalizada:** possibilidade de inserir uma chave própria temporariamente pela barra lateral.
- **Configuração alternativa:** suporte a variáveis de ambiente e Secrets do Streamlit.

## Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal |
| Streamlit | Interface web e gerenciamento da sessão |
| Groq SDK | Comunicação com a API de inteligência artificial |
| python-dotenv | Carregamento de variáveis de ambiente |
| GPT-OSS 20B | Modelo de linguagem utilizado |

## Como executar o projeto

### 1. Pré-requisitos

- Python 3.10 ou superior.
- Uma chave de API da Groq, disponível em [Groq Console](https://console.groq.com/).

### 2. Clone o repositório

```bash
git clone https://github.com/GalvaoLabs/codeforge_ai.git
```

Entre na pasta do projeto:

```bash
cd codeforge_ai
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual:

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
streamlit run app.py
```

A aplicação será aberta no navegador.

## Configuração da API Key

O CodeForge AI Coder oferece duas maneiras de configurar a chave de acesso à API da Groq.

### Opção 1 — Chave própria do usuário

Ao abrir a aplicação, insira sua chave de API no campo correspondente da barra lateral.

A chave será utilizada durante a sessão e terá prioridade sobre a configuração padrão do desenvolvedor.

### Opção 2 — Variável de ambiente

Também é possível configurar uma chave padrão por meio de um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_aqui
```

O arquivo `.env` não deve ser enviado ao GitHub. Utilize o `.env.example` como referência para a configuração.

**Importante:** em ambientes como o Streamlit Community Cloud, utilize a funcionalidade Secrets para configurar variáveis de ambiente. Não compartilhe sua chave de API.

## Estrutura do projeto

```text
codeforge_ai/
│
├── app.py
├── .env.example
├── .gitignore
├── requirements.txt
├── logo.png
└── painel.png
```

## Conceitos aplicados

Durante o desenvolvimento, foram utilizados conceitos importantes de programação e desenvolvimento de aplicações:

- Integração com APIs externas.
- Manipulação de variáveis de ambiente.
- Gerenciamento de estado com `st.session_state`.
- Estruturação de mensagens para modelos de linguagem.
- Tratamento de exceções.
- Desenvolvimento de interfaces com Streamlit.

## Limitações

- O funcionamento depende da disponibilidade da API da Groq.
- O uso está sujeito aos limites e às condições da conta e da API.
- O histórico das conversas é mantido apenas durante a sessão.
- As respostas geradas por inteligência artificial podem apresentar erros e devem ser verificadas.

## Objetivo educacional

O projeto busca explorar a integração entre Python e inteligência artificial generativa, aplicando conceitos de desenvolvimento de aplicações, consumo de APIs e construção de interfaces interativas.

---

**Desenvolvido por [Miguel Henrique](https://github.com/GalvaoLabs) e [Mateus Sousa](https://github.com/msousa07).**