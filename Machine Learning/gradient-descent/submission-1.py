class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:

        minimizer = init

        for _ in range(iterations): 
            d = 2 * minimizer
            minimizer = minimizer - learning_rate * d

        return round(minimizer, 5)