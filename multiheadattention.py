import numpy as np

def multi_head_attention(X, W_q, W_k, W_v, W_o, num_heads):
    """
    Computes Multi-Head Attention using batch matrix operations.
    
    Parameters:
    - X: Input matrix of shape (batch_size, seq_len, d_model)
    - W_q, W_k, W_v: Projection weights of shape (d_model, d_model)
    - W_o: Output projection weight of shape (d_model, d_model)
    - num_heads: Number of attention heads
    """
    N, L, D = X.shape
    d_k = D // num_heads
    
    Q = np.dot(X, W_q)
    K = np.dot(X, W_k)
    V = np.dot(X, W_v)
    
    Q = Q.reshape(N, L, num_heads, d_k).transpose(0, 2, 1, 3)
    K = K.reshape(N, L, num_heads, d_k).transpose(0, 2, 1, 3)
    V = V.reshape(N, L, num_heads, d_k).transpose(0, 2, 1, 3)
    
    scores = np.matmul(Q, K.transpose(0, 1, 3, 2)) / np.sqrt(d_k)
    
    exp_scores = np.exp(scores - np.max(scores, axis=-1, keepdims=True))
    attn_weights = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)
    
    context = np.matmul(attn_weights, V)
    
    context = context.transpose(0, 2, 1, 3).reshape(N, L, D)
    
    output = np.dot(context, W_o)
    return output, attn_weights

batch_size, seq_len, d_model, heads = 2, 8, 64, 4
X = np.random.randn(batch_size, seq_len, d_model)

W_q = np.random.randn(d_model, d_model)
W_k = np.random.randn(d_model, d_model)
W_v = np.random.randn(d_model, d_model)
W_o = np.random.randn(d_model, d_model)

out, weights = multi_head_attention(X, W_q, W_k, W_v, W_o, heads)

print("Output shape:", out.shape)
print("Attention shape:", weights.shape)
