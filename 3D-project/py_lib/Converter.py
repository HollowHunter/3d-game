class Converter:
    def __init__(self, lib, ffi):
        """creates the bridge between the C code and Python"""
        self.lib = lib
        self.ffi = ffi
        self.INT_SIZE = self.lib.get_int_size()
        self.FLOAT_SIZE = self.lib.get_float_size()

    def to_int_array(self, data):
        res = []
        for num in data:
            pointer = self.lib.int_to_bytes(num)
            res += self.ffi.unpack(pointer, self.INT_SIZE)
            self.lib.free_mem(pointer)
        #        del(pointer)
        #        print(self.ffi.unpack(pointer, INT_SIZE))
        return bytes(res)

    def to_float_array(self, data):
        res = []
        for num in data:
            pointer = self.lib.float_to_bytes(num)
            res += self.ffi.unpack(pointer, self.INT_SIZE)
            self.lib.free_mem(pointer)
        #        del(pointer)
        #        print(self.ffi.unpack(pointer, INT_SIZE))
        return bytes(res)

    def to_int_list(self, data):
        res = []
        for i in range(0, len(data), self.INT_SIZE):
            res.append(0)
            for j in range(self.INT_SIZE - 1, -1, -1):
                #            print(i+j, len(data))
                res[-1] *= 256
                res[-1] += data[i + j]
        return res

    def convert_2d(self, array):
        res = []
        for i in array:
            res.extend(i)
        return res
