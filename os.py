import os

def generate_tree(path, prefix='', is_last=True, lines=None):
    """生成树形结构，存入列表而不是print"""
    if lines is None:
        lines = []
    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        return lines

    # 过滤隐藏文件
    items = [item for item in items if not item.startswith('.')]

    for i, item in enumerate(items):
        is_last_item = (i == len(items) - 1)
        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):
            lines.append(prefix + ('└── ' if is_last_item else '├── ') + f'📁 {item}/')
            generate_tree(full_path, prefix + ('    ' if is_last_item else '│   '), is_last_item, lines)
        else:
            lines.append(prefix + ('└── ' if is_last_item else '├── ') + f'📄 {item}')
    return lines

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_name = os.path.basename(script_dir)

    tree_lines = [f'📂 {root_name}/']
    tree_lines.extend(generate_tree(script_dir))

    # 写入txt文件
    with open("tree.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(tree_lines))

    print("✅ 目录树已保存至 tree.txt")
    print('\n' + '='*50)
    input('按回车退出...')
