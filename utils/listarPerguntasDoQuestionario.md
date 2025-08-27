# Plano: listarPerguntasDoQuestionario.py

## Objetivo
Criar um script que analisa questionários em PDF e extrai automaticamente todas as perguntas, gerando uma lista estruturada em JSON.

## Funcionalidades Principais

### 1. Análise Direta do PDF com Claude API
- **Claude lê diretamente o PDF**: Processar arquivo PDF página por página
- **Primeira passada**: Analisar cada página do questionário via Claude API
- **Prompt para Claude**: "Identifique todas as perguntas nesta página do questionário. Para cada pergunta encontrada, extraia: nome/identificador da pergunta e um resumo do enunciado em até 120 caracteres"
- Configurar API key do Claude (Anthropic)

### 2. Estrutura de Dados
```json
{
  "questionario": "nome_do_arquivo",
  "perguntas": [
    {
      "Nome": "Q1_Idade",
      "Ordem": 1,
      "Enunciado120Char": "Qual é a sua idade? Marque a faixa etária correspondente nas opções abaixo."
    },
    {
      "Nome": "Q2_Escolaridade", 
      "Ordem": 2,
      "Enunciado120Char": "Indique seu nível de escolaridade completo ou em andamento."
    }
  ]
}
```

## Implementação Técnica

### Dependências Necessárias
```python
import anthropic  # Claude API client - PRINCIPAL
import json
import os
from pathlib import Path
```

### Fluxo de Execução

1. **Input**: Caminho para PDF do questionário
2. **Análise Direta**: Claude API lê PDF página por página → Identificação de perguntas
3. **Compilação**: Lista consolidada de perguntas identificadas pelo Claude
4. **Output**: `dados/[nome_questionario].json`

### Estrutura do Script
```python
class ListarPerguntasQuestionario:
    def __init__(self, api_key_claude):
        # Inicializar cliente Claude
        
    def analisar_pdf_com_claude(self, pdf_path):
        # Claude lê PDF diretamente página por página
        
    def compilar_perguntas(self, analises_paginas):
        # Consolidar perguntas de todas as páginas
        
    def exportar_json(self, perguntas, nome_questionario):
        # Salvar em dados/[nome].json
        
    def processar_questionario(self, pdf_path):
        # Orquestrar todo o processo
```

## Configurações

### API Claude
- Configurar chave da API Anthropic
- Definir modelo (claude-3-sonnet ou claude-3-haiku)
- Configurar limites de tokens e rate limiting

### Prompts Otimizados
- **Prompt principal** (análise por página): Focado em identificação precisa de perguntas

## Saída Esperada
- Arquivo JSON em `dados/[nome_questionario].json`
- Log detalhado do processamento

## Considerações Especiais
- Tratar questionários com múltiplas colunas
- Lidar com perguntas condicionais (skip logic)
- Identificar sub-perguntas e escalas
- Manter ordem original das perguntas no PDF

## Uso
```bash
python utils/listarPerguntasDoQuestionario.py dados/questionarios/qt2.pdf
```

Resultado: `dados/qt2.json` com lista estruturada de perguntas