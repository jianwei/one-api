import subprocess

def check_go_environment():
    # 检查Go版本和GOROOT完整性
    print("正在验证Go环境状态...")
    
    # 1. 获取Go版本
    go_version = subprocess.run(["go", "version"], capture_output=True, text=True)
    if go_version.returncode != 0:
        print(f"ERROR: Go环境未正确安装，运行 'go version' 失败：{go_version.stderr}")
        return
    
    # 2. 检查slices包是否存在
    go_root = subprocess.run(["go", "env", "GOROOT"], capture_output=True, text=True).stdout.strip()
    slices_path = f"{go_root}/src/slices"
    has_slices = subprocess.run(["ls", slices_path], capture_output=True, text=True).returncode == 0
    
    print(f"Go版本: {go_version.stdout.strip()}")
    print(f"GOROOT路径: {go_root}")
    print(f"是否存在slices包？ {'✅ 存在' if has_slices else '❌ 不存在'}")

    if not has_slices:
        print("⚠️ 关键错误: slices包未在标准库中找到")
        print("----- 修复建议: 执行以下步骤 -----")
        print("1. 卸载当前Go版本: sudo apt remove --purge golang")
        print("2. 安装最新Go版本:")
        print("   wget https://golang.org/dl/go1.21.3.linux-amd64.tar.gz")
        print("   sudo tar -C /usr/local -xzf go1.21.3.linux-amd64.tar.gz")
        print("3. 设置环境变量: echo 'export PATH=/usr/local/go/bin:$PATH' >> ~/.bashrc")
        print("4. 重启终端或执行: source ~/.bashrc")

def run_diagnosis():
    check_go_environment()
    print("\n--- 验证Go工作流 ---")
    print("尝试构建示例程序以验证环境：")
    try:
        subprocess.run(["go", "run", "/dev/stdin"], input="package main\nimport \"fmt\"\nfunc main() { fmt.Println('修复验证成功！') }\n", text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"构建失败：{e}")
        print("请先修复Go环境后再尝试构建")

run_diagnosis()
