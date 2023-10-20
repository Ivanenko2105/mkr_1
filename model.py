input_lvs = [
    {
        'X': (0, 1.01, 0.01),
        'name': 'Distance',
        'terms': {
            'close': ('trapmf', 0, 0, 0.25, 0.5),
            'medium': ('trapmf', 0.25, 0.4, 0.6, 0.75),
            'far': ('trapmf', 0.5, 0.75, 1, 1),
        }
    },

    {
        'X': (0, 1.01, 0.01),
        'name': 'Enemy condition',
        'terms': {
            'recedes': ('trapmf', 0, 0, 0.25, 0.4),
            'stays in place': ('trimf', 0.25, 0.5, 0.75),
            'approaches': ('trapmf', 0.6, 0.75, 1, 1),
        }
    },

    {
        'X': (0, 1.01, 0.01),
        'name': 'Danger',
        'terms': {
            'low': ('trapmf', 0, 0, 0.25, 0.35),
            'medium': ('trapmf', 0.2, 0.4, 0.6, 0.8),
            'high': ('trapmf', 0.65, 0.75, 1, 1),
        }
    },
]

output_lv = {
    'X': (0, 1.01, 0.01),
    'name': 'Character status',
    'terms': {
        'slowly moves back': ('trapmf', 0, 0, 0.3, 0.45),
        'іmmobile': ('trimf', 0.3, 0.5, 0.7),
        'slowly moving forward': ('trapmf', 0.55, 0.7, 1, 1)
    }
}


rule_base = [
	(('close', 'recedes', 'low'), 'slowly moving forward'),
	(('close', 'recedes', 'medium'), 'іmmobile'),
	(('close', 'recedes', 'high'), 'slowly moves back'),
	(('close', 'stays in place', 'low'), 'іmmobile'),
	(('close', 'stays in place', 'medium'), 'slowly moves back'),
	(('close', 'stays in place', 'high'), 'slowly moves back'),
	(('close', 'approaches', 'low'), 'slowly moves back'),
	(('close', 'approaches', 'medium'), 'slowly moves back'),
	(('close', 'approaches', 'high'), 'slowly moves back'),
	(('medium', 'recedes', 'low'), 'slowly moving forward'),
	(('medium', 'recedes', 'medium'), 'slowly moving forward'),
	(('medium', 'recedes', 'high'), 'іmmobile'),
	(('medium', 'stays in place', 'low'), 'slowly moving forward'),
	(('medium', 'stays in place', 'medium'), 'іmmobile'),
	(('medium', 'stays in place', 'high'), 'slowly moves back'),
	(('medium', 'approaches', 'low'), 'іmmobile'),
	(('medium', 'approaches', 'medium'), 'slowly moves back'),
	(('medium', 'approaches', 'high'), 'slowly moves back'),
	(('far', 'recedes', 'low'), 'slowly moving forward'),
	(('far', 'recedes', 'medium'), 'slowly moving forward'),
	(('far', 'recedes', 'high'), 'slowly moving forward'),
	(('far', 'stays in place', 'low'), 'slowly moving forward'),
	(('far', 'stays in place', 'medium'), 'slowly moving forward'),
	(('far', 'stays in place', 'high'), 'іmmobile'),
	(('far', 'approaches', 'low'), 'slowly moving forward'),
	(('far', 'approaches', 'medium'), 'іmmobile'),
	(('far', 'approaches', 'high'), 'slowly moves back')
]