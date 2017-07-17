# coding: utf-8
import sys, time
import threading


def split_list_item_to_group(item_list, group_count):
    """
    将传入的List中的元素拆分到多个List中，再将这些List作为一个List返回
    :param item_list:
    :param group_count:
    :return:
    """
    item_group_list = list()
    for n in range(0, group_count):
        item_group_list.append(list())
    for num in range(0, len(item_list)):
        mod_num = num % group_count
        item_group_list[mod_num].append(item_list[num])
    return item_group_list


def print_number_with_thread(thread_paras):
    number_group = thread_paras["number_group"]
    for number in number_group:
        print("number is {0}".format(number))
        time.sleep(0.1)


def demo():
    number_list = list()
    thread_count = 10
    thread_list = list()
    for number in range(0, 100000):
        number_list.append(number)
    number_group_list = split_list_item_to_group(number_list, thread_count)
    for number_group in number_group_list:
        thread_paras = {
            "number_group": number_group,
        }
        thread_item = threading.Thread(target=print_number_with_thread, args=(thread_paras,))
        thread_list.append(thread_item)
        thread_item.start()
    running_thread_count = thread_count
    while running_thread_count > 0:
        running_thread_count = len(filter(lambda item: item.isAlive(), thread_list))
        print("正在运行的线程数：{0}".format(running_thread_count))
        time.sleep(1)
    print("多线程执行完成")

if __name__ == '__main__':
    demo()

