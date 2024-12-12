from collections import Counter, heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Untuk prioritas dalam heapq
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    # Buat heap dengan node untuk setiap karakter
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Gabungkan dua node dengan frekuensi terendah
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def build_codes(node, prefix="", codes={}):
    if node:
        if node.char is not None:
            codes[node.char] = prefix
        build_codes(node.left, prefix + "0", codes)
        build_codes(node.right, prefix + "1", codes)
    return codes

def huffman_encode(data):
    # Hitung frekuensi karakter
    frequencies = Counter(data)

    # Bangun pohon Huffman
    root = build_huffman_tree(frequencies)

    # Buat tabel kode Huffman
    codes = build_codes(root)

    # Encode data
    encoded_data = "".join(codes[char] for char in data)
    return codes, encoded_data

# Data input
data = "EEFFFGGGHH"

# Encode menggunakan Huffman
codes, encoded_data = huffman_encode(data)

# Output hasil
print("Kode Huffman:", codes)
print("Data terkompresi:", encoded_data)
