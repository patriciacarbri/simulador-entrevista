"""
tts/synthesis.py
----------------
Responsabilidade única: receber texto + voz → devolver bytes MP3.
Usa edge-tts: gratuito, local, sem autenticação.

edge-tts NÃO processa SSML — lê as tags como texto literal.
Solução: separar o texto nas marcações <break>, sintetizar cada
trecho individualmente e intercalar silêncio MP3 entre eles.
"""

import asyncio
import io
import re
import struct
import edge_tts
from tts.config import SPEAKING_RATE, PITCH, PAUSE_BETWEEN_SPEAKERS


# Regex que captura tanto <break time='400ms'/> quanto <break time="600ms"/>
_BREAK_RE = re.compile(r"<break\s+time=['\"](\d+)ms['\"]\s*/>")


def _ms_to_mp3_silence(ms: int) -> bytes:
    """
    Gera bytes de silêncio MP3 para a duração informada em milissegundos.

    Usa frames MP3 de 26ms (128kbps, 44100Hz) preenchidos com zeros.
    Concatenar com outros MP3 é válido — MP3 é um formato de stream.
    """
    frame_duration_ms = 26
    num_frames = max(1, ms // frame_duration_ms)

    # Cabeçalho de frame MP3: 128kbps, 44100Hz, stereo, sem padding
    # Bytes: FF FB 90 00  (sync + MPEG1 Layer3 + 128kbps + 44100Hz + stereo)
    header = bytes([0xFF, 0xFB, 0x90, 0x00])
    frame_size = 417   # tamanho de frame a 128kbps/44100Hz
    frame = header + bytes(frame_size - len(header))

    return frame * num_frames


def _split_on_breaks(text: str) -> list[tuple[str, int]]:
    """
    Divide o texto nas tags <break> e retorna lista de (trecho, pausa_ms).

    Cada tupla representa:
      - trecho: texto a ser sintetizado
      - pausa_ms: silêncio em ms a inserir DEPOIS deste trecho (0 = nenhum)

    Exemplo:
      "Olá. <break time='400ms'/> Tudo bem?"
      → [("Olá.", 400), ("Tudo bem?", 0)]
    """
    partes = _BREAK_RE.split(text)
    # split com grupo de captura alterna: [texto, ms, texto, ms, ..., texto]
    resultado = []
    for i in range(0, len(partes), 2):
        trecho = partes[i].strip()
        pausa  = int(partes[i + 1]) if i + 1 < len(partes) else 0
        if trecho:
            resultado.append((trecho, pausa))
    return resultado


async def _synthesize_trecho(text: str, voice_name: str) -> bytes:
    """Sintetiza um trecho de texto puro (sem tags) e retorna bytes MP3."""
    communicate = edge_tts.Communicate(text, voice_name, rate=SPEAKING_RATE, pitch=PITCH)
    buffer = io.BytesIO()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            buffer.write(chunk["data"])
    return buffer.getvalue()


async def synthesize(text: str, voice_name: str, add_pause_before: bool = False) -> bytes:
    """
    Sintetiza uma fala completa, respeitando as pausas <break> internas.

    Args:
        text:             Texto da fala, pode conter <break time='Xms'/>.
        voice_name:       Voz Edge TTS (ex: pt-BR-AntonioNeural).
        add_pause_before: Se True, insere pausa de transição antes do áudio.

    Returns:
        Bytes MP3 com áudio e silêncios intercalados.
    """
    trechos = _split_on_breaks(text)
    buffer  = io.BytesIO()

    if add_pause_before:
        ms = int(PAUSE_BETWEEN_SPEAKERS.replace("ms", ""))
        buffer.write(_ms_to_mp3_silence(ms))

    for trecho, pausa_ms in trechos:
        audio = await _synthesize_trecho(trecho, voice_name)
        buffer.write(audio)
        if pausa_ms:
            buffer.write(_ms_to_mp3_silence(pausa_ms))

    return buffer.getvalue()