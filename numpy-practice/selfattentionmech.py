import numpy as np

np.random.seed(42)

def softmax(x):
    x = x - np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

def self_attention(X, Wq, Wk, Wv):
    Q = X @ Wq
    K = X @ Wk
    V = X @ Wv

    dk = Q.shape[-1]

    scores = Q @ K.T
    scores = scores / np.sqrt(dk)

    attention = softmax(scores)

    output = attention @ V

    return output, attention

seq_len = 6
d_model = 8
d_k = 8

X = np.random.randn(seq_len, d_model)

Wq = np.random.randn(d_model, d_k)
Wk = np.random.randn(d_model, d_k)
Wv = np.random.randn(d_model, d_k)

output, attention = self_attention(X, Wq, Wk, Wv)

print("Input Shape:", X.shape)
print("Query Shape:", (X @ Wq).shape)
print("Key Shape:", (X @ Wk).shape)
print("Value Shape:", (X @ Wv).shape)

print("\nAttention Matrix:")
print(np.round(attention, 3))

print("\nAttention Row Sums:")
print(np.round(np.sum(attention, axis=1), 3))

print("\nOutput Shape:", output.shape)

print("\nAttention Output:")
print(np.round(output, 3))

token_names = [
    "I",
    "love",
    "learning",
    "Python",
    "and",
    "AI"
]

print("\nToken Attention:")
for i in range(seq_len):
    print(token_names[i], "->", np.round(attention[i], 3))

strongest = np.argmax(attention, axis=1)

print("\nStrongest Connections:")
for i in range(seq_len):
    print(
        token_names[i],
        "->",
        token_names[strongest[i]],
        "Score:",
        round(attention[i, strongest[i]], 3)
    )
