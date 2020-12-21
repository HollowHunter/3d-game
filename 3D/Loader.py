class ObjectLoader:
    def load(file):
        plots = []
        polygons = []
        with open(file) as file:
            for line in file.readlines():
                data = line.split()
                if data[0] == 'v':
                    plots.append((float(data[1]), float(data[3]), -float(data[2])))
                elif data[0] == 'f':
                    polygon = (tuple(map(lambda a: int(a.split('/')[0]) - 1, data[1:])))
                    if len(polygon) == 3:
                        polygons.append(polygon)
                    elif len(polygon) > 3:
                        polygons.extend([(polygon[0], polygon[i], polygon[i + 1]) for i in range(len(polygon) - 1)])
        return plots, polygons
