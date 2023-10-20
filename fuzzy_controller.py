import model
import inference_mamdani


class FuzzyController:
	def __init__(self) -> None:
		self.max_values = [5, 5, 5]
		self.min_values = [1, 1, 1]

		inference_mamdani.preprocessing(model.input_lvs, model.output_lv)
	
	def __normalization(self, x, min, max) -> float:
		"""
			Normalization of the quantity x in the interval [0,1]
		"""
		return round((x - min) / (max - min), 2)
	
	def __denormalization(self, y, min, max) -> int:
		"""
			Denormalization: from [0,1] to [Ymin, Ymax]
		"""
		print(y)
		coef = (max - min) / (0.8125438596491228 - 0.18745614035087718)
		return round((y - 0.18745614035087718) * coef + min)
	
	def get_result(self, crisp):
		normalization_crisp = []
		for i in range(len(crisp)):
			normalization_crisp.append(self.__normalization(crisp[i], self.min_values[i], self.max_values[i]))

		result = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, normalization_crisp)
		denormalization_result = self.__denormalization(result[0], 1, 5)
		return (result[1], denormalization_result)