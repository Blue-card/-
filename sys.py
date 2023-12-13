import os

fileName = "student.txt"


def main():
    while True:
        menu()
        choice = int(input("请选择："))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input("你确定要退出系统吗？(Y/N) \n ")
                if answer.lower() == "y":
                    print("谢谢您使用本系统。")
                    break  # 结束本次循环，退出系统
                else:
                    continue
            elif choice == 1:
                Insert()  # 录入学生信息
            elif choice == 2:
                lookUp()  # 查找
            elif choice == 3:
                Delete()  # 删除
            elif choice == 4:
                Replace()  # 修改
            elif choice == 5:
                Sorted()  # 排序
            elif choice == 6:
                Count()  # 排序
            elif choice == 7:
                showAll()  # 排序


def menu():
    print("{:=^45}".format("学生信息管理系统"),
          "\n{:~^48}".format("功能菜单"))
    print("{:<10} {:^10} {:>10}\n{:<10} {:^7} {:>17}\n{:<10} {:>22}"
          .format("1.录入学生信息", "2.查找学生信息",
                  "3.删除学生信息", "4.修改学生信息", "5.排序",
                  "6.统计学生总人数", "7.显示所有学生信息", "0.退出系统"))
    print("{:=^51}".format("="))


def Insert():
    student_list = []
    mark = True
    while mark:
        id = input("请输入学号：")
        if not id:
            break
        name = input("请输入姓名：")
        if not id:
            break

        try:
            Chinese = eval(input("请输入语文成绩："))
            Math = eval(input("请输入数学成绩："))
            English = eval(input("请输入英语成绩："))

        except:
            print("输入的成绩无效，请输入有效的数值。")
            continue
        # 将有效的信息存入字典中
        student = {"id": id, "name": name, "Chinese": Chinese, "Math": Math, "English": English}
        # 将字典添加到学生列表中
        student_list.append(student)

        answer = input("是否继续添加？（Y/N）\n")
        if answer.lower() == "n":
            break
        else:
            continue

    # 将录入的信息保存到本地
    Save(student_list)
    print("学生信息录入完毕。")


def Save(list):
    try:
        stu_txt = open(fileName, 'a+', encoding='utf-8')
    except:
        create_docx = open(fileName, 'w+', encoding='utf-8')
        create_docx.close()
        stu_txt = open(create_docx, 'a+', encoding="utf-8")
    for item in list:
        stu_txt.write(str(item) + "\n")
    stu_txt.close()


def lookUp():
    student_querry = []
    while True:
        id = ""
        name = ""
        if os.path.exists(fileName):
            mode = eval(input("按ID查找请输入1，按姓名查找请输入2："))
            if mode == 1:
                id = input("请输入ID：")
            elif mode == 2:
                name = input("请输入学生姓名：")
            else:
                print("您的输入有误，请重新输入。")
                lookUp()
            with open(fileName, 'r', encoding='utf-8') as rf:
                student = rf.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != "":
                        if d['id'] == id:
                            student_querry.append(d)
                    elif name != "":
                        if d['name'] == name:
                            student_querry.append(d)
            # 显示查询结果
            show_student(student_querry)
            # 清空列表
            student_querry.clear()
            answer = input("是否要继续查询？（Y/N）\n")
            if answer.lower() == "y":
                continue
            else:
                break



        else:
            print("暂未保存学生信息")
            return


def show_student(lst):
    if len(lst) == 0:
        print("没有查到相关学生信息")
        return
        # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format("ID", "姓名", "语文成绩", "数学成绩", "英语成绩", "总成绩"))
    # 定义内容的显示格式
    format_data = "{:^6}\t{:^12}\t{:^11}\t{:^12}\t{:^13}\t{:^10}"
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('Chinese'),
                                 item.get('Math'),
                                 item.get('English'),
                                 int(item.get('Chinese')) + int(item.get('Math')) + int(item.get('English'))
                                 ))


