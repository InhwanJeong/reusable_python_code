""" generate dummy gps data, ver0.1

developed by inhwanJeong
release on 07/28/2022(2022.07.28)
feedback: ghjklla007@naver.com

"""

import random
from tqdm import trange


class GenerateGpsCoordinates:
    """
    Dummy GPS coordinates generated Decimal degrees
        e.g. (latitude: 35.122242, longitude: 128.964089)

    :parameter seed: The seed is used for getting fixed data,
    :type seed: int

    """
    def __init__(self, seed: int = None):
        self.latitude_start_point = 34.738741
        self.latitude_end_point = 37.792874
        self.longitude_start_point = 126.402920
        self.longitude_end_point = 129.375212

        if seed:
            random.seed(seed)

    def generate_coordinates(self) -> list:
        """
            GPS coordinates - tuple
                e.g. Decimal degrees (DD): 35.122242, 128.964089.
        :return: list(tuple, tuple, ..., tuple)
        """
        coordinates_list = [
            (round(random.uniform(self.latitude_start_point, self.latitude_end_point), 6),
             round(random.uniform(self.longitude_start_point, self.longitude_end_point), 6))
            for _ in trange(10000)
        ]

        return coordinates_list


if __name__ == '__main__':
    gps_generate_object = GenerateGpsCoordinates()
    gps_list = gps_generate_object.generate_coordinates()

    print(gps_list[0])
