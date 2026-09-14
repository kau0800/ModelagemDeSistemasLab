# Setup do Gemini API no PyCharm

## Fase 1: Gerar API Key do Gemini

1. Acesse https://aistudio.google.com/app/apikey
2. Clique em **"Create API Key"** (vai gerar grátis, tem crédito free)
3. Copie a chave gerada

## Fase 2: Configurar no PyCharm

### Opção A: Variável de Ambiente (Recomendado)

**No Terminal (macOS/Linux):**
```bash
export GEMINI_API_KEY="sua_chave_aqui"
```

**No Terminal (Windows PowerShell):**
```powershell
$env:GEMINI_API_KEY="sua_chave_aqui"
```

**Depois abra o PyCharm:**
```bash
pycharm .
```

### Opção B: Arquivo .env (Mais fácil)

1. Cria um arquivo `.env` na raiz do projeto:
```
GEMINI_API_KEY=sua_chave_aqui
```

2. Instala a biblioteca:
```bash
pip install python-dotenv
```

3. Adiciona no `gemini_agent.py` antes de chamar a API:
```python
from dotenv import load_dotenv
load_dotenv()
```

## Fase 3: Instalar Dependências

```bash
pip install google-generativeai
```

## Fase 4: Rodar o Agente

No terminal do PyCharm:
```bash
python gemini_agent.py
```

Isso vai:
1. Ler `docs/specs/frete.md`, `docs/tasks.md` e `test_frete.py`
2. Chamar o Gemini 3 vezes (uma para cada arquivo)
3. Gerar `frete.py`, `app.py` e `templates/index.html`

## Fase 5: Testar Tudo

```bash
pytest test_frete.py -v
python app.py
```

Acessa `http://localhost:5000` no navegador.

---

## Troubleshooting

**Erro: "ModuleNotFoundError: No module named 'google'"**
```bash
pip install google-generativeai
```

**Erro: "GEMINI_API_KEY not found"**
- Verifica se a variável de ambiente foi setada
- Ou usa o arquivo `.env`

**Gemini demorando muito?**
- É normal, é uma API remota. Pode levar 5-10 segundos.

**Código gerado está com erros?**
- Ajusta o prompt em `gemini_agent.py`
- Roda novamente: `python gemini_agent.py`
