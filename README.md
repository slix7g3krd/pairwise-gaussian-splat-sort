# pairwise-gaussian-splat-sort

## 领域

游戏、图形与多媒体

## 主题

高斯泼溅排序与卸载

## 说明

排序栅栏、延迟回收与亚像素覆盖。

初始状态下 `graphics/gaussian_splat_sort.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
