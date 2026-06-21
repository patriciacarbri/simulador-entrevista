"""
tts/config.py
-------------
Todas as constantes do projeto em um lugar só.
Para trocar voz ou formato de saída: muda aqui, em nenhum outro lugar.

Vozes disponíveis em pt-BR no Edge TTS:
    pt-BR-AntonioNeural   masculina
    pt-BR-FranciscaNeural feminina
    pt-BR-ThalitaNeural   feminina (mais jovem)

Lista completa: edge-tts --list-voices | grep pt-BR
"""

VOICE_JOURNALIST = "pt-BR-AntonioNeural"    # masculina
VOICE_SPECIALIST = "pt-BR-FranciscaNeural"  # feminina
OUTPUT_FILE      = "entrevista_radio.mp3"

SPEAKING_RATE    = "-5%"    # edge-tts usa string com % relativo ao padrão
PITCH            = "-2Hz"   # leve redução para tom mais sério

PAUSE_BETWEEN_SPEAKERS = "600ms"   # pausa na virada de locutor