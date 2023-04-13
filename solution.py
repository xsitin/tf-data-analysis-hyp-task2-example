import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 385459798 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.1
    p_val = anderson_ksamp([x, y]).pvalue
    return p_val < alpha