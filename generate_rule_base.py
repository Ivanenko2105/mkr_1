from model import input_lvs
from itertools import product

area = {"far": 1,
		"medium": 0.5,
		"close": 0}

сondition = {"low": 1,
		 "medium": 0.5,
		 "high": 0}

floor = {"recedes": 1,
		     "stays in place": 0.5,
		     "approaches": 0}

coef = {"Area": 0.333,
		"Floor": 0.333,
		"Condition": 0.333}

Class = {
		"slowly moving forward": 0.55,
		"іmmobile": 0.45,
		"slowly moves back": 0}


# Извлекаем имена терминов принадлежности для каждой переменной
term_names_lists = [list(var['terms'].keys()) for var in input_lvs]

# Создаем список кортежей всех возможных комбинаций
combinations = list(product(*term_names_lists))
rule_base = []
values = set()
for comb in combinations:
	area_coef = area[comb[0]] * coef["Area"]
	floor_coef = floor[comb[1]] * coef["Floor"]
	age_coef = сondition[comb[2]] * coef["Condition"]
	res = area_coef + floor_coef + age_coef
	values.add(res)

	for key, value in Class.items():
		if res >= value:
			rule_base.append((comb, key))
			break

# for value in sorted(values):
# 	print(value)

# print(len(values))

for rule in rule_base:
	print(str(rule) + ",")

