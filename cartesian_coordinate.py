class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

    def __str__(self):
        return f"({self.x}, {self.y})"

# Example usage
if __name__ == "__main__":
    point1 = Point(3, 4)
    point2 = Point(6, 8)
    print(f"Point 1: {point1}")
    print(f"Point 2: {point2}")
    print(f"Distance between Point 1 and Point 2: {point1.distance_to(point2)}")