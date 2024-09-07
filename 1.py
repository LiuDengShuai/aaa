from scipy.stats import norm
# 给定参数
p = 0.10  # 次品率
E = 0.05  # 次品率误差
power = 0.80  # 功效
# 计算样本大小
# 情形 1: 95% 置信水平
alpha_1 = 0.05
Z_alpha_1 = norm.ppf(1 - alpha_1 / 2)
Z_beta_1 = norm.ppf(power)
n_1 = ((Z_alpha_1 * norm.ppf(0.975) * norm.ppf(0.9) * 2 * p * (1 - p) + Z_beta_1 * norm.ppf(0.8) * norm.ppf(0.9) * p * (1 - p)) / E) ** 2
# 情形 2: 90% 置信水平
alpha_2 = 0.10
Z_alpha_2 = norm.ppf(1 - alpha_2 / 2)
Z_beta_2 = norm.ppf(power)
n_2 = ((Z_alpha_2 * norm.ppf(0.95) * norm.ppf(0.8) * 2 * p * (1 - p) + Z_beta_2 * norm.ppf(0.8) * norm.ppf(0.8) * p * (1 - p)) / E) **2
print(n_1,n_2)