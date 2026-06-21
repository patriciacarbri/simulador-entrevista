"""
tts/audio.py
------------
Responsabilidade única: receber chunks de bytes MP3 → salvar arquivo final.
 
"""

from pathlib import Path


def concatenate_and_save(chunks: list[bytes], output_path: str) -> Path:
    """
    Concatena uma lista de bytes MP3 e salva em disco.

    MP3 é um formato de stream: concatenação direta de arquivos
    válidos produz um arquivo válido. Sem necessidade de pydub
    para o caso básico.

    Args:
        chunks:      Lista de bytes MP3, um por fala do roteiro.
        output_path: Caminho do arquivo de saída (str ou Path).

    Returns:
        Path do arquivo salvo.
    """
    destination = Path(output_path)
    destination.write_bytes(b"".join(chunks))
    return destination

