import timeit
import numpy as np


class EvalDict:
    def __init__(self, test_dict: dict, n: int, size: int = 40001):
        self.original_dict = test_dict
        self.test_dict = test_dict
        self.size = size
        self.n = n        

    def set_size(self, size):
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

    def evaluation(self):
        n = self.n
        ##### evaluating insertion #####
        execution_time_insertion = []
        for _ in range(n):
            exec_time = timeit.timeit(self.insertion_test, globals=globals(), number=1)
            self.test_dict = self.original_dict
            execution_time_insertion.append(exec_time)

        ##### evaluating replacing #####
        execution_time_replacing = []
        for _ in range(n):
            exec_time = timeit.timeit(self.replacing_test, globals=globals(), number=1)
            self.test_dict = {f"{i}": i for i in range(self.size)}
            execution_time_replacing.append(exec_time)

        ##### evaluating removing - TOP DOWN #####
        execution_time_poping_top = []
        for _ in range(n):
            exec_time = timeit.timeit(self.removing_test_top_down, globals=globals(), number=1)
            self.test_dict = {f"{i}": i for i in range(self.size)}
            execution_time_poping_top.append(exec_time)

        ##### evaluating removing - BOTTOM UP #####
        execution_time_poping_bottom = []
        for _ in range(n):
            exec_time = timeit.timeit(self.removing_test_bottom_up, globals=globals(), number=1)
            self.test_dict = {f"{i}": i for i in range(self.size)}
            execution_time_poping_bottom.append(exec_time)

        times = {
                 "insertion": execution_time_insertion,
                 "replacing": execution_time_replacing,
                 "removing_top": execution_time_poping_top,
                 "removing_bottom": execution_time_poping_bottom
                 }

        return times

    def adjusting_samples(self, dict_tempos):
        medias_agrupadas = {}
        group_size = 10
        for key, value in dict_tempos.items():
            medias_agrupadas[key] = []
            for i in range(0, len(value), group_size):
                grupo = value[i:i + group_size]
                media_grupo = np.mean(grupo)
                medias_agrupadas[key].append(media_grupo)

        return medias_agrupadas

    def calc_mean(self, dic):
        result = {}
        for k, v in dic.items():
            result[k] = np.mean(v) * (10**6)

        return result

    def evaluation_with_size_variation(self, sizes):
        results = {}

        for size in sizes:
            self.test_dict = self.original_dict
            self.set_size(size)

            mean_times = self.evaluation()
            mean_times = self.adjusting_samples(mean_times)
            mean_times = self.calc_mean(mean_times)
            results[size] = mean_times

        return results
