"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""

def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    # 请在下方编写代码
    # 统一处理为小写，避免大小写敏感
    operation = operation.lower()

    if operation == "add":
        # 期望 args = (new_student,)
        if not args:
            raise ValueError("add 操作必须提供要添加的学生")
        new_student = args[0]
        students.append(new_student)

    elif operation == "remove":
        # 期望 args = (student_name,)
        if not args:
            raise ValueError("remove 操作必须提供要删除的学生姓名")
        student_name = args[0]
        if student_name in students:
            students.remove(student_name)
        else:
            raise ValueError(f"学生 {student_name} 不存在")

    elif operation == "update":
        # 期望 args = (old_name, new_name)
        if len(args) < 2:
            raise ValueError("update 操作必须提供 old_name 和 new_name")
        old_name, new_name = args[0], args[1]
        try:
            idx = students.index(old_name)
            students[idx] = new_name
        except ValueError:
            raise ValueError(f"学生 {old_name} 不存在")

    else:
        raise ValueError(f"不支持的操作类型: {operation}")

    return students
    pass 