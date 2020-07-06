def points_on_segments(segments):
    """
    segments - list of segments
    example:
            [[2, 3], [2, 6], [1, 8]]

    возращает оптимальное число точек, которыми нужно покрыть все отрезки,
    чтобы каждый из отрезков содержал хотя бы одну точку
    """
    assert isinstance(segments, list)
    assert len(segments) > 0
    assert len(segments[0]) == 2

    # отсортируем отрезки по левым концам
    segments = sorted(segments)

    points = []
    while len(segments) > 0:
        # первая точка - левый конец самого последнего отрезка
        points.append(segments[-1][0])

        # удаляем те отрезки, на которые попала первая точка
        segments = [i for i in segments if points[-1] not in range(i[0], i[1] + 1)]

    return points
