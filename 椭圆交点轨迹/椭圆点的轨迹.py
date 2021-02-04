from sympy import symbols, Eq, sqrt, diff, solve, pprint
from sympy.plotting import plot_parametric, plot

if __name__ == "__main__":

    # 定义变量
    x, y, b, z = symbols("x y b z")
    # 定义原始椭圆
    origin_ellipses = Eq(x ** 2 / 6 + y ** 2 / b ** 2, 1)
    print(f"{'原始椭圆为':=^20}")
    pprint(origin_ellipses)
    # 定义b所在另一个椭圆
    new_ellipses = Eq(y ** 2 / 6 + x ** 2 / (6 - b ** 2), 1)
    print(f"{'b所在另一椭圆为':=^20}")
    pprint(origin_ellipses)
    # 求解交点之一
    Intersections = solve([origin_ellipses, new_ellipses], x, y)
    pprint(f"{'交点为:':=^20}")
    for point in Intersections:
        pprint(point)
    # 绘制此交点轨迹
    plot_parametric(*[(point[0], point[1], (b, 0, sqrt(6))) for point in Intersections])
    # 另一线段长度，因为平方，所以其实四个函数可以看做一个
    line_length = sqrt(x ** 2 + y ** 2)
    line_length_list = [
        line_length.subs({x: point[0], y: point[1]}) for point in Intersections
    ]
    line_length = line_length_list[0]
    pprint(f"{'线段长度为:':=^20}")
    pprint(line_length)
    # 绘制长度曲线
    plot((line_length_list[0], (b, 0, sqrt(6))))
    # 求导
    line_length_diff = line_length.diff()
    pprint(f"{'导数为:':=^20}")
    pprint(line_length_diff)
    # 求导数零点
    zero_point = solve(diff(line_length_list[0], b), dict=True)
    pprint(f"{'零点为:':=^20}")
    pprint(zero_point)
    pprint(f"{'最短长度为:':=^20}")
    pprint([line_length.subs(point) for point in zero_point])
