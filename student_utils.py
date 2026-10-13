def parse_student(line):
    line = line.strip()
    # 空行判定
    if not line:
        raise ValueError("空行，无有效数据")
    # 按逗号分割
    parts = line.split(",")
    # 检查字段数量
    if len(parts) != 2:
        raise ValueError(f"字段数量错误，期望2个，实际{len(parts)}个")
    name, score_str = parts
    name = name.strip()
    score_str = score_str.strip()
    # 检查姓名
    if not name:
        raise ValueError("姓名为空")
    # 成绩转整数
    try:
        score = int(score_str)
    except ValueError:
        raise ValueError(f"成绩'{score_str}'无法转换为整数")
    # 检查成绩范围
    if score < 0 or score > 100:
        raise ValueError(f"成绩{score}超出0~100范围")
    return {"name": name, "score": score}