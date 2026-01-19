from dataclasses import dataclass

@dataclass
class Sums:
    square: int = 0
    row: int = 0
    col: int = 0


class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        sums_mat = [[Sums() for _ in range(n)] for _ in range(m)]
        max_length = min(m, n)
        for length in range(max_length):
            if length:
                has_valid_square = self._growSquares(sums_mat, mat, length, threshold)
            else:
                has_valid_square = self._createSquares(sums_mat, mat, threshold)
            if not has_valid_square:
                return length
        return max_length

    def _growSquares(
            self, sums_mat: list[list[Sums]], mat: list[list[int]],
            length: int, threshold: int) -> bool:
        m = len(mat) - length
        n = len(mat[0]) - length
        return self._updateSquares(sums_mat, mat, m, n, self._growSquare, threshold)

    def _createSquares(
            self, sums_mat: list[list[Sums]], mat: list[list[int]],
            threshold: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        return self._updateSquares(sums_mat, mat, m, n, self._createSquare, threshold)

    def _updateSquares(
            self, sums_mat: list[list[Sums]], mat: list[list[int]], m: int, n: int,
            sums_updater: Callable[[list[list[Sums]], list[list[int]], int, int], int],
            threshold: int) -> bool:
        has_valid_square = False
        for i in range(m):
            for j in range(n):
                area = sums_updater(sums_mat, mat, i, j)
                has_valid_square = has_valid_square or area <= threshold
        return has_valid_square

    def _growSquare(
            self, sums_mat: list[list[Sums]], mat: list[list[int]], i: int, j: int) -> int:
        value = mat[i][j]
        next_square_sum = sums_mat[i + 1][j + 1].square
        next_row_sum = sums_mat[i][j + 1].row
        next_col_sum = sums_mat[i + 1][j].col
        sums = sums_mat[i][j]
        sums.square = value + next_square_sum + next_row_sum + next_col_sum
        sums.row = value + next_row_sum
        sums.col = value + next_col_sum
        return sums.square

    def _createSquare(
            self, sums_mat: list[list[Sums]], mat: list[list[int]], i: int, j: int) -> int:
        value = mat[i][j]
        sums = sums_mat[i][j]
        sums.square = value
        sums.row = value
        sums.col = value
        return sums.square