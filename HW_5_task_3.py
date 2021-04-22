from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена']

klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

tutors_to_klasses = ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses) if klasses is not None)

print(*tutors_to_klasses)
