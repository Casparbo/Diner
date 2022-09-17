import random as rand
import os
import argparse
import copy


def read(files):
	courses = []

	for file in files:
		with open(file) as f:
			menu = dict()
			menu["appetizer"] = f.readline()
			menu["main"] = f.readline()
			menu["dessert"] = f.readline()

			courses.append(menu)

	return courses


def mix(courses):
	local_courses = copy.deepcopy(courses)
	new_courses = []
	for menu_id in range(len(courses)):
		available_menus = [local_courses[i] for i in range(len(local_courses)) if i != menu_id]
		new_menu = dict()

		if available_menus in ([{'appetizer': 'bla1\n'}, {}, {}], [{'main': 'bla2\n'}, {}, {}], [{'dessert': 'bla3'}, {}, {}]):
			return false

		appetizer_menu = rand.choice([a_m for a_m in available_menus if "appetizer" in a_m])
		main_menu = rand.choice([a_m for a_m in available_menus if "main" in a_m and a_m is not appetizer_menu])
		dessert_menu = rand.choice([a_m for a_m in available_menus if "dessert" in a_m and a_m is not appetizer_menu and a_m is not main_menu])

		new_menu["appetizer"] = appetizer_menu["appetizer"]
		new_menu["main"] = main_menu["main"]
		new_menu["dessert"] = dessert_menu["dessert"]


		new_courses.append(new_menu)

		del appetizer_menu["appetizer"]
		del main_menu["main"]
		del dessert_menu["dessert"]


	return new_courses



def write(files, courses):
	for file, course in zip(files, courses):
		with open(f"new_{file}", "w") as f:
			f.write("".join(course.values()))


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("files", nargs="+")
	args = parser.parse_args()

	courses = read(args.files)

	while True:
		try:
			new_courses = mix(courses)
			break
		except IndexError:
			continue

	write(args.files, new_courses)



if __name__ == '__main__':
	main()