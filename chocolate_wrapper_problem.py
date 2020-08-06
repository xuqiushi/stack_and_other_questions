"""
Description
Sanjay has m rupees, each chocolate costs c rupees, shopkeeper will give away k chocolates for w wrappers. Can you find now how many chocolates Sanjay will be able to eat?
Input: 4 integers separated by space in order m, c, w, k
integers c and w will be >0
integers m and k will be >=0
integer k will be
Output: An integer denoting number of chocolates Sanjay will be able to get.
Sample input:
15, 2, 3, 1
Sample output:
10
Explanation:
Sanjay has 15 rupees, buys 7 chocolates for 2 rupees each.
Sanjay now has 7 wrappers, exchanges 6 of them for 2 more chocolates.
Sanjay now has 3 wrappers and exchanges them for 1 more chocolate making a total of 10 chocolates
Sample input:
15, 2, 3, 2
Sample output:
17
Explanation:
Sanjay has 15 rupees, buys 7 chocolates for 2 rupees each.
Sanjay now has 7 wrappers, exchanges 6 of them for 4 more chocolates.
Sanjay now has 5 wrappers and exchanges 3 of them for 2 more chocolates.
Sanjay now has 4 wrappers and exchanges 3 of them for 2 more chocolates.
Sanjay now has 3 wrappers and exchanges them for 2 chocolates making a total of 17 chocolates.
"""


class ChocolateProblem(object):
    def __init__(
        self, assets, unit_price, single_exchange_wrappers, singe_exchange_chocolates
    ):
        self.assets = assets
        self.unit_price = unit_price
        self.single_exchange_wrappers = single_exchange_wrappers
        self.singe_exchange_chocolates = singe_exchange_chocolates

    @classmethod
    def print_info(
        cls,
        remaining_assets,
        remaining_wrappers,
        remaining_chocolates,
        chocolates_bought_this_time=0,
    ):
        print(
            f"Remaining assets: {remaining_assets}, "
            f"Remaining wrappers: {remaining_wrappers}, "
            f"Remaining chocolates: {remaining_chocolates}, "
            f"Remaining chocolates this time: {chocolates_bought_this_time}"
        )

    def solve(self):
        remaining_assets = self.assets
        remaining_wrappers = 0
        remaining_chocolates = 0
        self.print_info(remaining_assets, remaining_wrappers, remaining_chocolates)
        chocolate_bought_first_time = remaining_assets // self.unit_price
        remaining_assets = remaining_assets % self.unit_price
        remaining_chocolates += chocolate_bought_first_time
        remaining_wrappers = chocolate_bought_first_time
        self.print_info(
            remaining_assets,
            remaining_wrappers,
            remaining_chocolates,
            chocolate_bought_first_time,
        )
        while remaining_wrappers >= self.single_exchange_wrappers:
            chocolate_bought_this_time = (
                remaining_wrappers // self.single_exchange_wrappers
            ) * self.singe_exchange_chocolates
            remaining_chocolates += chocolate_bought_this_time
            wrapper_remainder_this_time = (
                remaining_wrappers % self.single_exchange_wrappers
            )
            remaining_wrappers = (
                chocolate_bought_this_time + wrapper_remainder_this_time
            )
            self.print_info(
                remaining_assets,
                remaining_wrappers,
                remaining_chocolates,
                chocolates_bought_this_time=chocolate_bought_this_time,
            )


if __name__ == "__main__":
    chocolate_problem = ChocolateProblem(15, 2, 3, 1)
    chocolate_problem.solve()
    chocolate_problem = ChocolateProblem(15, 2, 3, 2)
    chocolate_problem.solve()
