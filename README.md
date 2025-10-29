# PROJETO_ANTI_FRAUDE

# 🛡️ Anti-Furto - Detector de Cartões (DIO Challenge)

> Projeto simples para demonstração de integração com Azure Blob Storage e um serviço de análise de dados (ex.: detecção/validação de informações de cartão em imagens).  
> Implementado como uma aplicação web leve usando **Streamlit** para upload de imagens e retorno de validação.

---

## ✅ Visão Geral

O **Anti-Furto** permite que o usuário faça upload de uma imagem (formato PNG/JPG/JPEG) com um suposto cartão de crédito.  
O fluxo principal:

1. O usuário faz upload da imagem via interface Streamlit (`app.py`).
2. A imagem é enviada para **Azure Blob Storage** (função `upload_blob` em `services/blob_service.py`).
3. O serviço de análise (`services/credit_card_service.py`) analisa a imagem e tenta extrair/validar informações do cartão (titular, banco, validade).
4. A interface exibe a imagem e o resultado da validação (Válido / Inválido) com os dados extraídos.

> ⚠️ Este projeto é **para fins educacionais** e demonstra integração de componentes — **não deve ser usado** em produção para processar dados sensíveis sem cumprir requisitos legais, de privacidade e segurança.

---

## 📂 Estrutura do Repositório

PROJETO_ANTI_FRAUDE/
│
├── src/
│   ├── services/
│   │   └── blob_service.py
│   │   └── credit_card_service.py
│   │
│   ├── utils/
│   │   └── config.py
│   │
│   └── app.py
│
├── .env
├── requirements.txt
└── README.md


