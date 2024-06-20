import timeit


class EvalDict:
    def __init__(self, test_dict: dict, size: int = 40001):
        self.original_dict = test_dict
        self.test_dict = test_dict
        self.size = size

    def insertion_test(self):
        for num in range(self.size):
            self.test_dict[str(num)] = num

    def replacing_test(self):
        for num in range(self.size):
            self.test_dict[str(num)] = 1 - num  # replacing existent values

    def removing_test_top_down(self):
        for num in range(self.size):
            self.test_dict.pop(str(num))

    def removing_test_bottom_up(self):
        for num in range(self.size - 1, -1, -1):
            self.test_dict.pop(str(num))

    def evaluation(self, n: int = 1000):
        ##### evaluating insertion #####
        execution_time_insertion = []
        for _ in range(n):
            exec_time = timeit.timeit(self.insertion_test, globals=globals(), number=1)
            self.test_dict = self.original_dict
            execution_time_insertion.append(exec_time)

        ##### evaluating replacing #####
        execution_time_replacing = []
        self.dict_full = {f"{i}": i for i in range(self.size)}
        for _ in range(n):
            exec_time = timeit.timeit(self.replacing_test, globals=globals(), number=1)
            self.test_dict = self.dict_full
            execution_time_replacing.append(exec_time)

        ##### evaluating removing - TOP DOWN #####
        execution_time_poping_top = []
        for _ in range(n):
            exec_time = timeit.timeit(self.removing_test_top_down, globals=globals(), number=1)
            self.test_dict = self.dict_full
            execution_time_poping_top.append(exec_time)

        ##### evaluating removing - BOTTOM UP #####
        execution_time_poping_bottom = []
        for _ in range(n):
            exec_time = timeit.timeit(self.removing_test_bottom_up, globals=globals(), number=1)
            self.test_dict = self.dict_full
            execution_time_poping_bottom.append(exec_time)
