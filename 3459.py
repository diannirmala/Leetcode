class Solution(object):
    def lenOfVDiagonal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        # directions: 0=NE, 1=SE, 2=SW, 3=NW
        dirs = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
        cw = [1, 2, 3, 0]

        # helper: iterate order so that next cell (i+di, j+dj) is computed first
        def order(di, dj):
            # if di = +1 -> need to iterate i from bottom->top (n-1..0) so next (i+1) is out of range or already done
            # if di = -1 -> i from top->bottom
            ir = range(0, n) if di == -1 else range(n - 1, -1, -1)
            # if dj = +1 -> j from right->left (m-1..0); if dj = -1 -> left->right
            jr = range(m - 1, -1, -1) if dj == +1 else range(0, m)
            return ir, jr

        # ALT[d][i][j]: panjang alternating (0/2) lurus dari (i,j) ke arah d (termasuk sel ini)
        ALT = []
        for d in range(4):
            di, dj = dirs[d]
            ir, jr = order(di, dj)
            alt = [[0]*m for _ in range(n)]
            for i in ir:
                row = grid[i]
                for j in jr:
                    v = row[j]
                    if v == 0 or v == 2:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m and (grid[ni][nj] == (0 if v == 2 else 2)):
                            alt[i][j] = 1 + alt[ni][nj]
                        else:
                            alt[i][j] = 1
                    # else alt default 0
            ALT.append(alt)

        # BEST[d][i][j]: mulai dari (i,j) (harus 0/2), boleh 1x belok cw(d); setelah belok -> lurus saja
        BEST = []
        for d in range(4):
            di, dj = dirs[d]
            ir, jr = order(di, dj)
            best = [[0]*m for _ in range(n)]
            for i in ir:
                row = grid[i]
                for j in jr:
                    v = row[j]
                    if v != 0 and v != 2:
                        continue
                    # minimal: hanya sel ini
                    b = 1
                    # lurus (masih boleh belok nanti)
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and (grid[ni][nj] == (0 if v == 2 else 2)):
                        b = max(b, 1 + best[ni][nj])  # tetap di arah d

                    # belok sekarang (cw), setelah itu lurus (pakai ALT di arah baru)
                    d2 = cw[d]
                    di2, dj2 = dirs[d2]
                    ni2, nj2 = i + di2, j + dj2
                    if 0 <= ni2 < n and 0 <= nj2 < m and (grid[ni2][nj2] == (0 if v == 2 else 2)):
                        b = max(b, 1 + ALT[d2][ni2][nj2])

                    best[i][j] = b
            BEST.append(best)

        # jawab: mulai di setiap 1; tetangga pertama HARUS 2, lalu tambah BEST di arah tsb
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1:
                    continue
                # minimal 1 (hanya si '1' itu sendiri)
                best_here = 1
                for d in range(4):
                    di, dj = dirs[d]
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 2:
                        # start after '1' with a '2'
                        best_here = max(best_here, 1 + BEST[d][ni][nj])
                if best_here > ans:
                    ans = best_here
        return ans
    
solution = Solution()
print(solution.lenOfVDiagonal([[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]))
print(solution.lenOfVDiagonal([[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]))
print(solution.lenOfVDiagonal([[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]))
print(solution.lenOfVDiagonal([[1]]))