import png, numpy, Queue, operator, itertools

def is_white(coord, image):
    """ Returns whether (x, y) is approx. a white pixel."""
    a = True
    for i in xrange(3):
        if not a: break
        a = image[coord[1]][coord[0] * 3 + i] > 240
    return a

def bfs(s, e, i, visited):
    """ Perform a breadth-first search. """
    frontier = Queue.Queue()
    while s != e:
        for d in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            np = tuple(map(operator.add, s, d))
            if is_white(np, i) and np not in visited:
                frontier.put(np)
        visited.append(s)
        s = frontier.get()
    return visited

def main():
    r = png.Reader(filename = "examples/normal.png")
    rows, cols, pixels, meta = r.asDirect()
    assert meta['planes'] == 3 # ensure the file is RGB
    image2d = numpy.vstack(itertools.imap(numpy.uint8, pixels))
    start, end = (402, 985), (398, 27)
    print (bfs(start, end, image2d, []))