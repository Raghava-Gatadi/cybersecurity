import binascii
def mix_column(col):
    c_0 = col[0]
    all_xor = col[0] ^ col[1] ^ col[2] ^ col[3]
    col[0] ^= all_xor ^ multiply_2(col[0] ^ col[1])
    col[1] ^= all_xor ^ multiply_2(col[1] ^ col[2])
    col[2] ^= all_xor ^ multiply_2(col[2] ^ col[3])
    col[3] ^= all_xor ^ multiply_2(c_0 ^ col[3])
s_box_string = '63 7c 77 7b f2 6b 6f c5 30 01 67 2b fe d7 ab 76' \
               'ca 82 c9 7d fa 59 47 f0 ad d4 a2 af 9c a4 72 c0' \
               'b7 fd 93 26 36 3f f7 cc 34 a5 e5 f1 71 d8 31 15' \
               '04 c7 23 c3 18 96 05 9a 07 12 80 e2 eb 27 b2 75' \
               '09 83 2c 1a 1b 6e 5a a0 52 3b d6 b3 29 e3 2f 84' \
               '53 d1 00 ed 20 fc b1 5b 6a cb be 39 4a 4c 58 cf' \
               'd0 ef aa fb 43 4d 33 85 45 f9 02 7f 50 3c 9f a8' \
               '51 a3 40 8f 92 9d 38 f5 bc b6 da 21 10 ff f3 d2' \
               'cd 0c 13 ec 5f 97 44 17 c4 a7 7e 3d 64 5d 19 73' \
               '60 81 4f dc 22 2a 90 88 46 ee b8 14 de 5e 0b db' \
               'e0 32 3a 0a 49 06 24 5c c2 d3 ac 62 91 95 e4 79' \
               'e7 c8 37 6d 8d d5 4e a9 6c 56 f4 ea 65 7a ae 08' \
               'ba 78 25 2e 1c a6 b4 c6 e8 dd 74 1f 4b bd 8b 8a' \
               '70 3e b5 66 48 03 f6 0e 61 35 57 b9 86 c1 1d 9e' \
               'e1 f8 98 11 69 d9 8e 94 9b 1e 87 e9 ce 55 28 df' \
               '8c a1 89 0d bf e6 42 68 41 99 2d 0f b0 54 bb 16'.replace(" ", "")


s_box = bytearray.fromhex(s_box_string)

def sub_word(word):
    substituted_word = bytes(s_box[i] for i in word)
    return substituted_word

def round_constant(i):
    round_constant_lookup = bytearray.fromhex('01020408102040801b36')
    if i <= 0 or i > len(round_constant_lookup):
        return bytes([0, 0, 0, 0])
    
    if i == 1:
        return bytes([round_constant_lookup[0], 0, 0, 0])
    
    round_constant_value = bytes([round_constant_lookup[i-1], 0, 0, 0])
    return round_constant_value

def xor_bytes(a, b):
    return bytes([x ^ y for (x, y) in zip(a, b)])

def rot_word(word):
    return word[1:] + word[:1]

