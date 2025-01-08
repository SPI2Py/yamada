from cypari import pari
from yamada import SpatialGraphDiagram, Edge, Crossing, has_r1, apply_r1



# %% Test the R1 move on unknots

def test_r1_1():
    a = pari('A')

    yp_ground_truth = -a ** 2 - a - 1

    x1 = Crossing('x1')
    x1[1], x1[3] = x1[2], x1[0]

    e0, e1 = Edge(0), Edge(1)

    e0[0], e0[1] = x1[0], x1[3]
    e1[0], e1[1] = x1[2], x1[1]

    sgd = SpatialGraphDiagram([x1, e0, e1])

    yp_before_r1 = sgd.yamada_polynomial()

    assert yp_before_r1 == yp_ground_truth

    r1_crossing_labels = has_r1(sgd)

    assert len(r1_crossing_labels) == 1
    assert 'x1' in r1_crossing_labels

    sgd = apply_r1(sgd, 'x1')

    yp_after_r1 = sgd.yamada_polynomial()

    assert yp_after_r1 == yp_ground_truth


def test_r1_2():
    a = pari('A')

    yp_ground_truth = -a ** 2 - a - 1

    x1 = Crossing('x1')
    x1[1], x1[3] = x1[2], x1[0]

    sgd = SpatialGraphDiagram([x1])

    yp_before_r1 = sgd.yamada_polynomial()

    assert yp_before_r1 == yp_ground_truth

    r1_crossing_labels = has_r1(sgd)

    assert len(r1_crossing_labels) == 1
    assert 'x1' in r1_crossing_labels

    sgd = apply_r1(sgd, 'x1')

    yp_after_r1 = sgd.yamada_polynomial()

    assert yp_after_r1 == yp_ground_truth


def test_r1_3():
    a = pari('A')

    yp_ground_truth = -a ** 2 - a - 1

    x1 = Crossing('x1')
    x2 = Crossing('x2')

    e1, e2, e3, e4 = Edge(1), Edge(2), Edge(3), Edge(4)

    x2[3] = e1[0]
    x2[0] = e1[1]
    x2[1] = e2[0]
    x2[2] = e4[1]

    x1[2] = e2[1]
    x1[1] = e4[0]
    x1[0] = e3[1]
    x1[3] = e3[0]

    sgd = SpatialGraphDiagram([x1, x2, e1, e2, e3, e4])

    yp_before_r1s = sgd.yamada_polynomial()

    assert yp_before_r1s == yp_ground_truth

    r1_crossing_labels = has_r1(sgd)

    assert len(r1_crossing_labels) == 2
    assert 'x1' in r1_crossing_labels and 'x2' in r1_crossing_labels

    sgd = apply_r1(sgd, 'x1')

    yp_after_first_r1 = sgd.yamada_polynomial()

    assert yp_after_first_r1 == yp_ground_truth

    r1_crossing_labels = has_r1(sgd)

    assert len(r1_crossing_labels) == 1
    assert 'x2' in r1_crossing_labels

    sgd = apply_r1(sgd, 'x2')

    yp_after_second_r1 = sgd.yamada_polynomial()

    assert yp_after_second_r1 == yp_ground_truth

    r1_crossing_labels = has_r1(sgd)

    assert len(r1_crossing_labels) == 0


def test_r1_4():
    a = pari('A')

    yp_ground_truth = -a ** 2 - a - 1

    x1 = Crossing('x1')
    x2 = Crossing('x2')

    e1, e2, e3, e4 = Edge(1), Edge(2), Edge(3), Edge(4)

    x2[3] = e4[1]
    x2[0] = e1[0]
    x2[1] = e1[1]
    x2[2] = e2[0]

    x1[2] = e2[1]
    x1[1] = e4[0]
    x1[0] = e3[1]
    x1[3] = e3[0]

    sgd = SpatialGraphDiagram([x1, x2, e1, e2, e3, e4])

    yp_before_r1s = sgd.yamada_polynomial()

    assert yp_before_r1s == yp_ground_truth

    r1_crossing_labels = has_r1(sgd)

    assert len(r1_crossing_labels) == 2
    assert 'x1' in r1_crossing_labels and 'x2' in r1_crossing_labels

    sgd = apply_r1(sgd, 'x1')

    yp_after_first_r1 = sgd.yamada_polynomial()

    assert yp_after_first_r1 == yp_ground_truth

    r1_crossing_labels = has_r1(sgd)

    assert len(r1_crossing_labels) == 1
    assert 'x2' in r1_crossing_labels

    sgd = apply_r1(sgd, 'x2')

    yp_after_second_r1 = sgd.yamada_polynomial()

    assert yp_after_second_r1 == yp_ground_truth

    r1_crossing_labels = has_r1(sgd)

    assert len(r1_crossing_labels) == 0