import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def ler_arquivo(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"Arquivo não encontrado: {caminho}"

def gerar_codigo_frete():
    spec = ler_arquivo("docs/specs/frete.md")
    tasks = ler_arquivo("docs/tasks.md")
    testes = ler_arquivo("test_frete.py")
    
    prompt = f"""Você é um desenvolvedor Full-Stack Python especializado em TDD.

SUA TAREFA: Gerar o código de `frete.py` que passa em TODOS os testes sem adicionar regras extras.

---
ESPECIFICAÇÃO (EARS):
{spec}

---
PLANO DE TAREFAS:
{tasks}

---
TESTES QUE DEVEM PASSAR (test_frete.py):
{testes}

---
RESTRIÇÕES (REGRA DE OURO):
1. Implemente APENAS o que os testes esperam
2. Não adicione lógica extra
3. Não adicione novos requisitos
4. O código deve passar em 100% dos testes

RETORNE APENAS O CÓDIGO Python puro de `frete.py`, sem explicações."""
    
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    
    return response.text

def gerar_app_flask():
    spec = ler_arquivo("docs/specs/frete.md")
    tasks = ler_arquivo("docs/tasks.md")
    
    prompt = f"""Você é um desenvolvedor Full-Stack Python especializado em Flask.

SUA TAREFA: Gerar o arquivo `app.py` que:
1. Importa a função `calcular_frete` de `frete.py`
2. Cria uma aplicação Flask
3. Expõe um endpoint POST `/calcular`
4. Retorna JSON com o resultado

---
ESPECIFICAÇÃO:
{spec}

---
PLANO DE TAREFAS:
{tasks}

---
REQUISITOS:
- O endpoint POST `/calcular` recebe JSON com `valor_carrinho` e `regiao`
- Retorna JSON com `frete` e `status`
- Endpoint GET `/` serve a página principal

RETORNE APENAS O CÓDIGO Python puro de `app.py`, sem explicações."""
    
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    
    return response.text

def gerar_html():
    spec = ler_arquivo("docs/specs/frete.md")
    
    prompt = f"""Você é um desenvolvedor Frontend HTML5 + JavaScript.

SUA TAREFA: Gerar `templates/index.html` com:
1. Formulário HTML5 com inputs para `valor_carrinho` e `regiao`
2. Botão para enviar (POST) para `/calcular`
3. Exibir o resultado (frete e status) na tela

---
ESPECIFICAÇÃO:
{spec}

---
REQUISITOS:
- Usar fetch() para enviar os dados
- Lidar com sucesso e erro na resposta
- Design simples e funcional

RETORNE APENAS O CÓDIGO HTML5 + JavaScript puro, sem explicações."""
    
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    
    return response.text

if __name__ == "__main__":
    print("Gerando frete.py...")
    codigo_frete = gerar_codigo_frete()
    with open("frete.py", "w", encoding='utf-8') as f:
        f.write(codigo_frete)
    print("✓ frete.py gerado")
    
    print("\nGerando app.py...")
    codigo_app = gerar_app_flask()
    with open("app.py", "w", encoding='utf-8') as f:
        f.write(codigo_app)
    print("✓ app.py gerado")
    
    print("\nGerando templates/index.html...")
    codigo_html = gerar_html()
    with open("templates/index.html", "w", encoding='utf-8') as f:
        f.write(codigo_html)
    print("✓ templates/index.html gerado")
    
    print("\n✓ Todos os arquivos foram gerados com sucesso!")