def Delete():
    while True:
        student_id = input("请输入要删除学生的学号：")
        if student_id != "":
            if os.path.exists(fileName):
                with open(fileName, "r", encoding='utf-8') as f:
                    student_old = f.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(fileName, 'w', encoding='utf-8') as nf:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转成字典
                        if d['id'] != student_id:
                            nf.write(str(d) + "\n")
                        else:
                            flag = True
                    if flag:
                        print('ID为{:}学生已经被删除。'.format(student_id))
                    else:
                        print("没有找到ID为{:}的学生".format(student_id))
            else:
                print("无学生信息，请先录入。")
                break
            showAll()  # 删除完成后，重新输出全部学生信息
            answer = input("是否继续删除：(Y/N)")
            if answer.lower() == "y":
                continue
            else:
                break


def Replace():
    showAll()
    if os.path.exists(fileName):
        with open(fileName, 'r', encoding='utf-8') as rf:
            student_old = rf.readlines()
    else:
        return
    student_id = input("请输入要修改的学生的ID：")
    if student_id != '':
        with open(fileName, 'w', encoding="utf-8") as wf:
            for item in student_old:
                d = dict(eval(item))
                if d['id'] == student_id:
                    print('已经找到ID为{:}学生的信息,可以修改。'.format(student_id))
                    while True:
                        try:
                            d['name'] = input('请输入姓名：')
                            d['Chinese'] = input('请输入语文成绩：')
                            d['Math'] = input('请输入数学成绩：')
                            d['English'] = input('请输入英语成绩：')
                        except:
                            print('您的输入有错误，请重新输入。')
                        else:
                            break
                    wf.write(str(d) + "\n")
                    print("修改成功。")
                else:
                    wf.write(str(d) + "\n")
            answer = input("是否需要继续修改学生信息？（Y/N）")
            if answer.lower() == 'y':
                Delete()


def Sorted():
    showAll()
    if os.path.exists(fileName):
        with open(fileName, 'r', encoding='utf-8') as rf:
            students_list = rf.readlines()
        students_new = []
        for item in students_list:
            d = dict(eval(item))
            students_new.append(d)
    else:
        return
    asc_or_desc = input("请选择（0:升序；1：降序): ")
    if asc_or_desc == '1':
        asc_or_desc_bool = True
    elif asc_or_desc == '0':
        asc_or_desc_bool = False
    else:
        print("您的输入有误。")
        Sorted()
    mode = input("请选择按（1.语文成绩；2.数学成绩；3.英语成绩；4.总成绩）来排序")
    if mode == '1':
        students_new.sort(key=lambda students_new: int(students_new['Chinese']), reverse=asc_or_desc_bool)
    elif mode == '2':
        students_new.sort(key=lambda students_new: int(students_new['Math']), reverse=asc_or_desc_bool)
    elif mode == '3':
        students_new.sort(key=lambda students_new: int(students_new['English']), reverse=asc_or_desc_bool)
    elif mode == '4':
        students_new.sort(key=lambda students_new: int(students_new['Chinese']) +
                                                   int(students_new['Math']) +
                                                   int(students_new['English']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误。')
        Sorted()
    show_student(students_new)


def showAll():
    stu_list = []
    if os.path.exists(fileName):
        with open(fileName, 'r', encoding='utf-8') as rf:
            students = rf.readlines()
            for item in students:
                stu_list.append(eval(item))
            if stu_list:
                show_student(stu_list)

    else:
        print('暂未保存学生信息。')


def Count():
    if os.path.exists(fileName):
        with open(fileName, 'r', encoding='utf-8') as rf:
            student_num = rf.readlines()
            if student_num == "":
                print("还未录入学生信息。")
            else:
                print("一共有{:}名学生。".format(len(student_num)))
    else:
        print("暂未保存学生信息。")


if __name__ == '__main__':
    main()

