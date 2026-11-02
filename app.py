
# CodeForge AI Coder
# Assistente de programação com inteligência artificial

# Imports
import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Carrega as variáveis do arquivo .env, quando disponível
load_dotenv()

# Configuração da página (deve ser chamada uma única vez)
st.set_page_config(
    page_title="CodeForge AI Coder",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Prompt de sistema
CUSTOM_PROMPT = """
Você é o "CodeForge AI Coder", um assistente de IA especialista
em programação, com foco principal em Python.

Sua missão é ajudar desenvolvedores iniciantes com dúvidas
de programação de forma clara, precisa e útil.

REGRAS DE OPERAÇÃO:

1. FOCO EM PROGRAMAÇÃO:
Responda apenas a perguntas relacionadas a programação,
algoritmos, estruturas de dados, bibliotecas e frameworks.
Se o usuário perguntar sobre outro assunto, informe educadamente
que seu foco é auxiliar com programação.

2. ESTRUTURA DA RESPOSTA:
Sempre que possível, organize suas respostas da seguinte forma:

- Explicação Clara: apresente o conceito de maneira didática.
- Exemplo de Código: forneça exemplos em Python com sintaxe correta.
- Detalhes do Código: explique a lógica e as funções utilizadas.
- Documentação de Referência: indique documentação oficial
  relevante da linguagem ou biblioteca utilizada.

3. CLAREZA E PRECISÃO:
Utilize linguagem clara e tecnicamente correta.
Evite jargões desnecessários.
Seja didático e considere que o usuário pode ser iniciante.
"""

# Recupera uma chave configurada pelo desenvolvedor
def get_default_api_key():
    api_key = os.getenv("GROQ_API_KEY")

    if api_key:
        return api_key

    try:
        return st.secrets.get("GROQ_API_KEY", None)
    except Exception:
        return None


# Inicializa o histórico da conversa
if "messages" not in st.session_state:
    st.session_state.messages = []


# BARRA LATERAL
with st.sidebar:

    st.title("🤖 CodeForge AI Coder")

    st.image("painel.png")

    st.write(
        "Um assistente de inteligência artificial "
        "focado em programação, especialmente Python."
    )

    st.markdown("---")

    # Campo para inserir a chave de API
    st.subheader("Configuração da API")

    user_api_key = st.text_input(
        "Sua chave de API da Groq",
        type="password",
        placeholder="gsk_...",
        help="Sua chave será utilizada durante esta sessão."
    )

    # Define qual chave será utilizada
    if user_api_key.strip():
        api_key = user_api_key.strip()
        st.success("Utilizando sua chave de API.")
    else:
        api_key = get_default_api_key()

        if api_key:
            st.info("Utilizando a chave configurada pelo desenvolvedor.")
        else:
            st.warning("Insira uma chave de API para começar.")

    st.markdown("---")

    st.markdown(
        """
        **Sobre o projeto**

        O CodeForge AI Coder foi desenvolvido para auxiliar
        estudantes e iniciantes no aprendizado de programação.

        A inteligência artificial pode cometer erros.
        Sempre verifique as respostas e os códigos gerados.
        """
    )

    st.markdown("---")

    st.markdown(
        "Conheça os cursos, formações e programas de "
        "pós-graduação da DSA."
    )


# INTERFACE PRINCIPAL

st.title("CodeForge AI Coder")

st.subheader("Seu assistente de programação")

st.caption(
    "Faça perguntas sobre Python e obtenha explicações, "
    "exemplos de código e referências."
)


# EXIBIÇÃO DO HISTÓRICO

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ENTRADA DO USUÁRIO

if prompt := st.chat_input("Qual é a sua dúvida sobre Python?"):

    # Verifica se existe uma chave de API
    if not api_key:
        st.warning(
            "Para utilizar o CodeForge AI Coder, "
            "insira uma chave de API da Groq na barra lateral."
        )
        st.stop()

    # Armazena e exibe a mensagem do usuário
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepara o histórico para enviar à API
    messages_for_api = [
        {"role": "system", "content": CUSTOM_PROMPT}
    ]

    messages_for_api.extend(st.session_state.messages)

    # Gera a resposta da inteligência artificial
    with st.chat_message("assistant"):

        with st.spinner("Analisando sua pergunta..."):

            try:
                # Inicializa o cliente da Groq
                client = Groq(api_key=api_key)

                # Solicita uma resposta à API
                chat_completion = client.chat.completions.create(
                    messages=messages_for_api,
                    model="openai/gpt-oss-20b",
                    temperature=0.7,
                    max_tokens=2048
                )

                # Extrai a resposta gerada
                ai_response = (
                    chat_completion.choices[0].message.content
                )

                # Exibe a resposta
                st.markdown(ai_response)

                # Armazena a resposta no histórico
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": ai_response
                    }
                )

            except Exception:
                st.error(
                    "Não foi possível gerar uma resposta. "
                    "Verifique sua chave de API, sua conexão "
                    "e tente novamente."
                )


# RODAPÉ

st.markdown(
    """
    <div style="text-align: center; color: gray;">
        <hr>
        <p>CodeForge AI Coder | Desenvolvido por GalvaoLabs</p>
    </div>
    """,
    unsafe_allow_html=True
)