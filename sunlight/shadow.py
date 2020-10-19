import math
class Shadow:
	def __init__(self, building):
		self.building = building

	def compute_length(self, alpha):
		return self.building.get_height() / math.tan(alpha)

	def __line_params(self, p1, p2):
		x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]

		m = (y2-y1)/(x2-x1)
		b = y1-m*x1

		return m, b

	def __slope2angle(self, m):
		angle = math.atan(m)
		return angle if angle >= 0 else angle + math.pi

	def compute_intersection_angle(self, xp, yp):
		xb, yb = self.building.get_distance(), self.building.get_height()

		m, _ = self.__line_params((xp, yp), (xb, yb))
		
		if xb < xp:
			# building on the east, the sun is raising, the slope must be negative, else 0
			m = m if m <= 0 else 0
			angle = math.pi if m==0 else self.__slope2angle(m)
		else:
			# building on the west, the sun is setting, the slope must be positive, else math.pi
			m = m if m >= 0 else 0
			angle = 0 if m==0 else self.__slope2angle(m)

		return math.pi - angle