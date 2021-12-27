if __name__ == "__main__":
    from collections import OrderedDict
    import numpy as np
    from sklearn.preprocessing import MultiLabelBinarizer

    class DuplicateFinder(object):
        def __init__(self, raw_list):
            self.raw_list = raw_list
            self.multi_label_encoder = MultiLabelBinarizer()
            self.final_results = OrderedDict()
            self.title_select = []
            self.content_select = []
            self.not_select = []

        @property
        def match_result(self):
            label_matrix = self.multi_label_encoder.fit_transform(self.raw_list)
            return np.dot(label_matrix, label_matrix.T)

        @property
        def raw_results(self):
            return np.array(np.where(self.match_result >= 3)).T

        def solve(self):
            for result in self.raw_results:
                if result[0] == result[1]:
                    continue
                if result[0] in self.content_select:
                    continue
                if result[0] not in self.final_results:
                    self.final_results[result[0]] = []
                    self.final_results[result[0]].append(result[1])
                    self.title_select.append(result[0])
                    self.content_select.append(result[1])
                elif result[1] not in self.content_select + self.title_select:
                    self.final_results[result[0]].append(result[1])
                    self.content_select.append(result[1])
                else:
                    continue
            self.not_select = list(
                set(range(self.match_result.shape[0]))
                - set(self.title_select + self.content_select)
            )

        def print_result(self):
            print(f"This is more than one matched: {self.final_results}")
            for key in self.final_results:
                print(self.raw_list[key])
            print(f"This is just one: {self.not_select}")
            for key in self.not_select:
                print(self.raw_list[key])

    list1 = [
        ("Ram", "Laxman", "Bharat", "Sita"),
        ("Ram", "Ravan", "Bharat", "Sita"),
        ("Ram", "Luv", "Dashrat", "Sita"),
        ("Dasrath", "Kekei", "Bharat", "Ram"),
        ("Laxman", "Bharat", "Ram", "Hanuman"),
        ("Hanuman", "Sita", "Kekei", "Ravan"),
        ("Ram", "Sita", "Hanuman", "Ravan"),
    ]
    solver = DuplicateFinder(list1)
    solver.solve()
    solver.print_result()
