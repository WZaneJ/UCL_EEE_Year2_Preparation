# ============================================================
# Week 1 Day 5 - 行波和驻波类
# ============================================================
# 实现两种特殊波动类型：
# 1. TravellingWave（行波）：具有传播方向
# 2. StandingWave（驻波）：节点固定的波
# 比较两者在数学表达式和物理特性上的区别
# ============================================================

import numpy as np
import matplotlib.pyplot as plt


class Wave:
    """基本波形类（父类）"""
    
    def __init__(self, amplitude, frequency, phase=0):
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase
        self.omega = 2 * np.pi * frequency
    
    def evaluate(self, t, x=0):
        """基本正弦波（不考虑空间位置）"""
        return self.amplitude * np.sin(self.omega * t + self.phase)


class TravellingWave(Wave):
    """
    行波类：具有传播方向的波
    
    数学表达式：
    y(t,x) = A * sin(ωt - βx + φ)  （正方向）
    y(t,x) = A * sin(ωt + βx + φ)  （负方向）
    
    其中 β = ω/v (波数)，假设波速 v = 1 m/s 简化计算
    """
    
    def __init__(self, amplitude, frequency, phase=0, direction=1):
        """
        参数：
        - direction: 传播方向，+1表示正方向，-1表示负方向
        """
        super().__init__(amplitude, frequency, phase)
        self.direction = direction
    
    def evaluate(self, t, x=0):
        """
        计算行波在时间t、位置x的值
        
        行波公式: y(t,x) = A * sin(ωt - βx + φ)
        其中 β = ω/v (波数)，假设波速 v = 1 m/s
        """
        # 假设波速 v = 1 m/s，所以 β = ω
        beta = self.omega
        return self.amplitude * np.sin(self.omega * t - self.direction * beta * x + self.phase)


class StandingWave(Wave):
    """
    驻波类：由两列相反方向行波叠加形成
    
    数学表达式：
    y(t,x) = 2A * cos(βx) * sin(ωt + φ)
    
    特点：
    - 节点位置固定：x = (2n+1)π/(2β)
    - 腹点位置固定：x = nπ/β
    - 能量不传播，在节点间振荡
    """
    
    def __init__(self, amplitude, frequency, phase=0):
        super().__init__(amplitude, frequency, phase)
    
    def evaluate(self, t, x=0):
        """
        计算驻波在时间t、位置x的值
        
        驻波公式: y(t,x) = 2A * cos(βx) * sin(ωt + φ)
        """
        # 假设波速 v = 1 m/s，所以 β = ω
        beta = self.omega
        return 2 * self.amplitude * np.cos(beta * x) * np.sin(self.omega * t + self.phase)


# ============================================================
# 测试代码
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("测试行波和驻波类")
    print("=" * 60)
    
    # 创建波形对象
    travelling_wave = TravellingWave(amplitude=1.0, frequency=10.0, direction=1)
    standing_wave = StandingWave(amplitude=1.0, frequency=10.0)
    
    # 打印信息
    print("\n行波信息:")
    print(f"  振幅: {travelling_wave.amplitude}")
    print(f"  频率: {travelling_wave.frequency} Hz")
    print(f"  方向: {'正方向' if travelling_wave.direction == 1 else '负方向'}")
    
    print("\n驻波信息:")
    print(f"  振幅: {standing_wave.amplitude}")
    print(f"  频率: {standing_wave.frequency} Hz")
    
    # 比较两种波在不同位置的特性
    print("\n" + "-" * 40)
    print("比较行波和驻波:")
    
    # 固定时间 t=0，观察空间分布
    t_fixed = 0
    x = np.linspace(0, 0.5, 1000)  # 0到0.5米
    
    y_travelling = travelling_wave.evaluate(t_fixed, x)
    y_standing = standing_wave.evaluate(t_fixed, x)
    
    print(f"在 t={t_fixed} s 时:")
    print(f"  行波在 x=0 处: {travelling_wave.evaluate(t_fixed, 0):.4f}")
    print(f"  驻波在 x=0 处: {standing_wave.evaluate(t_fixed, 0):.4f}")
    
    # 绘制比较图
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # 行波：不同时间的空间分布
    ax1.set_title('Travelling Wave: Spatial distribution at different times')
    for t_val in [0, 0.025, 0.05, 0.075]:
        y = travelling_wave.evaluate(t_val, x)
        ax1.plot(x * 100, y, label=f't={t_val*1000:.1f} ms')
    ax1.set_xlabel('Position (cm)')
    ax1.set_ylabel('Amplitude')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 驻波：不同时间的空间分布
    ax2.set_title('Standing Wave: Spatial distribution at different times')
    for t_val in [0, 0.025, 0.05, 0.075]:
        y = standing_wave.evaluate(t_val, x)
        ax2.plot(x * 100, y, label=f't={t_val*1000:.1f} ms')
    ax2.set_xlabel('Position (cm)')
    ax2.set_ylabel('Amplitude')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # 绘制动画效果（静态展示）
    print("\n正在绘制波形对比图...")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # 行波：固定位置的时间变化
    x_fixed = 0  # 固定位置 x=0
    t = np.linspace(0, 0.2, 1000)
    y_trav = travelling_wave.evaluate(t, x_fixed)
    y_stand = standing_wave.evaluate(t, x_fixed)
    
    ax1.plot(t * 1000, y_trav, label='Travelling Wave')
    ax1.plot(t * 1000, y_stand, label='Standing Wave', linestyle='--')
    ax1.set_xlabel('Time (ms)')
    ax1.set_ylabel('Amplitude')
    ax1.set_title(f'Wave at x={x_fixed} cm')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 驻波：节点和腹点标记
    x = np.linspace(0, 0.3, 1000)
    t_fixed = 0
    y_standing = standing_wave.evaluate(t_fixed, x)
    
    ax2.plot(x * 100, y_standing, label='Standing Wave at t=0')
    # 标记节点（振幅为0的点）
    ax2.axhline(y=0, color='r', linestyle=':', alpha=0.5, label='Node line')
    ax2.set_xlabel('Position (cm)')
    ax2.set_ylabel('Amplitude')
    ax2.set_title('Standing Wave Spatial Pattern')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print("\n分析结果:")
    print("1. 行波：波形随时间在空间中传播，能量随波传播")
    print("2. 驻波：波形不传播，节点固定，能量在节点间振荡")
    print("3. 数学区别：行波有 -βx 项，驻波有 cos(βx) 因子")