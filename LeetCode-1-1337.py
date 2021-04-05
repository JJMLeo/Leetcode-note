# 简单

# 2021.4.5 运行出错
# 输入：
# [[1,1,1,0,0,0,0],[1,1,1,1,1,1,0],[0,0,0,0,0,0,0],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1]]
# 4
# 输出：
# [2,0,3,4]
# 预期结果：
# [2,0,3,1]

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        idx_0 = [m] * m
        # 返回每一行第一个0的位置
        for i in range(m):
            try:
                idx_0[i] = mat[i].index(0)
            except ValueError:
                pass
        # 行数与0的位置对应
        idx_list = list(tuple(zip(range(m),idx_0)))
        # 排序
        idx_sorted = sorted(idx_list, key=lambda x: x[1])
        idx_ = [i for [i,v] in idx_sorted]
        # 返回行数
        return idx_[:k]
