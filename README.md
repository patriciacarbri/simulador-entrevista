# Simulador de Entrevista — TTS

Converte um roteiro de entrevista em áudio MP3 com duas vozes distintas: uma para o jornalista e outra para a especialista. As pausas entre falas e dentro das respostas mais longas são geradas automaticamente.

---

## Estrutura do projeto

```
tts_entrevista/
│
├── app.py                  # ponto de entrada — orquestra o fluxo
├── requirements.txt
├── README.md
│
├── roteiro/
│   ├── __init__.py
│   └── falas.py            # texto da entrevista (dados puros)
│
└── tts/
    ├── __init__.py
    ├── config.py           # vozes, cadência, arquivo de saída
    ├── synthesis.py        # sintetiza texto → bytes MP3
    └── audio.py            # concatena chunks → salva arquivo
```

---

## Pré-requisitos

- Python 3.10+
- Conexão com internet (o `edge-tts` faz streaming pelo Microsoft Edge)

---

## Instalação

```bash
# cria e ativa o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows

# instala as dependências
pip install -r requirements.txt
```

---

## Como usar

```bash
python app.py
```

O arquivo `entrevista_radio.mp3` será gerado na raiz do projeto.

---

## Configuração de vozes e cadência

Todas as configurações ficam em `tts/config.py`:

```python
VOICE_JOURNALIST = "pt-BR-AntonioNeural"    # masculina
VOICE_SPECIALIST = "pt-BR-FranciscaNeural"  # feminina
SPEAKING_RATE    = "-5%"    # velocidade relativa ao padrão
PITCH            = "-2Hz"   # tom da voz
PAUSE_BETWEEN_SPEAKERS = "600ms"   # pausa na virada de locutor
```

Para ver todas as vozes disponíveis em pt-BR:

```bash
edge-tts --list-voices | grep pt-BR
```

---

## Como editar o roteiro

Edite `roteiro/falas.py`. Cada fala é uma tupla `(locutor, texto)`:

```python
("jornalista", "Sua pergunta aqui."),
("especialista", "Resposta aqui. <break time='400ms'/> Continuação após pausa."),
```

As tags `<break time='Xms'/>` inserem silêncio real no ponto indicado — útil para simular respiração em respostas longas.

---

## Vozes disponíveis

| Voz | Gênero | Perfil |
|-----|--------|--------|
| `pt-BR-AntonioNeural` | Masculina | Formal, jornalístico |
| `pt-BR-FranciscaNeural` | Feminina | Clara, profissional |
| `pt-BR-ThalitaNeural` | Feminina | Mais jovem, dinâmica |

---

## Nota sobre qualidade de áudio

A implementação atual usa **Edge TTS** (Microsoft), que é gratuita, roda sem cadastro e não exige configuração de conta em nuvem.

Para resultados mais naturais — entonação mais expressiva, pausas mais orgânicas e qualidade próxima de locução profissional — a alternativa recomendada é a **Google Cloud Text-to-Speech** com vozes `Neural2` em pt-BR:

- Jornalista: `pt-BR-Neural2-B` (masculina)
- Especialista: `pt-BR-Neural2-A` (feminina)

A migração exige apenas substituir `tts/synthesis.py` e `tts/config.py` pela versão Google, além de configurar autenticação via `gcloud` e habilitar a API no GCP. O restante do projeto — roteiro, estrutura de módulos e `app.py` — permanece intacto.

Documentação da API Google TTS: https://cloud.google.com/text-to-speech/docs

---

## Dependências

| Pacote | Uso |
|--------|-----|
| `edge-tts` | Síntese de voz via Microsoft Edge Neural |