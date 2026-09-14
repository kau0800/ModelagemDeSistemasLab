```python
def calcular_frete(valor_carrinho: float, regiao: str) -> float:
    if valor_carrinho <= 0:
        raise ValueError("Valor de carrinho inválido")

    limite = 300.0 if regiao.lower() == "norte" else 200.0

    if valor_carrinho >= limite:
        return 0.0
    return 20.0
```