from screeninfo import get_monitors
import ctypes

def get_dpi():
    # 获取系统DPI
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    hdc = user32.GetDC(0)
    dpi_x = ctypes.windll.gdi32.GetDeviceCaps(hdc, 88)  # LOGPIXELSX
    dpi_y = ctypes.windll.gdi32.GetDeviceCaps(hdc, 90)  # LOGPIXELSY
    user32.ReleaseDC(0, hdc)
    return dpi_x, dpi_y

def main():
    dpi_x, dpi_y = get_dpi()
    for monitor in get_monitors():
        print(f"显示器: {monitor.name}")
        print(f"分辨率: {monitor.width}x{monitor.height} 像素")
        print(f"物理尺寸: {monitor.width_mm}x{monitor.height_mm} 毫米")
        
        # 计算逻辑尺寸
        logical_width = monitor.width * (96 / dpi_x)
        logical_height = monitor.height * (96 / dpi_y)
        print(f"逻辑尺寸: {logical_width}x{logical_height} 像素")
        
        # DPI
        print(f"DPI: {dpi_x}x{dpi_y}")
        
        # PPI计算
        ppi = ((monitor.width / (monitor.width_mm / 25.4)) + (monitor.height / (monitor.height_mm / 25.4))) / 2
        print(f"PPI: {ppi}")
        
        # 缩放比例
        scale = (dpi_x / 96) * 100
        print(f"缩放: {scale}%")
        
        print("-" * 20)

if __name__ == "__main__":
    main()
