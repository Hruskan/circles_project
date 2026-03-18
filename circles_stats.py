def radius_sum(r1, r2):
    return (r1 + r2)
def euclid_distance(x1, y1, x2, y2):
    return ((((x2-x1)**2)+((y2-y1)**2))**(1/2))
def has_intersection(circle_1, circle_2):
    intersections = 0
    if euclid_distance(circle_1["x"], circle_2["x"], circle_1["y"], circle_2["y"]) == radius_sum(circle_1["r"], circle_2["r"]):
        intersections += 1
    if euclid_distance(circle_1["x"], circle_2["x"], circle_1["y"], circle_2["y"]) < radius_sum(circle_1["r"], circle_2["r"]):
        intersections += 2
    if intersections > 0:
        intersection = True
    return {"intersects": intersection, "intersections": intersections}
