import os 

FRAME_WIDTH = 128
FRAME_HEIGHT = 128
BITS_PER_FRAME = FRAME_WIDTH * FRAME_HEIGHT
BYTES_PER_FRAME = BITS_PER_FRAME // 8
CHUNK_SIZE = 32 * 1024  # 32KB

INPUT_FOLDER = "Frames_Uncropped_Raw"
OUTPUT_FILENAME = "BadApple_Compressed.bin"
LOG_FILENAME = "log.txt"

def rle_compress(bits):
    rle = []
    i = 0
    while i < len(bits):
        val = bits[i]
        run_len = 1
        while i + run_len < len(bits) and bits[i + run_len] == val and run_len < 127:
            run_len += 1
        rle_byte = (val << 7) | run_len
        rle.append(rle_byte)
        i += run_len
    return rle

def byte_to_bits(byte):
    return [(byte >> (7 - i)) & 1 for i in range(8)]

def bytes_to_bits(raw_bytes):
    bits = []
    for b in raw_bytes:
        bits.extend(byte_to_bits(b))
    return bits[:BITS_PER_FRAME]

def main():
    frame_files = sorted([f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(".raw")])
    total_original = 0
    total_compressed = 0
    chunk_index = 0
    chunk_offset = 0
    output_data = bytearray()

    log_file = open(LOG_FILENAME, "w")

    for i, filename in enumerate(frame_files):
        path = os.path.join(INPUT_FOLDER, filename)
        with open(path, "rb") as f:
            raw = f.read()
            if len(raw) != BYTES_PER_FRAME:
                log_file.write(f"Warning: {filename} is not {BYTES_PER_FRAME} bytes\n")
                continue

            bits = bytes_to_bits(raw)
            rle = rle_compress(bits)
            total_original += len(raw)
            total_compressed += len(rle) + 1
            frame_data = bytearray(rle)
            frame_data.append(0x00)

            # If the frame would exceed the current 32KB chunk, pad and start new chunk
            if chunk_offset + len(frame_data) > CHUNK_SIZE:
                pad_len = CHUNK_SIZE - chunk_offset
                output_data.extend([0x00] * pad_len)
                chunk_index += 1
                chunk_offset = 0
                log_file.write(f"--- Chunk {chunk_index} ---\n")

            end_offset = chunk_offset + len(frame_data) - 1
            mem_addr = f"0x{end_offset:04X}"
            log_file.write(f"{filename} ends at memory location {mem_addr} in chunk {chunk_index}\n")

            output_data.extend(frame_data)
            chunk_offset += len(frame_data)

    # Final padding to align to next chunk if necessary
    if chunk_offset < CHUNK_SIZE:
        output_data.extend([0x00] * (CHUNK_SIZE - chunk_offset))

    with open(OUTPUT_FILENAME, "wb") as f:
        f.write(output_data)

    compression_ratio = total_original / total_compressed if total_compressed else 0

    log_file.write(f"\nProcessed {len(frame_files)} frames\n")
    log_file.write(f"Original size: {total_original} bytes\n")
    log_file.write(f"RLE size: {total_compressed} bytes\n")
    log_file.write(f"Compression ratio: {compression_ratio:.2f}:1\n")

    log_file.close()

if __name__ == "__main__":
    main()