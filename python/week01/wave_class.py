# ============================================================
# Week 1 Day 5 - Complete Wave Class Implementation
# ============================================================
# Comprehensive implementation of wave classes:
# 1. Basic Wave class
# 2. Extended Wave class with additional methods
# 3. Specialized wave types: TravellingWave, StandingWave
#
# This file combines all Day 5 Python work into a single,
# complete, runnable module.
# ============================================================

import numpy as np
import matplotlib.pyplot as plt


class Wave:
    """
    基本波形类：表示一个正弦波
    
    属性（Attributes）：
    - amplitude: 振幅 (A)
    - frequency: 频率 (f, Hz)
    - phase: 相位 (φ, rad)
    - omega: 角频率 (ω = 2πf)
    
    方法（Methods）：
    - evaluate(t): 计算波在时间t的值
    - plot(): 绘制一个完整周期的波形
    - info(): 打印波的基本信息
    - shift_phase(delta_phi): 相位移动
    - add_wave(other_wave): 波形叠加
    - sample(t_array): 多点采样
    """
    
    def __init__(self, amplitude, frequency, phase=0):
        """
        构造方法
        
        参数：
        - amplitude: 振幅（浮点数）
        - frequency: 频率（浮点数，单位Hz）
        - phase: 相位（浮点数，单位rad，默认为0）
        """
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase
        self.omega = 2 * np.pi * frequency  # 计算角频率
    
    def evaluate(self, t):
        """
        计算波在时间t的值
        
        公式: y(t) = A * sin(ωt + φ)
        
        参数：
        - t: 时间点（可以是数组）
        
        返回：
        - 波的值（浮点数或numpy数组）
        """
        return self.amplitude * np.sin(self.omega * t + self.phase)
    
    def plot(self):
        """
        绘制一个完整周期的波形图
        """
        # 计算一个完整周期
        period = 1.0 / self.frequency
        t = np.linspace(0, period, 1000)
        y = self.evaluate(t)
        
        # 创建图形
        plt.figure(figsize=(10, 4))
        plt.plot(t * 1000, y)  # 转换为毫秒
        plt.xlabel('Time (ms)')
        plt.ylabel('Amplitude')
        plt.title(f'Wave: A={self.amplitude}, f={self.frequency} Hz, φ={self.phase:.2f} rad')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    
    def info(self):
        """
        打印波的基本信息
        """
        print(f"Wave information:")
        print(f"  amplitude: {self.amplitude}")
        print(f"  frequency: {self.frequency} Hz")
        print(f"  angular frequency: {self.omega:.2f} rad/s")
        print(f"  phase: {self.phase:.2f} rad")
        print(f"  period: {1/self.frequency:.4f} s")
    
    def shift_phase(self, delta_phi):
        """
        相位移动方法
        
        参数：
        - delta_phi: 相位变化量（单位rad）
        
        功能：
        - 直接修改对象的phase属性
        - 返回None（修改器方法）
        """
        self.phase += delta_phi
        print(f"相位已移动 {delta_phi:.2f} rad，新相位: {self.phase:.2f} rad")
    
    def add_wave(self, other_wave):
        """
        波形叠加方法
        
        参数：
        - other_wave: 另一个Wave对象
        
        返回：
        - 新的Wave对象（振幅相加，频率和相位取第一个波的值）
        """
        new_amplitude = self.amplitude + other_wave.amplitude
        # 频率和相位取第一个波的值
        new_wave = Wave(new_amplitude, self.frequency, self.phase)
        print(f"波形叠加: {self.amplitude} + {other_wave.amplitude} = {new_amplitude}")
        return new_wave
    
    def sample(self, t_array):
        """
        多点采样方法
        
        参数：
        - t_array: 时间点数组（numpy数组）
        
        返回：
        - numpy数组，包含波在各时间点的值
        """
        return np.array([self.evaluate(t) for t in t_array])


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
# 主程序：生成可视化图片
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Week 1 Day 5 - Wave Class Visualization")
    print("=" * 60)
    
    # 创建不同类型的波
    basic_wave = Wave(amplitude=2.0, frequency=10.0)
    travelling_wave = TravellingWave(amplitude=1.0, frequency=10.0, direction=1)
    standing_wave = StandingWave(amplitude=1.0, frequency=10.0)
    
    # 创建图形
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 图1：基本波形
    t = np.linspace(0, 0.1, 1000)
    y_basic = basic_wave.evaluate(t)
    axes[0, 0].plot(t * 1000, y_basic, 'b-', linewidth=2)
    axes[0, 0].set_xlabel('Time (ms)')
    axes[0, 0].set_ylabel('Amplitude')
    axes[0, 0].set_title('Basic Wave: A=2.0, f=10 Hz')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(y=0, color='k', linestyle='-', alpha=0.3)
    
    # 图2：行波 - 空间分布
    x = np.linspace(0, 0.5, 1000)
    for t_val in [0, 0.025, 0.05]:
        y_trav = travelling_wave.evaluate(t_val, x)
        axes[0, 1].plot(x * 100, y_trav, label=f't={t_val*1000:.1f} ms')
    axes[0, 1].set_xlabel('Position (cm)')
    axes[0, 1].set_ylabel('Amplitude')
    axes[0, 1].set_title('Travelling Wave: Spatial Distribution')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # 图3：驻波 - 空间分布
    for t_val in [0, 0.025, 0.05]:
        y_stand = standing_wave.evaluate(t_val, x)
        axes[1, 0].plot(x * 100, y_stand, label=f't={t_val*1000:.1f} ms')
    axes[1, 0].set_xlabel('Position (cm)')
    axes[1, 0].set_ylabel('Amplitude')
    axes[1, 0].set_title('Standing Wave: Spatial Distribution')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axhline(y=0, color='r', linestyle=':', alpha=0.5)
    
    # 图4：波形叠加
    wave1 = Wave(amplitude=1.5, frequency=10.0)
    wave2 = Wave(amplitude=0.5, frequency=20.0, phase=np.pi/2)
    wave3 = wave1.add_wave(wave2)
    
    t = np.linspace(0, 0.1, 1000)
    y1 = wave1.evaluate(t)
    y2 = wave2.evaluate(t)
    y3 = wave3.evaluate(t)
    
    axes[1, 1].plot(t * 1000, y1, 'b-', label='Wave 1: A=1.5, f=10 Hz', alpha=0.7)
    axes[1, 1].plot(t * 1000, y2, 'g-', label='Wave 2: A=0.5, f=20 Hz', alpha=0.7)
    axes[1, 1].plot(t * 1000, y3, 'r-', linewidth=2, label='Superposed Wave')
    axes[1, 1].set_xlabel('Time (ms)')
    axes[1, 1].set_ylabel('Amplitude')
    axes[1, 1].set_title('Wave Superposition')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('wave_visualization.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print("\nVisualization saved as 'wave_visualization.png'")
    print("This demonstrates:")
    print("1. Basic wave properties (amplitude, frequency, phase)")
    print("2. Travelling wave spatial-temporal behavior")
    print("3. Standing wave node patterns")
    print("4. Wave superposition principle")