#state_cols->number of columns in state
#key_cols->number of columns in key
def key_expansion(key, state_cols: int = 4):
    print("Current Key used: ", key)
    key_cols = len(key) // 4
    key_length_bits = len(key) * 8

    if key_length_bits == 128:
        no_rounds = 10
    elif key_length_bits == 192:
        no_rounds = 12
    else:  # 256-bit keys
        no_rounds = 14

    w = state_from_bytes(key)
    # print(w)
    for i in range(key_cols, state_cols * (no_rounds + 1)):
        temp = w[i-1] #previous value of word
        if i % key_cols == 0:
            temp = xor_bytes(sub_word(rot_word(temp)), round_constant(i // key_cols))
        elif key_cols > 6 and i % key_cols == 4:
            temp = sub_word(temp)
        w.append(xor_bytes(w[i - key_cols], temp))

    return [w[i*4:(i+1)*4] for i in range(len(w) // 4)]

def add_round_key(state, key_schedule, round):
    round_key = key_schedule[round]
    for r in range(len(state)):
        state[r] = [state[r][c] ^ round_key[r][c] for c in range(len(state[0]))]

def sub_bytes(state):
    for r in range(len(state)):
        state[r] = [s_box[state[r][c]] for c in range(len(state[0]))]

def shift_rows(state):
    '''[00, 10, 20, 30]     [00, 10, 20, 30]
       [01, 11, 21, 31] --> [11, 21, 31, 01]
       [02, 12, 22, 32]     [22, 32, 02, 12]
       [03, 13, 23, 33]     [33, 03, 13, 23]'''
    state[0][1], state[1][1], state[2][1], state[3][1] = state[1][1], state[2][1], state[3][1], state[0][1]
    state[0][2], state[1][2], state[2][2], state[3][2] = state[2][2], state[3][2], state[0][2], state[1][2]
    state[0][3], state[1][3], state[2][3], state[3][3] = state[3][3], state[0][3], state[1][3], state[2][3]

def multiply_2(a):
    if a & 0x80:
        return ((a << 1) ^ 0x1b) & 0xff #0x1b is irreducible polynomial in GF(8)
    return a << 1

def multiply_3(num):
    result = num << 1  
    if (num & 0x80):  
        result ^= 0x1b  
    return result

def mix_Column(col):
    c_0, c_1, c_2, c_3 = col[0], col[1], col[2], col[3]      
    col[0] = multiply_2(c_0) ^ multiply_3(c_1) ^ c_2 ^ c_3   # [0x02 0x03 0x01 0x01] [c_0]   [c_0']
    col[1] = c_0 ^ multiply_2(c_1) ^ multiply_3(c_2) ^ c_3   # [0x01 0x02 0x03 0x01] [c_1] = [c_1'] 
    col[2] = c_0 ^ c_1 ^ multiply_2(c_2) ^ multiply_3(c_3)   # [0x01 0x01 0x02 0x03] [c_2]   [c_2']
    col[3] = multiply_3(c_0) ^ c_1 ^ c_2 ^ multiply_2(c_3)   # [0x03 0x01 0x01 0x02] [c_3]   [c_3']

def mix_columns(state):
    for r in state:
        mix_column(r)

#converts bytes to 2D list representing a state
def state_from_bytes(data):
    state = [data[i*4:(i+1)*4] for i in range(len(data) // 4)]
    return state

#converts state into bytes
def bytes_from_state(state):
    return bytes(state[0] + state[1] + state[2] + state[3])


def aes_encryption(data, key):

    key_length_bits = len(key) * 8

    if key_length_bits == 128:
        no_rounds = 10
    elif key_length_bits == 192:
        no_rounds = 12
    else:  # 256-bit keys
        no_rounds = 14

    state = state_from_bytes(data)

    key_schedule = key_expansion(key)

    add_round_key(state, key_schedule, round=0)

    for round in range(1, no_rounds):
        sub_bytes(state)
        shift_rows(state)
        mix_columns(state)
        add_round_key(state, key_schedule, round)

    sub_bytes(state)
    shift_rows(state)
    add_round_key(state, key_schedule, round=no_rounds)

    cipher = bytes_from_state(state)
    return cipher


inv_s_box_string = '52 09 6a d5 30 36 a5 38 bf 40 a3 9e 81 f3 d7 fb' \
                   '7c e3 39 82 9b 2f ff 87 34 8e 43 44 c4 de e9 cb' \
                   '54 7b 94 32 a6 c2 23 3d ee 4c 95 0b 42 fa c3 4e' \
                   '08 2e a1 66 28 d9 24 b2 76 5b a2 49 6d 8b d1 25' \
                   '72 f8 f6 64 86 68 98 16 d4 a4 5c cc 5d 65 b6 92' \
                   '6c 70 48 50 fd ed b9 da 5e 15 46 57 a7 8d 9d 84' \
                   '90 d8 ab 00 8c bc d3 0a f7 e4 58 05 b8 b3 45 06' \
                   'd0 2c 1e 8f ca 3f 0f 02 c1 af bd 03 01 13 8a 6b' \
                   '3a 91 11 41 4f 67 dc ea 97 f2 cf ce f0 b4 e6 73' \
                   '96 ac 74 22 e7 ad 35 85 e2 f9 37 e8 1c 75 df 6e' \
                   '47 f1 1a 71 1d 29 c5 89 6f b7 62 0e aa 18 be 1b' \
                   'fc 56 3e 4b c6 d2 79 20 9a db c0 fe 78 cd 5a f4' \
                   '1f dd a8 33 88 07 c7 31 b1 12 10 59 27 80 ec 5f' \
                   '60 51 7f a9 19 b5 4a 0d 2d e5 7a 9f 93 c9 9c ef' \
                   'a0 e0 3b 4d ae 2a f5 b0 c8 eb bb 3c 83 53 99 61' \
                   '17 2b 04 7e ba 77 d6 26 e1 69 14 63 55 21 0c 7d'.replace(" ", "")

inv_s_box = bytearray.fromhex(inv_s_box_string)


def inv_sub_bytes(state):
    for r in range(len(state)):
        state[r] = [inv_s_box[state[r][c]] for c in range(len(state[0]))]
        
def inv_shift_rows(state):
    state[1][1], state[2][1], state[3][1], state[0][1] = state[0][1], state[1][1], state[2][1], state[3][1]
    state[2][2], state[3][2], state[0][2], state[1][2] = state[0][2], state[1][2], state[2][2], state[3][2]
    state[3][3], state[0][3], state[1][3], state[2][3] = state[0][3], state[1][3], state[2][3], state[3][3]
    return


def multiply_2s_0e(b):
    # 0x0e = 14 = b1110 = ((x * 2 + x) * 2 + x) * 2
    return multiply_2(multiply_2(multiply_2(b) ^ b) ^ b)
def multiply_2s_0b(b):
    # 0x0b = 11 = b1011 = ((x*2)*2+x)*2+x
    return multiply_2(multiply_2(multiply_2(b)) ^ b) ^ b
def multiply_2s_0d(b):
    # 0x0d = 13 = b1101 = ((x*2+x)*2)*2+x
    return multiply_2(multiply_2(multiply_2(b) ^ b)) ^ b
def multiply_2s_09(b):
    # 0x09 = 9  = b1001 = ((x*2)*2)*2+x
    return multiply_2(multiply_2(multiply_2(b))) ^ b


def inv_mix_column(col):
    c_0, c_1, c_2, c_3 = col[0], col[1], col[2], col[3]
    col[0] = multiply_2s_0e(c_0) ^ multiply_2s_0b(c_1) ^ multiply_2s_0d(c_2) ^ multiply_2s_09(c_3) # [0x0e 0x0b 0x0d 0x09] [c_0]   [c_0']
    col[1] = multiply_2s_09(c_0) ^ multiply_2s_0e(c_1) ^ multiply_2s_0b(c_2) ^ multiply_2s_0d(c_3) # [0x09 0x0e 0x0b 0x0d] [c_1] = [c_1']
    col[2] = multiply_2s_0d(c_0) ^ multiply_2s_09(c_1) ^ multiply_2s_0e(c_2) ^ multiply_2s_0b(c_3) # [0x0d 0x09 0x0e 0x0b] [c_2]   [c_2']
    col[3] = multiply_2s_0b(c_0) ^ multiply_2s_0d(c_1) ^ multiply_2s_09(c_2) ^ multiply_2s_0e(c_3) # [0x0b 0x0d 0x09 0x0e] [c_3]   [c_3']


def inv_mix_columns(state):
    for r in state:
        inv_mix_column(r)

def aes_decryption(cipher, key):

    key_byte_length = len(key)
    key_length_bits = key_byte_length * 8

    if key_length_bits == 128:
        no_rounds = 10
    elif key_length_bits == 192:
        no_rounds = 12
    else:  # 256-bit keys
        no_rounds = 14

    state = state_from_bytes(cipher)
    key_schedule = key_expansion(key)
    add_round_key(state, key_schedule, round=no_rounds)

    for round in range(no_rounds-1, 0, -1):
        inv_shift_rows(state)
        inv_sub_bytes(state)
        add_round_key(state, key_schedule, round)
        inv_mix_columns(state)

    inv_shift_rows(state)
    inv_sub_bytes(state)
    add_round_key(state, key_schedule, round=0)

    plain = bytes_from_state(state)
    return plain

def add_padding(data, block_size: int = 32):
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length] * padding_length)
    return data + padding

def remove_padding(data):
    padding_length = data[-1]
    return data[:-padding_length]

def aes_encrypt(plaintext_string, key_string):
    plaintext_hex = binascii.hexlify(plaintext_string.encode()).decode('utf-8')
    plaintext_hex_padded = add_padding(bytearray.fromhex(plaintext_hex)).hex()
    
    block_size = 32
    blocks = [plaintext_hex_padded[i:i+block_size] for i in range(0, len(plaintext_hex_padded), block_size)]
    encrypted_blocks = []
    for block in blocks:
        plaintext_block = bytearray.fromhex(block)
        ciphertext_block = aes_encryption(plaintext_block, key_string.encode())
        encrypted_blocks.append(ciphertext_block)
    
    encrypted_data = b'_'.join(encrypted_blocks)
    return encrypted_data

def aes_decrypt(ciphertext_string, key_string):
    hex_cipher_blocks = ciphertext_string.split(b'_')
    decrypted_blocks = []
    for block in hex_cipher_blocks:
        # cipher_byte = bytearray.fromhex(block)
        decrypted_block = aes_decryption(block, key_string.encode())
        decrypted_blocks.append(decrypted_block)
    decrypted_text_bytes = b''.join(decrypted_blocks)
    decrypted_text_without_padding = remove_padding(decrypted_text_bytes)
    decrypted_text = decrypted_text_without_padding.decode('utf-8')
    return decrypted_text
