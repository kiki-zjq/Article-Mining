"""
Using Directions:
    1. Initialize a SASample Class
    E.g. sample = SASample(bg_path, bg_intersect_path, peak_path, peak_intersect_path)
    2. Set proper parameter for this Class, like signal2noise, fragment_number, saving_path, etc. Or just use the default value.
    E.g. sample.set_cores(5)
    3. Use run method to start sample process
    E.g. sample.run()
"""

import heapq
import math
import multiprocessing
import os
import random
import sys
import time
import h5py
import numpy as np
import pandas


class SASample:
    """
    Class Version of SASample_functions
    """
    def __init__(self, bg_path, bg_intersect_path, peak_path, peak_intersect_path, cell_number,
                 first_sample_save_path="first.h5", second_sample_save_path="second.h5", fragment_number=1000,
                 frag_num_var=1, max_threshold=2000, min_threshold=500, signal2noise=0.5, core_number=1):
        """
        Constructor For the SASample Class
        :param bg_path: background counting file path
        :param bg_intersect_path: background intersect file path
        :param peak_path: peak counting file path
        :param peak_intersect_path: peak intersect file path
        :param cell_number: How many cells you wnat to sample from a tissue
        :param first_sample_save_path: The path to save the result of first sample
        :param second_sample_save_path: The path to save the result of second sample
        :param fragment_number: The average value of fragment number for one cell. Default value is 1000
        :param frag_num_var: The variance for fragment number's value. Default value is 1
        :param max_threshold: The maximum threshold for fragment number. Default value is 2000
        :param min_threshold: The minimum threshold for fragment number. Default value is 500
        :param signal2noise: The signal to noise ratio. Default value is 0.5
        :param core_number: The CPU core number you want to use. Default value is 1
        """
        self.bg_path = bg_path
        self.bg_intersect_path = bg_intersect_path
        self.peak_path = peak_path
        self.peak_intersect_path = peak_intersect_path
        self.cell_number = cell_number
        self.fragment_number = fragment_number
        self.first_sample_save_path = first_sample_save_path
        self.second_sample_save_path = second_sample_save_path
        self.frag_num_var = frag_num_var
        self.max_threshold = max_threshold
        self.min_threshold = min_threshold
        self.signal2noise = signal2noise
        self.core_number = core_number

    def set_cores(self, core_number):
        """
        Setter method for core_number
        :param core_number: The CPU Cores Number you want to use in this task
        :return: null
        """
        self.core_number = core_number

    def set_fragment_number(self, fragment_number, frag_num_var):
        """
        Setter method for fragment_number
        :param frag_num_var: The variance for fragment_number
        :param fragment_number: The average number for fragment_number
        :return: null
        """
        self.fragment_number = fragment_number
        self.frag_num_var = frag_num_var

    def set_threshold(self, min_threshold, max_threshold):
        """
        Setter method for threshold
        :param min_threshold: The min threshold for fragment number
        :param max_threshold: The max threshold for fragment number
        :return: null
        """
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold

    def set_signal2noise(self, signal2noise):
        """
        setter method for signal2noise
        :param signal2noise: The SNR to split the fragment number into two parts
        :return: null
        """
        self.signal2noise = signal2noise

    def set_save_path(self, first_sample_save_path, second_sample_save_path):
        """
        Setter method for first_sample_save_path and second_sample_save_path
        :param first_sample_save_path: The path to save the result of first sample
        :param second_sample_save_path: The path to save the result of second sample
        :return: null
        """
        self.first_sample_save_path = first_sample_save_path
        self.second_sample_save_path = second_sample_save_path

    def __reading_file(self, count_file_path, intersect_file_path, type="peak"):
        """
        Reading data from peak_file_path and intersect_file_path, and format them in specific format
        :param count_file_path: The path for counting file
        :param intersect_file_path: The path for intersect path
        :return: Count File Data, Intersect File Data, Intersect Dictionary Data
        """
        s = time.time()
        header_names = ['chrome', 'start', 'end', 'seg', 'number']
        data = pandas.read_csv(count_file_path, sep='\t', header=None, names=header_names)
        peak_data = data[data['number'] != 0]
        middle = time.time()
        print("Reading Count File: {}seconds".format(middle - s))
        header_names = ['chrome', 'start', 'end', 'name', "chrome2", "seg1", "seg2", "seg3"]
        intersect_data = pandas.read_csv(intersect_file_path, sep='\t', header=None, names=header_names)
        names = intersect_data['name'].tolist()
        final = time.time()
        print("Reading Intersect File: {}seconds".format(final - middle))
        dictionary = {}
        last = ""
        temp = []
        counter = 0
        for each in names:
            if last == "":
                last = each
                temp.append(counter)
            elif each == last:
                temp.append(counter)
            else:
                dictionary[last] = temp
                last = each
                temp = [counter]
            counter += 1
        dictionary[last] = temp
        print("Finishing Dictionary {} seconds".format(time.time() - final))
        print("Finishing Reading Data {} seconds".format(time.time() - s))
        if type == "peak":
            self.peak_data = peak_data
            self.peak_intersect_data = intersect_data
            self.peak_dictionary = dictionary
        else:
            self.bg_data = peak_data
            self.bg_intersect_data = intersect_data
            self.bg_dictionary = dictionary

    def run(self):
        """
        The main function to run this module
        :return: null
        """
        s = time.time()
        print("-" * 5 + "First Round File" + "-" * 5)
        self.__reading_file(self.bg_path, self.bg_intersect_path, type="bg")
        print("-" * 5 + "Second Round File" + "-" * 5)
        self.__reading_file(self.peak_path, self.peak_intersect_path)

        for number in range(math.ceil(self.cell_number / self.core_number)):
            temp = time.time()

            process = []
            for iteration in range(self.core_number):
                distribution = np.random.normal(math.log(self.fragment_number), self.frag_num_var)
                cell_frag_num = math.exp(distribution)
                if cell_frag_num > self.max_threshold:
                    cell_frag_num = self.max_threshold
                if cell_frag_num < self.min_threshold:
                    cell_frag_num = self.min_threshold

                order = number * self.core_number + iteration
                print('-' * 5 + str(order) + '-' * 5)
                peak_round_1 = int(round(cell_frag_num * self.signal2noise / 2))
                peak_round_2 = int(round(cell_frag_num * self.signal2noise) - peak_round_1)
                bg_round_1 = int(round(cell_frag_num * (1.0 - self.signal2noise) / 2))
                bg_round_2 = int(cell_frag_num - peak_round_1 - peak_round_2 - bg_round_1)
                print("Cell_Frag_Num:{} Peak_Round_1:{} Peak_Round_2 Bg_Round_1:{} Bg_Round_2:{}"
                      .format(cell_frag_num, peak_round_1, peak_round_2, bg_round_1, bg_round_2))
                print("Started Peak Sample")
                print("Size:{} Peak_Round_1:{} Peak_Round_2:{} Bg_Round_1:{} Bg_Round_2:{}"
                      .format(cell_frag_num, peak_round_1, peak_round_2, bg_round_1, bg_round_2))
                t = multiprocessing.Process(
                    target=self.__multi_core_function(peak_round_1, peak_round_2, bg_round_1, bg_round_2, order))
                t.start()
                process.append(t)
            for p in process:
                p.join()
            print("One Iteration:")
            print(time.time() - temp)
        print("Total Time :::::::")
        print(time.time() - s)

    def __multi_core_function(self, peak_round_1, peak_round_2, bg_round_1, bg_round_2, order):
        """
        Used to group all the four sample functions in one function in order to pass them to one CPU CORE.
        :param peak_round_1: The number of first round to sample the peak data
        :param peak_round_2: The number of second round to sample the peak data
        :param bg_round_1: The number of first round to sample the background data
        :param bg_round_2: The number of second round to sample the background data
        :param order: The order of this cell
        :return null
        """
        self.__first_sample(self.peak_data, self.peak_intersect_data, self.peak_dictionary, peak_round_1, order,
                            "peak_round_1")
        self.__first_sample(self.peak_data, self.peak_intersect_data, self.peak_dictionary, peak_round_2, order,
                            "peak_round_2")
        self.__first_sample(self.bg_data, self.bg_intersect_data, self.bg_dictionary, bg_round_1, order, "bg_round_1")
        self.__first_sample(self.bg_data, self.bg_intersect_data, self.bg_dictionary, bg_round_2, order, "bg_round_2")

    def __first_sample(self, data, intersect_data, dictionary, size, order, t="normal"):
        """
        This is function will read the data from the path and pass the n, weight and size to sample_int_expjs to get the
        sample position
        :param data: Counting Data. Generated by reading_file().
        :param intersect_data: Intersect Data. Generated by reading_file().
        :param dictionary: Intersect Data Dictionary. Generated by reading_file().
        :param size: The number of zones you want to sample from all the zones.
        :param order: The order of this cell
        :param t: The type of this sample, e.g. Peak Data, Background Data, etc. Default Value is normal.
        :return: null
        """
        print("-----------First Sample {} No.{}----------------".format(t, order))
        begin = time.time()
        weight = data['number'].tolist()
        middle = time.time()
        print("Loading Cost:{} seconds".format(middle - begin))
        # sample
        samp = self.sample_int_expj(len(weight), size, weight)
        ending = time.time()
        print("Sample Cost:{} seconds".format(ending - middle))
        # store information
        first_store_path = "first.h5"
        if os.path.exists(first_store_path):
            output = h5py.File(first_store_path, "w")
        else:
            output = h5py.File("first.h5", "a")
        column1 = data['chrome'].tolist()
        column2 = data['start'].tolist()
        column3 = data['end'].tolist()
        column4 = data['seg'].tolist()
        chromosome = list(map(lambda x: column1[x - 1].encode(), samp))
        start_zone = list(map(lambda x: column2[x - 1], samp))
        end_zone = list(map(lambda x: column3[x - 1], samp))
        samp_name = list(map(lambda x: column4[x - 1], samp))
        cell_id = [order for p in range(len(samp))]

        output['chromosome'] = chromosome
        output['start'] = start_zone
        output['end'] = end_zone
        output['cell_id'] = cell_id
        output.close()
        print("Saving Cost:{} seconds".format(time.time() - ending))
        self.__second_sample(intersect_data, dictionary, samp_name, order, t)

    def __check_args(self, n, size):
        """
        Check whether size is less than n and whether n is equal to the length of prob.
        Because we have to select size numbers from n numbers. So we have to ensure size <= n
        If it doesn't conform to the rule, the program will exit.
        :param n: the length of prob
        :param size: the number of samples we want to sample
        """
        # Judge whether size <= n
        if n < size:
            print("Cannot take a sample larger than the population")
            sys.exit(-1)

    def __second_sample(self, data, dictionary, sample_name, order, t="normal"):
        """
        Read data, process data, conduct the second step sample, return the result.
        :param data: Intersect Data. Passed by first_sample
        :param dictionary: Intersect Dictionary Data. Passed by fisrt_sample.
        :param sample_name: The sample name for all the sampled zones.
        :param order: The order of this cell
        :param t: The type of this sample, e.g. Peak Data, Background Data, etc. Default Value is normal.
        """
        # Initial the data header and use the name column as the ID to classify.
        print("-----------Second Sample {} No.{}---------------".format(t, order))
        print("Start Loading...")
        middle = time.time()

        chromosome = []
        start_zone = []
        end_zone = []
        cell_id = []
        for each in sample_name:
            samp_list = dictionary[each]
            select_number = random.randint(0, len(samp_list) - 1)
            random_select = data.iloc[samp_list[select_number]]
            chromosome.append(random_select['chrome2'].encode())
            start_zone.append(random_select['seg1'])
            end_zone.append(random_select['seg2'])
            cell_id.append(order)
        last = time.time()
        print("Sample Cost:{} seconds".format(last - middle))

        # store information
        second_store_path = self.second_sample_save_path
        if os.path.exists(second_store_path):
            output = h5py.File(second_store_path, "w")
        else:
            output = h5py.File(second_store_path, "a")

        output['chromosome'] = chromosome
        output['start'] = start_zone
        output['end'] = end_zone
        output['cell_id'] = cell_id
        output.close()
        print("Saving Cost:{} seconds".format(time.time() - last))

    def sample_int_expj(self, n, size, prob):
        """
        Sampling will be performed according to the weight of each member of the population.
        :param n: The number of all the zones in a tissue.
        :param size: The number of how many zones we want to sampled out.
        :param prob: The probabilities for every zone in a numpy(float32) format.
        :return List including the weighted sample position.
        """
        self.__check_args(n, size)

        # Corner case
        if size == 0:
            return np.zeros(0)
        random.seed(int(time.time()))
        # part 1
        prob = np.array(prob)
        R = []
        for i in range(0, size):
            k_i = random.expovariate(1) / prob[i]
            heapq.heappush(R, (-k_i, k_i, i + 1))
        # part 2
        i = size
        while i < n:
            T_w = R[0]
            X_w = random.expovariate(1) / T_w[1]
            w = 0.0
            for p in range(i, n):
                w += prob[p]
                if X_w < w:
                    break
                i += 1

            if i >= n:
                break
            #
            t_w = -T_w[1] * prob[i]
            #
            e_2 = math.log(random.uniform(math.exp(t_w), 1.0), math.e)
            if prob[i] != 0:
                k_i = -e_2 / prob[i]
            else:
                k_i = math.inf

            heapq.heappop(R)
            heapq.heappush(R, (-k_i, k_i, i + 1))
            i += 1
        # part 3
        ret = np.zeros(size, dtype=int)
        for i in range(size - 1, -1, -1):
            if len(R) == 0:
                print("Reservoir empty before all elements have been filled")
                break
            ret[size - i - 1] = R[-1][2]
            R.pop()

        if len(R):
            print("Reservoir not empty after all elements have been filled")
        return ret.tolist()
