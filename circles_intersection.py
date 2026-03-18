from circles_stats import has_intersection

circle_1 = {"x": 0, "y": 0, "r": 2}
circle_2 = {"x": 3, "y": 0, "r": 1}

result = circles_stats.has_intersection(circle_1, circle_2)

print(f"Intersects: {result["intersects"]}, Intersections: {result["intersections"]}")
