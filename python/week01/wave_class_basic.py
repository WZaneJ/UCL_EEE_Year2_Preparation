# ============================================================
# Week 1 Day 5 - 基本Wave类
# ============================================================
# 实现一个基本的正弦波类
# 包含：振幅、频率、相位属性
# 方法：evaluate（计算值）、plot（绘图）、info（打印信息）
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


# ============================================================
# 测试代码
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("测试基本Wave类")
    print("=" * 60)
    
    # 创建波形对象
    wave1 = Wave(amplitude=2.0, frequency=50.0)
    wave2 = Wave(amplitude=1.5, frequency=100.0, phase=np.pi/4)
    
    # 打印信息
    print("\n波形1的信息:")
    wave1.info()
    
    print("\n波形2的信息:")
    wave2.info()
    
    # 计算特定时间点的值
    t = 0.01  # 10 ms
    print(f"\n在 t={t} s 时:")
    print(f"  wave1 的值: {wave1.evaluate(t):.4f}")
    print(f"  wave2 的值: {wave2.evaluate(t):.4f}")
    
    # 绘制波形
    print("\n正在绘制波形...")
    wave1.plot()