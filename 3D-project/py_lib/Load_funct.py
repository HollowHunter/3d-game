def load(file, k=1):
    name = ''
    plots = []  # точки в пространстве
    polygons = []  # полигоны (номера точек)
    tex_plots = []  # текстурные координаты
    surfaces = []  # полигоны на текстуре
    plots_normals = []  # нормали
    normals = []  # номера нормалей в полигонах
    with open(file) as file:
        for line in file.readlines():

            data = line.split()
            if data == []:
                continue
            elif data[0] == 'v':
                plots.append([float(data[1]) * k, float(data[3]) * k, -float(data[2]) * k])
            elif data[0] == 'vt':
                tex_plots.append([float(data[1]), 1-float(data[2])])
            elif data[0] == 'vn':
                plots_normals.append([float(data[1]), float(data[3]), -float(data[2])])
            elif data[0] == 'f':
                polygon = list(map(lambda a: int(a.split('/')[0]) - 1, data[1:]))
                texture = list(map(lambda a: int(a.split('/')[1]) - 1, data[1:]))
                normal_pol = list(map(lambda a: int(a.split('/')[1]) - 1, data[1:]))
                if len(polygon) == 3:
                    polygons.append(polygon)
                    surfaces.append(texture)
                    normals.append(normal_pol)
                elif len(polygon) > 3:
                    polygons.extend([(polygon[0], polygon[i], polygon[i + 1]) for i in range(len(polygon) - 1)])
                    surfaces.extend([(texture[0], texture[i], texture[i + 1]) for i in range(len(texture) - 1)])
                    normals.extend(
                        [(normal_pol[0], normal_pol[i], normal_pol[i + 1]) for i in range(len(normal_pol) - 1)])
    print(plots)
    return [plots, polygons, tex_plots, surfaces, plots_normals, normals]


plots = [[0, 0.5, 0, 5], [0, -0.5, 0, 5], [0, 0.5, -0, 5], [0, -0.5, -0, 5]]  # точки в пространстве
polygons = [[0, 1, 2], [0, 3, 2]]  # полигоны (номера точек)
tex_plots = [[0, 0], [1, 0], [0, 1], [1, 1]]  # текстурные координаты
surfaces = [[0, 2, 1], [0, 1, 3]]  # полигоны на текстуре
plots_normals = [[...], [...], ...]  # нормали
normals = [[0, 1, 2]]  # номера нормалей в полигонах
