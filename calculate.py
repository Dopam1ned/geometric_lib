from geometric_lib.circle import (
    area as circle_area,
    perimeter as circle_perimeter
)
from geometric_lib.square import (
    area as square_area,
    perimeter as square_perimeter
)
from geometric_lib.triangle import (
    area as triangle_area,
    perimeter as triangle_perimeter
)


fig_funcs = {
    'circle': {'area': circle_area, 'perimeter': circle_perimeter},
    'square': {'area': square_area, 'perimeter': square_perimeter},
    'triangle': {'area': triangle_area, 'perimeter': triangle_perimeter}
}


def calc(fig, func, size):
    assert fig in fig_funcs
    assert func in fig_funcs[fig]

    return fig_funcs[fig][func](*size)


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, avaliable are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input(
            "Input figure sizes separated by space, 1 for circle and square\n"
        ).split(' ')))

    calc(fig, func, size)
