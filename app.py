"""
app.py
------
Ponto de entrada. Não contém lógica de negócio.
Lê o roteiro, chama síntese fala a fala, salva o resultado.

Uso:
    python app.py
"""

import asyncio

from roteiro.falas import ROTEIRO
from tts.config import VOICE_JOURNALIST, VOICE_SPECIALIST, OUTPUT_FILE
from tts.synthesis import synthesize
from tts.audio import concatenate_and_save


VOICE_MAP: dict[str, str] = {
    "jornalista":   VOICE_JOURNALIST,
    "especialista": VOICE_SPECIALIST,
}


async def run() -> None:
    print(f"Iniciando geração de áudio — {len(ROTEIRO)} falas\n")

    chunks: list[bytes] = []

    for idx, (locutor, texto) in enumerate(ROTEIRO, start=1):
        voice = VOICE_MAP[locutor]
        label = locutor.capitalize()

        print(f"[{idx:02d}/{len(ROTEIRO)}] {label}... ", end="", flush=True)

        audio = await synthesize(texto, voice, add_pause_before=(idx > 1))
        chunks.append(audio)

        print(f"OK ({len(audio):,} bytes)")

    saved = concatenate_and_save(chunks, OUTPUT_FILE)
    total = sum(len(c) for c in chunks)

    print(f"\nSalvo em: {saved}")
    print(f"Tamanho total: {total:,} bytes ({total / 1024:.1f} KB)")


if __name__ == "__main__":
    asyncio.run(run())