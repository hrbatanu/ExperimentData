#!/usr/bin/env python3
"""
计算无限二维正方形电阻网格中对角线上两点之间的电阻

对于无限大的二维正方形均匀电阻网格，从原点(0,0)到点(n,n)的电阻
可以通过格林函数方法或随机游走理论计算。

理论结果：R(n,n) ∝ ln(n) （当n很大时）
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from scipy.sparse.linalg import spsolve


def calculate_resistance_finite_grid(n, grid_size=None):
    """
    在有限网格中计算从(0,0)到(n,n)的电阻

    参数:
        n: 目标点的对角线坐标
        grid_size: 网格大小（默认为5*n以近似无限网格）

    返回:
        电阻值（以单位电阻R0为单位）
    """
    if grid_size is None:
        grid_size = max(5 * n, 20)

    # 节点数量
    N = (2 * grid_size + 1) ** 2

    # 节点索引函数
    def node_index(i, j):
        return (i + grid_size) * (2 * grid_size + 1) + (j + grid_size)

    # 构建拉普拉斯矩阵
    row, col, data = [], [], []

    for i in range(-grid_size, grid_size + 1):
        for j in range(-grid_size, grid_size + 1):
            idx = node_index(i, j)

            # 对角元素（连接数）
            degree = 0

            # 右边的连接
            if i < grid_size:
                degree += 1
                neighbor = node_index(i + 1, j)
                row.append(idx)
                col.append(neighbor)
                data.append(-1)

            # 左边的连接
            if i > -grid_size:
                degree += 1
                neighbor = node_index(i - 1, j)
                row.append(idx)
                col.append(neighbor)
                data.append(-1)

            # 上边的连接
            if j < grid_size:
                degree += 1
                neighbor = node_index(i, j + 1)
                row.append(idx)
                col.append(neighbor)
                data.append(-1)

            # 下边的连接
            if j > -grid_size:
                degree += 1
                neighbor = node_index(i, j - 1)
                row.append(idx)
                col.append(neighbor)
                data.append(-1)

            # 对角元素
            row.append(idx)
            col.append(idx)
            data.append(degree)

    L = sparse.csr_matrix((data, (row, col)), shape=(N, N))

    # 注入电流：从(0,0)注入+I，从(n,n)流出-I
    I = np.zeros(N)
    source_idx = node_index(0, 0)
    sink_idx = node_index(n, n)
    I[source_idx] = 1.0
    I[sink_idx] = -1.0

    # 设置参考电位（接地）
    # 将一个远离的节点设为0电位
    ref_idx = node_index(grid_size, grid_size)

    # 修改矩阵：将参考节点的行设为单位向量
    L = L.tolil()
    L[ref_idx, :] = 0
    L[ref_idx, ref_idx] = 1
    I[ref_idx] = 0
    L = L.tocsr()

    # 求解电位
    V = spsolve(L, I)

    # 计算电阻
    R = V[source_idx] - V[sink_idx]

    return R


def theoretical_resistance(n):
    """
    理论近似公式

    对于大的n，R(n,n) ≈ (R0/π) * ln(n√2) = (R0/π) * [ln(n) + ln(√2)]
    """
    return (1/np.pi) * (np.log(n * np.sqrt(2)))


def main():
    print("=" * 70)
    print("无限二维正方形电阻网格 - 对角线电阻计算")
    print("=" * 70)
    print()

    # 计算不同n值的电阻
    n_values = [1, 2, 3, 4, 5, 8, 10, 15, 20, 25, 30]
    resistances = []
    theoretical = []

    print(f"{'n':<6} {'数值解 R(n,n)':<20} {'理论值 ln(n)':<20} {'R/ln(n)':<15}")
    print("-" * 70)

    for n in n_values:
        R = calculate_resistance_finite_grid(n)
        R_theory = theoretical_resistance(n)
        ln_n = np.log(n)
        ratio = R / ln_n if n > 1 else 0

        resistances.append(R)
        theoretical.append(R_theory)

        print(f"{n:<6} {R:<20.6f} {R_theory:<20.6f} {ratio:<15.6f}")

    print()
    print("=" * 70)
    print("结论：")
    print("=" * 70)
    print()
    print("对于无限大的二维正方形均匀电阻网格，")
    print("从原点(0,0)到对角线上的点(n,n)的电阻：")
    print()
    print("    R(n,n) ∝ ln(n)")
    print()
    print("更精确的公式为：")
    print("    R(n,n) ≈ (R₀/π) × ln(n√2)")
    print()
    print("其中 R₀ 是单根电阻丝的电阻。")
    print()
    print("从上表可以看到，R(n,n)/ln(n) 的比值趋于常数 R₀/π ≈ 0.318R₀")
    print()

    # 绘图
    plt.figure(figsize=(12, 5))

    # 子图1：电阻 vs n
    plt.subplot(1, 2, 1)
    plt.plot(n_values, resistances, 'bo-', label='数值计算', markersize=8)
    plt.plot(n_values, theoretical, 'r--', label='理论值 (R₀/π)ln(n√2)', linewidth=2)
    plt.xlabel('n', fontsize=12)
    plt.ylabel('电阻 R(n,n) [单位: R₀]', fontsize=12)
    plt.title('对角线电阻 vs 距离', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)

    # 子图2：R/ln(n) vs n，验证正比关系
    plt.subplot(1, 2, 2)
    n_values_log = [n for n in n_values if n > 1]
    ratios = [resistances[i] / np.log(n_values[i]) for i in range(len(n_values)) if n_values[i] > 1]
    plt.plot(n_values_log, ratios, 'go-', markersize=8, linewidth=2)
    plt.axhline(y=1/np.pi, color='r', linestyle='--', linewidth=2, label='理论值 R₀/π')
    plt.xlabel('n', fontsize=12)
    plt.ylabel('R(n,n) / ln(n)', fontsize=12)
    plt.title('验证对数关系', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/home/user/ExperimentData/grid_resistance_plot.png', dpi=300, bbox_inches='tight')
    print(f"图表已保存到: /home/user/ExperimentData/grid_resistance_plot.png")
    print()


if __name__ == "__main__":
    main()
